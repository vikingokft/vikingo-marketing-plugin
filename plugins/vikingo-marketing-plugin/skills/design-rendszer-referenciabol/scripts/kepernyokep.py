#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kepernyokep.py - képernyőkép egy helyi HTML-ről asztali (1440 px) és valódi mobil (390 px) szélességen,
a gépen lévő Chrome-mal, háttérben. A design-rendszer-referenciabol skill ellenőrző lépéséhez.

  python3 kepernyokep.py elonezet.html [-o kepek/] [--szelesseg 1440 390]
  python3 kepernyokep.py https://pelda.hu -o referenciak/      (a referenciaoldalról is, összevetéshez)
  (a -o nélkül a HTML melletti kepek/ mappába ment; egy projektoldalnál add meg a design-rendszer/kepek mappát)

Kimenet: <név>-1440.jpg és <név>-390.jpg (ha egyben túl nagy, -1, -2 ... darabokban), és a kiírásban
a jobbra kilógó elemek listája, meg hogy betöltődtek-e a betűk. Csak a Python beépített moduljait használja.
A Chrome egy ideiglenes, üres profillal fut, amit a végén letöröl, így semmi nem marad utána.
"""
import argparse
import base64
import json
import os
import re
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

CHROME = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "google-chrome", "chromium", "chromium-browser",
]


def chrome_utvonal():
    for c in CHROME:
        if os.path.isabs(c) and os.path.exists(c):
            return c
        if not os.path.isabs(c) and shutil.which(c):
            return shutil.which(c)
    sys.exit("✗ Nem találom a Google Chrome-ot. Telepítsd, vagy nézd meg az oldalt kézzel a böngészőben.")


class CDP:
    """Minimális Chrome DevTools-kapcsolat websocketen, külső csomag nélkül."""

    def __init__(self, port):
        tabs = None
        for _ in range(60):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2))
                break
            except Exception:
                time.sleep(0.5)
        if not tabs:
            raise RuntimeError("a Chrome nem indult el")
        ws = [t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"]
        path = ws.split(str(port), 1)[1]
        self.s = socket.create_connection(("127.0.0.1", port))
        self.s.settimeout(60)
        kulcs = base64.b64encode(os.urandom(16)).decode()
        self.s.send((f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\nUpgrade: websocket\r\n"
                     f"Connection: Upgrade\r\nSec-WebSocket-Key: {kulcs}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.s.recv(1)
        self.n = 0

    def _rx(self, n):
        d = b""
        while len(d) < n:
            d += self.s.recv(n - len(d))
        return d

    def _recv(self):
        msg = b""
        while True:
            h = self._rx(2)
            ln = h[1] & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._rx(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._rx(8))[0]
            msg += self._rx(ln)
            if h[0] & 0x80:
                return msg

    def call(self, method, **params):
        self.n += 1
        data = json.dumps({"id": self.n, "method": method, "params": params}).encode()
        m = os.urandom(4)
        ln = len(data)
        if ln < 126:
            hdr = bytes([0x81, 0x80 | ln])
        elif ln < 65536:
            hdr = bytes([0x81, 0x80 | 126]) + struct.pack(">H", ln)
        else:
            hdr = bytes([0x81, 0x80 | 127]) + struct.pack(">Q", ln)
        self.s.send(hdr + m + bytes(b ^ m[i % 4] for i, b in enumerate(data)))
        while True:
            r = json.loads(self._recv())
            if r.get("id") == self.n:
                return r.get("result", r)

    def ertek(self, kifejezes):
        return self.call("Runtime.evaluate", expression=kifejezes, returnByValue=True)["result"].get("value")


# kilóg, ha a jobb széle túlmegy a képernyőn, és egyik őse sem vágja le (overflow: hidden/clip)
KILOGOK = ('JSON.stringify([...document.querySelectorAll("body *")].filter(e=>{const r=e.getBoundingClientRect();'
           'if(!(r.width>0&&r.right>%d&&getComputedStyle(e).position!=="fixed"))return false;'
           'for(let p=e.parentElement;p&&p!==document.documentElement;p=p.parentElement){const s=getComputedStyle(p);'
           'if(/hidden|clip|auto|scroll/.test(s.overflowX)&&p.getBoundingClientRect().right<=window.innerWidth+1)return false}'
           'return true}).slice(0,8)'
           '.map(e=>e.tagName.toLowerCase()+(e.className&&typeof e.className==="string"?"."+e.className.split(" ")[0]:"")'
           '+" (jobb széle: "+Math.round(e.getBoundingClientRect().right)+" px)"))')
# felugró ablak, süti-sáv, sötétítő réteg: rögzített vagy ragadós elem, ami a képernyő nagy részét vagy alját takarja
REJT = ('[...document.querySelectorAll("body *")].forEach(e=>{const s=getComputedStyle(e);if(s.position!=="fixed")return;'
        'const r=e.getBoundingClientRect();if(r.width*r.height>innerWidth*innerHeight*0.25||(+s.zIndex>100&&r.top>innerHeight*0.5))'
        'e.style.setProperty("display","none","important")});document.documentElement.style.overflow="visible";'
        'document.body.style.overflow="visible";1')
# szakaszok: legalább 250 px magas, majdnem teljes szélességű blokkok, a legkülső szinten; [y, magasság] párok,
# legfeljebb 14, a 2400 px-nél magasabbak levágva (a kép a felépítést mutassa, nem a teljes hosszt)
SZAKASZOK = ('JSON.stringify((()=>{const W=innerWidth,jo=[...document.querySelectorAll("body *")].filter(e=>{const r=e.getBoundingClientRect();'
             'return r.height>=250&&r.width>=W*0.9&&getComputedStyle(e).position!=="fixed"});'
             # a „burok” (main, wrapper) az, ami az oldal felénél magasabb: azon belül a legkülső blokkok a szakaszok
             'const H=document.documentElement.scrollHeight,jo2=jo.filter(e=>e.getBoundingClientRect().height<H*0.5);'
             'const kulso=jo2.filter(e=>!jo2.some(o=>o!==e&&o.contains(e)));'
             'return kulso.map(e=>{const r=e.getBoundingClientRect();return [Math.round(r.top+scrollY),Math.round(Math.min(r.height,2400))]})'
             '.sort((a,b)=>a[0]-b[0]).filter((v,i,t)=>!i||v[0]>=t[i-1][0]+t[i-1][1]-5).slice(0,14)})())')
# a ténylegesen használt betűcsaládok (címsorok, szöveg, gomb), és amelyik ezek közül nem töltődött be
BETUK = ('JSON.stringify([...new Set([...document.querySelectorAll("h1,h2,h3,p,a,button,li")].map(e=>{const s=getComputedStyle(e);'
         'return s.fontStyle+"|"+s.fontWeight+"|"+s.fontFamily.split(",")[0].replace(/[\\"\']/g,"").trim()}))]'
         '.filter(k=>{const [st,w,f]=k.split("|");return !["serif","sans-serif","system-ui","monospace"].includes(f)'
         '&&!document.fonts.check(st+" "+w+" 16px \\""+f+"\\"")}).map(k=>k.split("|").reverse().join(" ")))')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("-o", default=None, help="kimeneti mappa (alapból a HTML mellett: kepek/)")
    ap.add_argument("--szelesseg", nargs="+", type=int, default=[1440, 390])
    ap.add_argument("--max-kb", type=int, default=400, help="egy kép legfeljebb ekkora legyen, különben darabolja")
    ap.add_argument("--szakaszok", action="store_true", help="asztali nézetben minden nagyobb szakaszt külön képre is ment")
    ap.add_argument("--kiolvas", action="store_true", help="asztali nézetben lefuttatja a references/elemzes.md kiolvasó szkriptjét, "
                    "és a mért betűket, színeket, lekerekítéseket kiolvasas.json-be menti (képet ilyenkor nem készít)")
    a = ap.parse_args()

    webcim = a.html.startswith(("http://", "https://"))  # a referenciaoldal is fotózható
    html = Path(re.sub(r"\W+", "-", a.html.split("//", 1)[1]).strip("-")[:60]) if webcim else Path(a.html).resolve()
    ki = Path(a.o) if a.o else (Path("kepek") if webcim else html.parent / "kepek")
    ki.mkdir(parents=True, exist_ok=True)
    profil = tempfile.mkdtemp(prefix="kepernyokep-")
    port = 9300 + os.getpid() % 500
    p = subprocess.Popen([chrome_utvonal(), "--headless=new", "--hide-scrollbars", "--no-first-run",
                          f"--user-data-dir={profil}", f"--remote-debugging-port={port}", "about:blank"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    try:
        c = CDP(port)
        if a.kiolvas:
            md = (Path(__file__).resolve().parent.parent / "references" / "elemzes.md").read_text(encoding="utf-8")
            js = md.split("```js", 1)[1].split("```", 1)[0]
            c.call("Emulation.setDeviceMetricsOverride", width=1440, height=900, deviceScaleFactor=1, mobile=False)
            c.call("Page.navigate", url=a.html if webcim else html.as_uri())
            time.sleep(6 if webcim else 3)
            c.ertek("document.fonts.ready.then(()=>1)")
            for _ in range(40):
                if c.ertek("(()=>{const y=scrollY;scrollBy(0,700);return scrollY===y})()"):
                    break
                time.sleep(0.35)
            c.ertek("scrollTo(0,0)")
            eredmeny = c.ertek(f"JSON.stringify({js.strip()})")
            f = ki / "kiolvasas.json"
            f.write_text(json.dumps(json.loads(eredmeny or "{}"), ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"✓ {f}")
            print(f.read_text(encoding="utf-8")[:3000])
            return
        for w in a.szelesseg:
            mobil = w < 768
            c.call("Emulation.setDeviceMetricsOverride", width=w, height=900, deviceScaleFactor=1, mobile=mobil)
            c.call("Page.navigate", url=a.html if webcim else html.as_uri())
            time.sleep(6 if webcim else 3)
            c.ertek("document.fonts.ready.then(()=>1)")
            if webcim:
                # idegen oldal: végiggörgetjük (a görgetésre megjelenő és a később betöltődő tartalom miatt),
                # és elrejtjük a felugró ablakokat, süti-sávokat (nagy, rögzített rétegek)
                for _ in range(40):
                    if c.ertek("(()=>{const y=scrollY;scrollBy(0,700);return scrollY===y})()"):
                        break
                    time.sleep(0.35)
                c.ertek("scrollTo(0,0)")
                time.sleep(1)
                c.ertek(REJT)
            h = int(c.ertek("document.documentElement.scrollHeight") or 900)
            sw = int(c.ertek("document.documentElement.scrollWidth") or w)
            kilog = json.loads(c.ertek(KILOGOK % (w + 1)) or "[]")
            nincs_betu = json.loads(c.ertek(BETUK) or "[]")
            if nincs_betu:  # lassú hálózat: még egyszer adunk időt a betűknek
                time.sleep(4)
                nincs_betu = json.loads(c.ertek(BETUK) or "[]")
            szakaszkepek = []
            if a.szakaszok and not mobil:
                # szakaszonként: normál magas nézetben mérjük (a 100vh-s blokkok így valós méretűek), és mindegyiket
                # előbb a képernyőre görgetjük, hogy a görgetésre betöltődő tartalom is látsszon
                c.call("Emulation.setDeviceMetricsOverride", width=w, height=1100, deviceScaleFactor=1, mobile=mobil)
                time.sleep(1)
                for y, hh in json.loads(c.ertek(SZAKASZOK) or "[]"):
                    c.ertek(f"scrollTo(0,{y})")
                    time.sleep(0.9)
                    szakaszkepek.append(base64.b64decode(c.call("Page.captureScreenshot", format="jpeg", quality=70, clip={
                        "x": 0, "y": y, "width": w, "height": min(hh, 1100), "scale": 1})["data"]))
                c.ertek("scrollTo(0,0)")
            c.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=mobil)
            time.sleep(1)
            for reszek in range(1, 8):
                lep = -(-h // reszek)
                darabok = [base64.b64decode(c.call("Page.captureScreenshot", format="jpeg", quality=60, clip={
                    "x": 0, "y": i * lep, "width": w, "height": min(lep, h - i * lep), "scale": 1})["data"])
                    for i in range(reszek)]
                if max(len(d) for d in darabok) <= a.max_kb * 1024:
                    break
            for i, d in enumerate(darabok, 1):
                f = ki / f"{html.stem}-{w}{'' if len(darabok) == 1 else f'-{i}'}.jpg"
                f.write_bytes(d)
                print(f"✓ {f} ({len(d) // 1024} KB)")
            print(f"  {w} px: oldalmagasság {h} px" + (f", VÍZSZINTES GÖRGETÉS: {sw} px széles" if sw > w else ""))
            if kilog and not webcim:  # idegen oldal rejtett menüje nem a mi hibánk
                print(f"  ✗ jobbra kilóg: {', '.join(kilog)}")
            if nincs_betu:
                print(f"  ✗ nem töltődött be: {', '.join(nincs_betu)}")
            for n, d in enumerate(szakaszkepek, 1):
                (ki / f"{html.stem}-szakasz-{n:02d}.jpg").write_bytes(d)
            if szakaszkepek:
                print(f"  {len(szakaszkepek)} szakaszkép: {html.stem}-szakasz-NN.jpg")
    finally:
        p.kill()
        p.wait()
        shutil.rmtree(profil, ignore_errors=True)


if __name__ == "__main__":
    main()
