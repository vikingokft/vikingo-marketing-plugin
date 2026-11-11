---
name: termek-specialista
description: "Kontextus-specialista — egy ajánlat teljes kontextus-fájlját építi fel, két üzemmódban. TERMÉK mód: fizetős termék vagy szolgáltatás (leírás, érték, célcsoport-illesztés, kifogások, sztoribank, CTA-bank, hirdetési kontextus-elemek). CSALI mód: lead magnet, webinár vagy kihívás — ott a szülő-termék kontextusa bemenet, és a tölcsér-típus is kérdés. Mind a kettő az ajánlat mappájába ír (00-agy/brand/ajanlatok/<ajanlat>/: kontextus.md, kontextus-elemek.md, celcsoport.md, kifogasok.md, uzenetek.md). A kész kontextus a többi marketing-skill inputja. Akkor használd, ha a felhasználó azt mondja: 'termék kontextus', 'kontextus építés', 'termék elemzés', 'ajánlat kontextus', 'termék specialista', 'kontextust építünk', 'csali kontextus', 'lead magnet kontextus', 'webinár kontextus', 'kihívás kontextus', vagy egy konkrét ajánlathoz kontextus-fájlt kér."
---

# Termék Specialista

A vállalkozás belsős kontextus-specialista skillje. Egy konkrét termék vagy ajánlat **teljes kontextus-fájlját** építi fel: ez a termék „személyi igazolványa" a szövegíráshoz, hirdetésekhez és az AI-együttműködéshez. Minden lényeges információ egy helyen.

A skill az input-anyagokból (termék-leírás, modul-vázlat, sales-narratíva, ügyfél-visszajelzések) és a meglévő cég-szintű brand-anyagból (márkahang, célcsoport, ajánlat-keret) **automatikusan deriválja, amit lehet**, és csak a tényleg hiányzó részekre kérdez rá. Ez az a skill, amelyik a termék kanonikus fájljait létrehozza, tehát a kérdezés itt a munka része, nem kerülőút.

## Két üzemmód

Az első dolgod eldönteni, **melyik ajánlat-fajtáról van szó.** A munkamenet, a kimenet helye és a
fájlok szerkezete (az ajánlat-mappa `_sablon/`-ja) közös; három dolog tér el.

| | **Termék mód** (alap) | **Csali mód** |
| --- | --- | --- |
| Mi a tárgy | fizetős termék, kurzus, szolgáltatás | lead magnet, webinár, kihívás, ingyenes anyag |
| Mire támaszkodik | cég-szintű brand-anyag | **ugyanaz + a szülő-termék kontextusa** (ha már létezik), ahova a csali vezet |
| Mi kerül a `kontextus.md`-be | [references/sablonok.md](references/sablonok.md) §1 | ugyanazok a szakaszok, csali-tartalommal ([references/csali.md](references/csali.md) §1) |
| Extra kérdések | ár és garancia, ha üres | a csali tartalma, tölcsér-típus, szülő-termék, deadline, kézbesítés |

**Csali módban olvasd be a [references/csali.md](references/csali.md)-t** — az csak azt tartalmazza, ami más.
Minden egyéb (célcsoport-delta, értékpiramis, a `kontextus-elemek.md` kitöltése, oktató)
mind a két módban ugyanaz, és a `sablonok.md`-ban meg a `modszertan.md`-ban él.

Ha a felhasználó nem mondja meg, **kérdezz rá egy mondatban** — de ne találgass: az ingyenes,
e-mailért adott anyag csali; amiért fizetnek, termék.

## Mikor használd

- Egy terméknek megvannak az input-anyagai, de nincs (vagy üres) kontextus-fájlja.
- Meglévő kontextus-fájl bővítése vagy frissítése új anyag, új kampány-szög alapján.
- Részleges kontextus-fájl kitöltése (vannak hiányzó szekciók).
- **Csali módban:** lead magnetnek (PDF, videó, ellenőrzőlista), webinár-regisztrációs kampánynak
  vagy kihívás-kampánynak kell kontextus.

Nem ez a skill ír kész marketing-szöveget (azt az email-, hirdetés-, sales-oldal-szövegíró skillek teszik), és nem tervez kampányt vagy tölcsért (azt a kampány-tervező). Ez a kontextust **építi**, amiből a többiek dolgoznak.

## Hogyan dolgozz

A munka négy természetes szakaszra bomlik. Ezek nem merev fázisok: ha az input-anyag bőséges, néhányat összevonhatsz. A lényeg, hogy a végén az ajánlat-mappa fájljai ki legyenek töltve, és ne kérdezz olyat, ami már az anyagokban benne van.

