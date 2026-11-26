#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ellenor.py - a design-rendszer-referenciabol skill segédprogramja. Három parancs:

  python3 ellenor.py fontok "Playfair Display" "DM Sans"
      Megnézi a Google Fontsnál, hogy a betűtípus létezik-e, és tudja-e az ő, ű, Ő, Ű betűt.

  python3 ellenor.py kontraszt DESIGN.md
      A DESIGN.md színpárjait méri (WCAG AA): szöveg a háttereken, szöveg a gombokon és kártyákon,
      a fő szín az alap háttéren. Hibánál 1-es kóddal lép ki.

  python3 ellenor.py css DESIGN.md [-o tokens.css]
      A DESIGN.md értékeiből CSS-változókat ír (--color-primary, --font-h1-size, --rounded-md ...),
      amit az előnézet és a weboldalak betölthetnek.

Csak a Python beépített moduljait használja. A fontok parancshoz internet kell.
"""
import argparse
import re
import struct
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MAGYAR = "őűŐŰ"
GF_CSS = "https://fonts.googleapis.com/css2?"


def gf_letolt(csalad, suly=None, text=None):
    """A Google Fonts egy TTF-jét adja vissza (bájtok). Ha a család nem létezik: LookupError."""
    fam = csalad if suly is None else f"{csalad}:wght@{suly}"
    q = {"family": fam}
    if text:
        q["text"] = text
    try:
        css = urllib.request.urlopen(GF_CSS + urllib.parse.urlencode(q), timeout=20).read().decode()
    except urllib.error.HTTPError as e:
        if e.code == 400:
            raise LookupError(csalad)
        raise
    url = re.search(r"url\((.*?)\)", css)
    if not url:
        raise LookupError(csalad)
    return urllib.request.urlopen(url.group(1), timeout=30).read()


def cmap_karakterek(d):
    """A TTF cmap táblájából a lefedett karakterek (4-es és 12-es formátum)."""
    n = struct.unpack(">H", d[4:6])[0]
    base = None
    for i in range(n):
        tag, _, off, _ = struct.unpack(">4sIII", d[12 + 16 * i:28 + 16 * i])
        if tag == b"cmap":
            base = off
    if base is None:
        return set()
    kar = set()
    for i in range(struct.unpack(">H", d[base + 2:base + 4])[0]):
        _, _, so = struct.unpack(">HHI", d[base + 4 + 8 * i:base + 12 + 8 * i])
        s = base + so
        fmt = struct.unpack(">H", d[s:s + 2])[0]
        if fmt == 4:
            x2 = struct.unpack(">H", d[s + 6:s + 8])[0]
            seg = x2 // 2
            vegek = struct.unpack(">%dH" % seg, d[s + 14:s + 14 + x2])
            kezd = struct.unpack(">%dH" % seg, d[s + 16 + x2:s + 16 + 2 * x2])
            delta = struct.unpack(">%dh" % seg, d[s + 16 + 2 * x2:s + 16 + 3 * x2])
            rp = s + 16 + 3 * x2
            ro = struct.unpack(">%dH" % seg, d[rp:rp + x2])
            for k in range(seg):
                for c in range(kezd[k], vegek[k] + 1):
                    if c == 0xFFFF:
                        continue
                    if ro[k] == 0:
                        g = (c + delta[k]) & 0xFFFF
                    else:
                        p = rp + 2 * k + ro[k] + 2 * (c - kezd[k])
                        g = struct.unpack(">H", d[p:p + 2])[0]
                        g = (g + delta[k]) & 0xFFFF if g else 0
                    if g:
                        kar.add(c)
        elif fmt == 12:
            for k in range(struct.unpack(">I", d[s + 12:s + 16])[0]):
                a, b, g = struct.unpack(">III", d[s + 16 + 12 * k:s + 28 + 12 * k])
                for c in range(a, b + 1):
                    if g + (c - a):
                        kar.add(c)
    return kar




def cmd_fontok(args):
    rossz = 0
    for csalad in args.csaladok:
        try:
            d = gf_letolt(csalad, text=MAGYAR)
        except LookupError:
            print(f"✗ {csalad}: nincs ilyen család a Google Fontsban (pontos név kell, például „Playfair Display”)")
            rossz += 1
            continue
        except Exception as e:  # nincs internet, időtúllépés
            print(f"? {csalad}: nem tudtam ellenőrizni ({e}). Nézd meg kézzel: fonts.google.com, Language: Hungarian")
            rossz += 1
            continue
        hiany = [k for k in MAGYAR if ord(k) not in cmap_karakterek(d)]
        if hiany:
            print(f"✗ {csalad}: hiányzik belőle: {' '.join(hiany)}. Magyar szöveghez nem jó.")
            rossz += 1
            continue
        # a dőlt változat külön fájl: ha a rendszer dőltet használ, annak is tudnia kell az ékezeteket
        try:
            dd = urllib.request.urlopen(GF_CSS + urllib.parse.urlencode(
                {"family": f"{csalad}:ital@1", "text": MAGYAR}), timeout=20).read().decode()
            url = re.search(r"url\((.*?)\)", dd)
            dolt = url and all(ord(k) in cmap_karakterek(urllib.request.urlopen(url.group(1), timeout=30).read())
                               for k in MAGYAR)
            dolt_szoveg = "a dőlt változata is" if dolt else "dőlt változata nincs (a böngésző ferdítené: dőlt kiemelésre ne ezt használd)"
        except Exception:
            dolt_szoveg = "dőlt változata nincs (a böngésző ferdítené: dőlt kiemelésre ne ezt használd)"
        print(f"✓ {csalad}: létezik, és tudja az ő, ű betűt; {dolt_szoveg}")
    sys.exit(1 if rossz else 0)


# ---------------------------------------------------------------- a DESIGN.md beolvasása

def _ertek(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _flow(s):
    """Egyszerű YAML flow-map: { a: 1, b: "x, y" } -> dict (idézőjelen belüli vesszőt kezel)."""
    belso = s.strip()[1:-1]
    darabok, cur, q = [], "", None
    for ch in belso:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            darabok.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        darabok.append(cur)
    out = {}
    for d in darabok:
        if ":" in d:
            k, v = d.split(":", 1)
            out[k.strip()] = _ertek(v)
    return out


def megjegyzes_nelkul(sor):
    """A sor végi YAML-megjegyzés (szóköz utáni #) levágása; az idézőjelen belüli # (hexkód) marad."""
    q = None
    for i, ch in enumerate(sor):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "#" and (i == 0 or sor[i - 1] in " \t"):
            return sor[:i].rstrip()
    return sor


def yaml_beolvas(szoveg):
    """A DESIGN.md YAML-blokkjai (fejléc és ```yaml blokkok) egy fába. Csak térképeket és egyszerű értékeket
    kezel (a design-tokenekhez ennyi kell); listát (például omitted) kihagy."""
    blokkok = []
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", szoveg, re.S)
    if m:
        blokkok.append(m.group(1))
    blokkok += re.findall(r"```ya?ml\s*\n(.*?)```", szoveg, re.S)
    fa = {}
    for blokk in blokkok:
        verem = [(-1, fa)]
        for sor in blokk.splitlines():
            if not sor.strip() or sor.lstrip().startswith(("#", "-")):
                continue
            beh = len(sor) - len(sor.lstrip())
            tartalom = megjegyzes_nelkul(sor.strip())
            if ":" not in tartalom:
                continue
            k, v = tartalom.split(":", 1)
            k, v = k.strip(), v.strip()
            while verem[-1][0] >= beh:
                verem.pop()
            szulo = verem[-1][1]
            if v == "":
                szulo[k] = {}
                verem.append((beh, szulo[k]))
            elif v.startswith("{") and v.endswith("}"):
                szulo[k] = _flow(v)
            else:
                szulo[k] = _ertek(v)
    return fa


def lapit(d, elo=""):
    out = {}
    for k, v in d.items():
        ut = f"{elo}.{k}" if elo else k
        if isinstance(v, dict):
            out.update(lapit(v, ut))
        else:
            out[ut] = v
    return out


def felold(ertek, lapos, mely=0):
    m = re.fullmatch(r"\{([\w.\-]+)\}", str(ertek).strip())
    if m and mely < 10:
        return felold(lapos.get(m.group(1), ertek), lapos, mely + 1)
    return ertek


# ---------------------------------------------------------------- kontraszt

def hex_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) == 8:
        h = h[:6]
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def fenyesseg(rgb):
    def csat(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (csat(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def arany(a, b):
    la, lb = sorted((fenyesseg(hex_rgb(a)), fenyesseg(hex_rgb(b))), reverse=True)
    return (la + 0.05) / (lb + 0.05)


SZOVEG = re.compile(r"^(ink|text|on-surface|foreground|body)")
HATTER = re.compile(r"^(neutral|surface|background|paper|base)")


def cmd_kontraszt(args):
    fa = yaml_beolvas(Path(args.fajl).read_text(encoding="utf-8"))
    lapos = lapit(fa)
    szinek = {k: v for k, v in lapit(fa.get("colors", {})).items() if str(v).startswith("#")}
    if not szinek:
        print("✗ Nem találok hexkódos színt a colors alatt.")
        sys.exit(1)
    parok = []  # (előtér, háttér, minimum, leírás)
    for k in szinek:
        if k.startswith("on-"):
            alap = k[3:]
            if alap not in szinek:  # on-night-muted -> night
                alap = re.sub(r"-(muted|soft|subtle|light|dim)$", "", alap)
            if alap in szinek:
                parok.append((k, alap, 4.5, f"{k} a {alap} színen"))
    szovegek = [k for k in szinek if SZOVEG.match(k.split(".")[-1])]
    # ha egy háttérnek saját on- párja van (például sötét felület), azon nem az általános szöveget mérjük
    hatterek = [k for k in szinek if HATTER.match(k.split(".")[-1]) and f"on-{k}" not in szinek]
    for s in szovegek:
        minimum = 3.0 if any(x in s for x in ("line", "border", "subtle")) else 4.5
        for h in hatterek:
            parok.append((s, h, minimum, f"{s} szöveg a {h} háttéren"))
    # a fő szín a világos háttereken. Sötét szakaszon a kiemelés színét a képen kell megnézni (a szkript nem tudja,
    # hogy ott a fő szín vagy egy világosabb változat áll); a secondary sokszor felületszín, ezért azt sem méri.
    if "primary" in szinek:
        for h in hatterek:
            parok.append(("primary", h, 3.0, f"a fő szín (gomb, kiemelés) elválik a {h} háttértől"))
    for nev, komp in (fa.get("components") or {}).items():
        if isinstance(komp, dict) and "backgroundColor" in komp and "textColor" in komp:
            parok.append((komp["textColor"], komp["backgroundColor"], 4.5, f"{nev}: szöveg a saját hátterén"))
    rossz = 0
    for elo, hat, minimum, leiras in parok:
        e = felold(szinek.get(elo, elo), lapos)
        h = felold(szinek.get(hat, hat), lapos)
        try:
            r = arany(str(e), str(h))
        except ValueError:
            print(f"? {leiras}: nem hexkód ({e} / {h}), kihagyva")
            continue
        jo = r >= minimum
        rossz += not jo
        print(f"{'✓' if jo else '✗'} {r:4.1f}:1 (kell {minimum}:1)  {leiras}  [{e} / {h}]")
    print("\nMinden pár rendben." if not rossz else f"\n{rossz} pár nem éri el a minimumot: ezeket javítsd.")
    sys.exit(1 if rossz else 0)


# ---------------------------------------------------------------- CSS-változók

def css_nev(ut):
    return re.sub(r"[^a-z0-9\-]", "-", ut.lower().replace(".", "-"))


def cmd_css(args):
    fa = yaml_beolvas(Path(args.fajl).read_text(encoding="utf-8"))
    lapos = lapit(fa)
    sorok = [":root {"]
    for k, v in lapit(fa.get("colors", {})).items():
        sorok.append(f"  --color-{css_nev(k)}: {felold(v, lapos)};")
    for k, v in (fa.get("typography") or {}).items():
        if not isinstance(v, dict):
            continue
        n = css_nev(k)
        if "fontFamily" in v:
            # ha a DESIGN.md tartalékbetűt is ad („Newsreader, Georgia, serif”), úgy marad; ha nem, általános tartalék jön mögé
            csal = [x.strip().strip("\"'") for x in v["fontFamily"].split(",")]
            if len(csal) == 1:
                print(f"! {k}: nincs tartalékbetű a fontFamily-ben (például „{csal[0]}, Georgia, serif”)", file=sys.stderr)
            sorok.append(f"  --font-{n}-family: \"{csal[0]}\"{''.join(', ' + x for x in csal[1:])};")
        for kulcs, css in (("fontSize", "size"), ("fontWeight", "weight"), ("lineHeight", "line-height"),
                           ("letterSpacing", "letter-spacing")):
            if kulcs in v:
                sorok.append(f"  --font-{n}-{css}: {v[kulcs]};")
    for csop, elo in (("rounded", "rounded"), ("spacing", "space")):
        for k, v in lapit(fa.get(csop, {})).items():
            sorok.append(f"  --{elo}-{css_nev(k)}: {v};")
    for k, v in (fa.get("motion") or {}).items():
        if isinstance(v, dict):
            sorok.append(f"  --motion-{css_nev(k)}: {v.get('duration', '200ms')} {v.get('timingFunction', 'ease')};")
    for nev, komp in (fa.get("components") or {}).items():
        if not isinstance(komp, dict):
            continue
        for k, v in komp.items():
            if k == "typography":
                continue
            tul = css_nev(re.sub(r"([A-Z])", r"-\1", k))
            sorok.append(f"  --{css_nev(nev)}-{tul}: {felold(v, lapos)};")
    sorok.append("}")
    # Google Fonts betöltése: minden család, ami a typography alatt szerepel, normál és dőlt, a használt súlyokkal
    csaladok = {}
    for v in (fa.get("typography") or {}).values():
        if isinstance(v, dict) and v.get("fontFamily"):
            nev = v["fontFamily"].split(",")[0].strip().strip("\"'")
            csaladok.setdefault(nev, set()).add(str(v.get("fontWeight", "400")))
    if csaladok:
        resz = []
        for nev, sulyok in csaladok.items():
            s = sorted(sulyok | {"400"}, key=int)
            dolttel = ("family=" + urllib.parse.quote_plus(nev) + ":ital,wght@"
                       + ";".join([f"0,{x}" for x in s] + [f"1,{x}" for x in s]))
            try:  # ha a családnak nincs dőltje, a Google 400-as hibát ad: akkor dőlt nélkül kérjük
                urllib.request.urlopen(GF_CSS + dolttel, timeout=15).read()
                resz.append(dolttel)
            except Exception:
                resz.append("family=" + urllib.parse.quote_plus(nev) + ":wght@" + ";".join(s))
        sorok.insert(0, f"@import url(\"https://fonts.googleapis.com/css2?{'&'.join(resz)}&display=swap\");\n")
    ki = "\n".join(sorok) + "\n"
    if args.o:
        Path(args.o).write_text(ki, encoding="utf-8")
        print(f"✓ {args.o}: {len(sorok) - 2} változó")
    else:
        print(ki, end="")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    al = ap.add_subparsers(dest="parancs", required=True)
    p = al.add_parser("fontok", help="Google Fonts: létezik-e, tudja-e az ő, ű betűt")
    p.add_argument("csaladok", nargs="+")
    p.set_defaults(f=cmd_fontok)
    p = al.add_parser("kontraszt", help="a DESIGN.md színpárjainak olvashatósága")
    p.add_argument("fajl")
    p.set_defaults(f=cmd_kontraszt)
    p = al.add_parser("css", help="CSS-változók a DESIGN.md értékeiből")
    p.add_argument("fajl")
    p.add_argument("-o")
    p.set_defaults(f=cmd_css)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
