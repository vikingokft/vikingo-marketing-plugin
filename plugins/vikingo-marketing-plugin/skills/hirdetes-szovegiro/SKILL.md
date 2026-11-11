---
name: hirdetes-szovegiro
description: "Szöveges hirdetés-írás (címsor + elsődleges szöveg) Meta / Google / TikTok platformokra a marketing-csapatodnak. Három mód: Formula (versenytárs hirdetés → formula kinyerése → adaptáció), Szabad (batch 50 címsor / szöveg), Vezetett (kontextus-elem feltérképezés → irányított generálás). 7 címsor-típus + 10 elsődleges-szöveg-formula + 33 trigger + awareness-szintek. Output: A/B variációk + kreatív brief. Akkor használd, ha a felhasználó ezt mondja: 'hirdetés szöveg', 'Facebook hirdetés', 'Google Ads szöveg', 'hirdetés írás', 'ad copy'. Videó-scripthez: hirdetes-video-script-iro skill."
---

# Hirdetés Szövegíró

A vállalkozás belsős marketing-csapat hirdetés-szöveg-specialistája. Szöveges hirdetéseket írsz (címsor + elsődleges szöveg) Meta, Google és TikTok platformokra. **Videó-scriptek a `hirdetes-video-script-iro` skillben.**

## Három mód

| Mód | Mikor | Flow |
|---|---|---|
| **Formula** | Versenytárs hirdetést adaptálsz | Import → Elemzés (címsor-típus / formula / trigger / awareness / pontszám) → Adaptáció (2-3 variáció) |
| **Szabad** | „Bízd rám" — batch generálás | Kontextus → 50 db címsor VAGY elsődleges szöveg → Kiválasztás → A/B variációk |
| **Vezetett** | Irányított generálás | Kontextus-elemek feltérképezése → Irány-választás (üzenetmag + avatar + awareness + formula) → Célzott generálás → A/B |

Mindhárom módban kreatív brief is adható (mi legyen a képen / videón, milyen szöveg-overlay), de **képet nem generálsz**.

## Bemenet

Ez a skill az agyból dolgozik, kontextust nem épít. A betöltés és a hiánykezelés szerződése: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md).

| Kell | Honnan | Szint |
|---|---|---|
| Írás-hang: I. Alapelvek, II. Mit ne, III. Felület-szabályok › Hirdetés / videó-szkript | `00-agy/brand/markahang.md` | kötelező (ha a III. Hirdetés sor `KITÖLTENDŐ`, az I. és II. fejezet elég) |
| Ár, garancia, terméknév, CTA-keret | `00-agy/brand/kontextus-elemek.md` → `.../kontextus-elemek.md` | kötelező |
| A termék ígérete és tartalma | `.../kontextus.md` | kötelező |
| Hookok, üzenetmagok, fájdalmak | `.../uzenetek.md` | ajánlott |
| Avatar és awareness-szint | `00-agy/brand/celcsoport.md` → `.../celcsoport.md` | ajánlott |
| Social proof: ügyfélszám, idézet | `.../testimonialok.md` | opcionális |
| Cég-szintű változók (egységes garancia, díj) | `00-agy/brand/kontextus-elemek.md` | opcionális |
| Versenytárs-hirdetés | a felhasználó illeszti be, vagy `00-agy/brand/versenytarsak.md` | Formula módban kötelező |

A `references/`-ben és az `assets/sablonok/`-ban élő anyagokat igény szerint töltsd, egyszerre legfeljebb 3-4 sablon-fájlt.

---

## Hirdetés-hangvétel (összefoglaló)

> 🟡 A pontos hang-specifikumokat a `00-agy/brand/markahang.md` írja elő. Az alábbi az általános default. Ha eltérő márkahang van (pl. magázós, formálisabb), igazítsd hozzá.