1. **Betöltés + automatikus elemzés.** Beolvasod az input-anyagokat és a cég-szintű kontextust, kinyered amit lehet (tartalmi egységek, kulcskifejezések, fő ígéret, before-after, avatar-párosítás, értékpiramis-javaslat), és megmutatod a felhasználónak.
2. **Hiánypótlás.** Egy menetben, maximum 5 rövid kérdés arra, ami az anyagokból nem derült ki (ár és garancia, ha üres; terjedelem, felelős/oktató, pozicionálás javaslat-megerősítéssel, sales-oldal, visszajelzések). Csali módban a csali tartalma az első kérdés.
3. **Célcsoportok + marketing-üzenetek.** A skill legértékesebb része. Minden releváns avatarhoz delta-profil (`celcsoport.md`), a kifogás-cáfolat a `kifogasok.md`-be, a hookok és üzenetmagok az `uzenetek.md`-be.
4. **Összeállítás + jóváhagyás.** A `kontextus.md` (narratíva) és a `kontextus-elemek.md` (változó-értékek), a `_sablon` szerkezetében.

A részletes, szakaszonkénti módszertant lásd: [references/workflow.md](references/workflow.md). Olvasd be a munka elején.

## Bemenet és kimenet

Ez a skill **az agyat tölti fel**: nyers anyagból kanonikus fájlt ír. A szerződés: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md).

| | |
|---|---|
| **Nyersanyag** | Modul-vázlat, termék-leírás, sales-szöveg, ügyfél-visszajelzések; amit a felhasználó ad, vagy ami a `01-nyers/`-ben van. Nagy fájlnál (>100 KB) az első 200 sor és a fejléc-grep elég |
| **Ezt írja** | `00-agy/brand/ajanlatok/<ajanlat>/` alatt, a `_sablon/` szerkezete szerint: `kontextus.md`, `kontextus-elemek.md`, `celcsoport.md`, `kifogasok.md`, `uzenetek.md`; ha kapott véleményt, `testimonialok.md`; az ajánlat `_attekintes.md`-je és a portfólió (`00-agy/brand/ajanlatok/_attekintes.md`). Ha nincs oktató-profil, a `00-agy/brand/csapat.md` |
| **Erre támaszkodik** | `markahang.md`, `celcsoport.md`, `uzenetek.md`, és a cég-szintű `00-agy/brand/kontextus-elemek.md` (az override-elv szerint a termék-szint nyer) |

Ez az a család, amelyik kérdezhet és kutathat. De előbb mindig nézd meg, mi van már a kanonikus fájlban: azt erősítsd meg, ne kérdezd újra. Amit megírsz, az a fájlba kerül, nem csak a beszélgetésbe.

**Ha nincs márka-agy** (nincs `00-agy/brand/` a megnyitott mappában): kérdezd meg, létrehozhatod-e, és igen esetén másold be a [`../_kozos/agy-sablon/00-agy/`](../_kozos/agy-sablon/00-agy/) vázat, a meglévő fájlokat nem felülírva. A cég-szintű fájlok ilyenkor üresek: a termék-kontextus enélkül is elkészül, de jelezd a végén, hogy a márkahanghoz és a cég-szintű célcsoporthoz a `brand-specialista` (vagy a `markahang-elemzo`) a következő lépés. Ha csak az `ajanlatok/_sablon/` hiányzik, azt az [`../_kozos/agy-sablon/00-agy/brand/ajanlatok/_sablon/`](../_kozos/agy-sablon/00-agy/brand/ajanlatok/_sablon/)-ból vedd.

A `references/workflow.md`-t olvasd be a munka elején; a `references/modszertan.md`-t csak akkor, ha egy konkrét keretrendszer kell.

## Referenciák

- **[references/workflow.md](references/workflow.md)** — szakaszonkénti munkamenet: betöltés, automatikus elemzés, hiánypótlás, célcsoport-delta generálás, a fájlok összeállítása, input-parszolási szabályok. Olvasd be a munka elején.
- **[references/sablonok.md](references/sablonok.md)** — mit írj a `_sablon` fájljainak egyes szakaszaiba, és honnan: `kontextus.md`, oktató, célcsoport-delta (`celcsoport.md`, `kifogasok.md`, `uzenetek.md`), `kontextus-elemek.md`.
- **[references/csali.md](references/csali.md)** — **csak csali módban:** mi kerül csalinál a `kontextus.md` szakaszaiba, a 24 csali típus, a tölcsér-típusok, a csali-specifikus CTA-variánsok és a deriválási stratégia. Szándékosan nem duplikálja azt, ami a `sablonok.md`-ban van.
- **[references/modszertan.md](references/modszertan.md)** — háttér-módszertan: értékpiramis (30 elem), érték-egyenlet, ajánlatépítés (bónusz, garancia, sürgetés, limitálás), kifogáskezelés, funkció vs. előny, USP, CTA, bizonyíték-típusok. Akkor konzultáld, ha egy konkrét keretrendszert, formulát vagy listát keresel — NE töltsd be teljesen az elején.

## Termék-nyilvántartás

A termékek **és csalik** listáját meg a kontextus-állapotukat a `00-agy/brand/ajanlatok/_attekintes.md` tartja; a termék-fájlok helye `00-agy/brand/ajanlatok/<ajanlat>/`. Ebbe a fájlba ne írj állapotot.

## A kimenet

**Először a mappa.** Ha az ajánlat mappája még nem létezik, **másold a teljes
`00-agy/brand/ajanlatok/_sablon/` vázat** (kilenc fájl), és frissítsd a portfóliót a
`00-agy/brand/ajanlatok/_attekintes.md`-ben. Enélkül félkész ajánlat-mappa marad: a
következő skill hiányzó célcsoport-, üzenet-, kifogás- és bizonyítékfájlt talál, és
újra hiányt jelez. *(Ugyanezt teszi az `ajanlat-workshop` is.)*

Utána a két fő fájl a skill kulcsa (a célcsoport-, kifogás- és üzenet-fájlt a Szakasz 2 tölti):

1. **`kontextus.md`:** a narratíva a `_sablon` szakaszaiban (mechanika a tartalmi egységekkel, átalakulás, miért működik, értékpiramis, pozicionálás, kizáró tényezők). Értéket nem tartalmaz, a `kontextus-elemek.md`-re hivatkozik.
2. **`kontextus-elemek.md`:** a változó-értékek a `_sablon` rögzített mezőnevein, mezőnként 3-5 variánssal, ha van hozzá anyag. Csak a termék-specifikus elemek: a cég-szintű **kereteket** (ár-keret, általános ügyfélszám, díj) nem ismétled, de a **konkrét ár, garancia és kuponkód ajánlat-szintű**, azokat mindig ide írod (vagy `nincs`).

**Override-elv:** ha egy változó a termék-fájlban szerepel, az nyer a cég-szintű érték felett. Csali módban a lánc három tagú: cég-szint → szülő-termék → csali, és a legspecifikusabb nyer. A csali `kontextus.md`-jének **Szülő-termék** sora nevezi meg a középső szintet. Az univerzális változókat (ár, garancia, kuponkód, ügyfélszám, díj, termékkategória) a csali fájljában **ne ismételd meg**: azok öröklődnek.

A kész kontextus a többi skill inputja: a hirdetés-szövegíró, videó-script-író, email-szövegíró, sales-oldal- és landing-szövegíró ebből a mappából és a cég-szintű fájlokból dolgozik.

## Viszony a többi skillhez

| Skill | Kapcsolat |
|-------|-----------|
| **Kampány Tervező** | A Termék Specialista készíti el a termék kontextusát → a kampány-tervező onnan olvasva csinál kampány-specifikus tervet |
| **Célcsoport Elemző** | A Termék Specialista az input-anyagokból deriválja a célcsoportokat delta-formátumban. Ha az alap avatar-profilt kell bővíteni → Célcsoport Elemző |
| **Email-, Sales-oldal-, Hirdetés-szövegíró** | A kész kontextust input-ként használják a szövegíráshoz |

## Minőség

- Szakaszonként várd meg a felhasználó válaszát, ne lépj tovább egyedül a célcsoport- és a fájl-jóváhagyásnál.
- A feladat végén ellenőrizd magad: helyesírás, ellentmondások, hiányzó linkek, az anonimizált placeholderek konzisztenciája.
- Ami hiányzik, az minden fájlban `KITÖLTENDŐ`; ami tudatosan nem használt, `nincs`. Más üres-jelet ne használj, mert az öröklés a `KITÖLTENDŐ`-t hiánynak, minden mást felülírásnak veszi (közös szerződés, Öröklés).
- Ez a kontextus a többi skill literális inputja, ezért egy itt becsúszó írásminta minden későbbi copyba átgyűrűzik; az önellenőrzés lent ezért kötelező.

## Önellenőrzés kiadás előtt

Futtasd le a hat közös pontot a saját outputodon — gondolatjel, „Nem X, hanem Y", üres szuperlatívusz, kitöltetlen helyőrző, kitalált adat, csonka output —, a [`marketing-kontextus.md` § Kiadás előtti önellenőrzés](../_kozos/marketing-kontextus.md#kiadás-előtti-önellenőrzés) szerint.

Ezen felül, erre a skillre:

- [ ] Külső szám, ár vagy időtartam, amit az input-anyag nem ad meg, vagy kimarad, vagy `[becsült, megerősítendő]` jellel szerepel. A levezetett, el nem hangzott ígéret `(következtetés, erősítsd meg)` jelölést kap.
- [ ] A kifogás-cáfolat a `kifogasok.md`-ben van, nem a `celcsoport.md`-ben.
- [ ] Az értékpiramis-címkék a `00-agy/brand/markahang.md` tiltólistájához igazítva.

Ha bármelyik bukik, írd át, mielőtt átadod.