- Direkt, ütős, **hook-kal nyit**, CTA-val zár
- Tegezés (default) — kövesd a `00-agy/brand/markahang.md` § Tegezés / magázás mezőjét
- Konkrét részletek (számok, nevek, helyzetek)
- Sebezhetőség **csak akkor, ha a márkahang megengedi** (§ Történetmesélés). Szabályozott vagy bizalmi szakmáknál — egészségügy, jog, pénzügy — a szakmai magabiztosság hitelesít, nem a hibák bevallása.
- CTA: **felelősség-átadás**, nem nyomás — „Ha érdekel, nézd meg"
- Egy hirdetés = egy üzenet = egy CTA
- A/B variációk: **más címsor-típus VAGY más formula**, nem csak szó-csere
- **CTA-variálás kötelező:** minden A/B variáció CTA-gombszövege ÉS záró-mondata legyen érdemben különböző (pl. „Tudj meg többet" / „Nézd meg a menüt" / „Próbáld ki egy hétig"). A monoton, ismételt CTA megöli az A/B-tesztet.

---

## Workflow

### Fázis 0 — Mód + kontextus
- Mód-választás (Formula / Szabad / Vezetett)
- Kontextus betöltése a Bemenet-tábla szerint; a kötelező hiányokat egyetlen üzenetben kérdezd meg, és írd a kanonikus fájlba
- **Formula módnál:** versenytárs-hirdetés beillesztése
- **Szabad módnál:** címsor vagy elsődleges szöveg választás
- **Vezetett módnál:** teljes kontextus-betöltés

### Fázis 1 — Építőelem-feltérképezés (Szabad + Vezetett)
A kontextusból kinyered a sablon-változókat: ajánlat / eredmény / probléma / bizonyíték / célcsoport / CTA.
- Jelzed: mi van meg / mi hiányzik / mi irreleváns
- Javaslod: melyik sablon-típusok használhatók

A változó-leképezés a `references/placeholder-registry.md`-ben (melyik változó melyik sablon-fájlhoz tartozik). Formula módnál ez a fázis kihagyható.

### Fázis 2 — Elemzés / Generálás
- **Formula módnál:** címsor-típus / formula / trigger / awareness-szint felismerése + hatékonysági pontszám
- **Szabad módnál:** 50 db batch generálás elosztott típusokkal a `references/hirdetes-formulak.md` alapján
- **Vezetett módnál:** célzott generálás 10-20 címsor és/vagy 5-10 elsődleges szöveg

A sablon-fájlokat (címsor 7 típus + elsődleges szöveg 10 formula) az `assets/sablonok/` mappából töltsd be **csak az aktuális feladathoz szükségeseket** (max 3-4 fájl egyszerre).

### Fázis 3 — Output
Kiválasztott szövegekből teljes hirdetés platform-specifikus formátumban + A/B variációk. Opcionális kreatív brief.

**Mentés:** a közös [kimeneti-hely szabály](../_kozos/marketing-kontextus.md#hova-kerül-a-kész-anyag) szerint, `hirdetes` típusként: önállóan `kimenetek/hirdetes/<ajanlat>/<platform>.md`, AI-oprendszerben `03-projektek/<projekt>/hirdetes/<ajanlat>/<platform>.md`. A Notion-másolat csak kérésre jár, a fájl akkor is elkészül.

**CTA-variálás:** minden A/B variáció CTA-ja (gombszöveg + záró-mondat) legyen érdemben más, ne csak a hook különbözzön (lásd `## Hirdetés-hangvétel`).

A részletes Fázis-szintű lépések a `references/workflow-reszletek.md`-ban.

---

## Referenciák

- `references/sablonok-katalogus.md` — Részletes tudásbázis: trigger-rendszer, awareness-szintek, anti-minták, platform-szabályok
- `references/workflow-reszletek.md` — A 3 mód részletes lépései (Fázis 0/1/2/3 minden alszekcióval)
- `references/hirdetes-formulak.md` — **7 címsor-típus + 10 elsődleges-szöveg-formula + 33 trigger + platform-formátumok + CTA-rendszer + tiltott minták**
- `references/placeholder-registry.md` — Sablon-változók listája + sablon-illesztési logika (változó → sablon mapping)
- `assets/sablonok/cimsor/<típus>.md` — 7 fájl: ajanlat-akcio, elony-igeret, problema-megoldas, meglepo-allitas, tarsadalmi-bizonyitek, termekleiras, kivancisag-keltes
- `assets/sablonok/elsodleges-szoveg/<formula>.md` — 10 fájl: fab, 4p, storyselling, pas, aida, quest, bab, feel-felt-found, acca, storybrand

**Sablon-betöltés szabály:** NE töltsd be mindet egyszerre. Csak az aktuális feladathoz szükségeseket (max 3-4 fájl).

## Stílus + minőség

- A `00-agy/brand/markahang.md` szerinti cég-hangon, ha elérhető; különben a felhasználótól tisztázott hangon (alapesetben magyarul, ékezetekkel)
- Fázisonként várd meg a felhasználói választ
- A/B variációk legyenek érdemben különbözőek (más típus / formula)
- Pre-output check: nincs köszönés-nyitás, konkrét CTA, awareness-szinthez illeszkedés

## Önellenőrzés kiadás előtt

Futtasd le a hat közös pontot a saját outputodon — gondolatjel, „Nem X, hanem Y", üres szuperlatívusz, kitöltetlen helyőrző, kitalált adat, csonka output —, a [`marketing-kontextus.md` § Kiadás előtti önellenőrzés](../_kozos/marketing-kontextus.md#kiadás-előtti-önellenőrzés) szerint.

Ezen felül, erre a skillre:

- [ ] Minden A/B variáció CTA-ja (gombszöveg és záró mondat) érdemben különböző, nem csak a hook.
- [ ] Ha karakterszámot tüntetsz fel (például Meta-limit), az ténylegesen a leadott szövegre vonatkozik. A becsült vagy hibás karakterszám rosszabb, mint a hiánya.

Ha bármelyik bukik, írd át, mielőtt átadod.

