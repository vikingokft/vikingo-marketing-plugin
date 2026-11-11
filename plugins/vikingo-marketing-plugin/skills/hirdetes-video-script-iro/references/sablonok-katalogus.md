# Hirdetés Videó Script Író — Sablon-katalógus + szabályok

A 15 sablon-kategória áttekintése, script-struktúra szabályok, CTA-rendszer, videó-hosszak, szerkesztési minták és minőségi referenciák.

> 207 sablon 15 kategóriában. A részletes sablonok: `assets/sablonok/[kategoria].md`

## Tartalomjegyzék

1. [15 sablon-kategória — áttekintés](#1-15-sablon-kategória--áttekintés)
2. [Kategória-relevancia — termék-mátrix](#2-kategória-relevancia--termék-mátrix)
3. [2A. Termék típus profilok](#2a-termék-típus-profilok)
4. [2B. Wave-besorolási kritériumok](#2b-wave-besorolási-kritériumok)
5. [Script-struktúra (Hook / Body / CTA)](#3-script-struktúra)
6. [Videó-hosszak](#4-videó-hosszak)
7. [Szerkesztési minták](#5-szerkesztési-minták)
8. [Tiltott szavak és minták](#6-tiltott-szavak-és-minták)
9. [Script példa (kommentálva)](#7-script-példa-kommentálva)
10. [Mentális kapcsolók](#8-mentális-kapcsolók)

---

## 1. 15 sablon-kategória — áttekintés

> 🟡 A „példa hook" sorok placeholderesek. Saját termékre adaptáld a hook-ot; a kategória-leírás és az építőelem-lista általános.

### 1.1 Testimonial & Szociális Bizonyíték (20 sablon)

**Fájl:** `assets/sablonok/testimonial.md` (VS-001..020)
**Mikor:** Van ügyfél-vélemény, vevő-szám, visszajelzés, vagy híres személy hivatkozás.
**Építőelemek:** testimonial idézet, ügyfél neve, eredmény, ügyfél-szám, szakértő háttér
**🟡 Példa hook:** „Több, mint [ügyfélszám] embert tanítottam / segítettem [téma]-ban. A legtöbbjük pár [időegység] alatt igazi haladást ért el."
**Ajánlott:** kurzus / szolgáltatás / SaaS

### 1.2 Termék Demo & Bemutató (20 sablon)

**Fájl:** `assets/sablonok/termek-demo.md` (VS-021..040)
**Mikor:** Konkrét feature-t, funkciót, vagy eszközt akarsz bemutatni. Képernyőfelvétellel kombinálható.
**Építőelemek:** terméknév, feature lista, konkrét funkció, képernyőfelvétel leírás, szám/adat
**🟡 Példa hook:** „Egyetlen [funkció / lépés], ami [X] időt spórol neked [időegység]. Megmutatom."
**Ajánlott:** szoftver, eszköz-jellegű termék

### 1.3 Alapító & Eredettörténet (15 sablon)

**Fájl:** `assets/sablonok/alapito.md` (VS-041..055)
**Mikor:** A felelős/alapító személyes háttere, motivációja, miért csinálta a terméket.
**Építőelemek:** alapítói sztori, motiváció, személyes háttér, fordulópont, értékek
**🟡 Példa hook:** „[X] évig csináltam egyedül mindent a vállalkozásomban. [Konkrétum a felelős sztorijából]."
**Ajánlott:** bármely termék

### 1.4 Előtte/Utána & Transzformáció (15 sablon)

**Fájl:** `assets/sablonok/elotte-utana.md` (VS-056..070)
**Mikor:** Van konkrét before-after (tudás, bevétel, képesség, magabiztosság, állapot).
**Építőelemek:** előtte állapot, utána állapot, időkeret, konkrét változás, fordulópont
**🟡 Példa hook:** „[Időtáv] ezelőtt nem tudtam, mi az a [téma]. Ma [konkrét eredmény]."
**Ajánlott:** bármely termék (erős átalakulási ígérettel)

### 1.5 Edukáció & Keretrendszer (25 sablon)

**Fájl:** `assets/sablonok/edukacio.md` (VS-071..095)
**Mikor:** Tanító tartalom: lépések, keretrendszer, tippek, módszer-bemutatás. A legtöbb sablon ebben a kategóriában.
**Építőelemek:** lépések, keretrendszer neve, tipp, konkrét módszer, szám (hány lépés/tipp)
**🟡 Példa hook:** „3 [téma]-trükk, amit a legtöbb kezdő nem ismer. Az első: [konkrét tipp]."
**Ajánlott:** bármely edukációs termék

### 1.6 Storytelling & Narratíva (15 sablon)

**Fájl:** `assets/sablonok/storytelling.md` (VS-096..110)
**Mikor:** Személyes történet, amely tanulságot hordoz és a termékhez vezet.
**Építőelemek:** felelős sztori, hiba/kudarc, fordulópont, tanulság, jelenlegi helyzet
**🟡 Példa hook:** „Két évig gondolkodtam, [mit kezdjek el]. Két évig."
**Ajánlott:** bármely termék

### 1.7 VSL & Direkt Válasz (15 sablon)

**Fájl:** `assets/sablonok/vsl.md` (VS-111..125)
**Mikor:** Közvetlen értékesítési szöveg, ajánlat-prezentáció, erős CTA.
**Építőelemek:** ajánlat, ár, garancia, bónuszok, sürgősség (ha valós), keretrendszer pillérei
**🟡 Példa hook:** „[Konkrét ár]. [Mit kapsz érte]. [Reciprocitás-ütős összehasonlítás]."
**Ajánlott:** előfizetés, csomag, kampány

### 1.8 Komédia & Szórakoztatás (15 sablon)

**Fájl:** `assets/sablonok/komedia.md` (VS-126..140)
**Mikor:** Humoros megközelítés, paródia, meme-formátum, self-aware reklám.
**Építőelemek:** humoros helyzet, paródia tárgya, self-aware elem, popkulturális referencia
**🟡 Példa hook:** „A [külsős szakember] megint [X] hétre tűnt el. De most én csináltam meg [Y] idő alatt. [Termékben]."
**Ajánlott:** ha van humoros felelős/oktató-tartalom, retargeting

### 1.9 Tudomány & Egészség (15 sablon)

**Fájl:** `assets/sablonok/tudomany.md` (VS-141..155)
**Mikor:** Tudományos háttér, kutatás, szisztematikus megközelítés (pl. tanulási módszertan, hatékonyság-kutatás, egészségügyi adat).
**Építőelemek:** kutatás/adat, szakértő vélemény, módszertan, összehasonlítás
**Ajánlott:** kevésbé releváns (csak ha van releváns kutatás/adat — egyébként skip)

### 1.10 Életmód & Rutin (10 sablon)

**Fájl:** `assets/sablonok/eletmod.md` (VS-156..165)
**Mikor:** Hogyan illeszkedik a termék az életbe. Napi rutin, időbeosztás, munka mellett tanulás.
**Építőelemek:** napi rutin, időbeosztás, élethelyzet, „mikor használom"
**🟡 Példa hook:** „Főállás mellett tanultam meg [téma]-t. Vonatúton, ebédszünetben, este 9-kor."
**Ajánlott:** bármely termék (különösen karrierváltóknak / életmód-változóknak)

### 1.11 Összehasonlítás & Verseny (10 sablon)

**Fájl:** `assets/sablonok/osszehasonlitas.md` (VS-166..175)
**Mikor:** [Termék A] vs. [Termék B], saját termék vs. alternatívák, kategória-szintű választás.
**Építőelemek:** két összehasonlított dolog, előnyök/hátrányok, konkrét különbségek
**🟡 Példa hook:** „[Termék A] vs. [Termék B]: mikor melyiket használd? A válasz nem az, amit gondolnál."
**Ajánlott:** szoftver-termékek, kategória-alternatívák

### 1.12 Retargeting & Tölcsér (7 sablon)

**Fájl:** `assets/sablonok/retargeting.md` (VS-176..182)
**Mikor:** Retargeting hirdetés, aki már látta a terméket / járt az oldalon. Emlékeztető, utolsó lökés.
**Építőelemek:** előző interakció, kifogás-kezelés, garancia, ár-emlékeztető
**🟡 Példa hook:** „Tudom, hogy már láttad a [Terméket]. Még gondolkodsz rajta?"
**Ajánlott:** retargeting kampányok

### 1.13 Meta & Produkció (8 sablon)

**Fájl:** `assets/sablonok/meta-produkcio.md` (VS-183..190)
**Mikor:** Self-aware reklám, „mögöttes tartalom", behind-the-scenes, produkciós megközelítés.
**Építőelemek:** self-aware elem, behind-the-scenes, produkciós technika
**Ajánlott:** retargeting, brand awareness

### 1.14 Kihívás & Esemény (7 sablon)

**Fájl:** `assets/sablonok/kihivas.md` (VS-191..197)
**Mikor:** Kihívás-kampány, élő esemény, webinár-meghívó.
**Építőelemek:** kihívás neve/időtartama, esemény-részletek, regisztrációs CTA
**Ajánlott:** kampányok, webinárok

### 1.15 UGC & Speciális Formátumok (10 sablon)

**Fájl:** `assets/sablonok/ugc.md` (VS-198..207)
**Mikor:** UGC stílusú (nem a felelős/oktató beszél), street interview formátum, lista formátum, speciális megközelítés.
**Építőelemek:** UGC szereplő, interjú-kérdés, lista-téma, speciális formátum-leírás
**Ajánlott:** változatos kampányok, TikTok natív

---

## 2. Kategória-relevancia — termék-mátrix

> 🟡 Az oszlop-fejlécek placeholderek. Saját termékportfólióra cseréld; a kategória-sorok általánosak.

### 2.1 Termékek

| Kategória | [Termék A] | [Termék B] | [Termék C] | [Termék D] | [Előfizetés / csomag] |
|-----------|------------|------------|------------|------------|----------------------|
| Testimonial | ✅ | ✅ | ✅ | ✅ | ✅ |
| Termék Demo | ✅✅ | ✅✅ | ✅✅ | ⚠️ | ⚠️ |
| Alapító | ✅ | ✅ | ✅ | ✅✅ | ✅✅ |
| Előtte/Utána | ✅ | ✅ | ✅ | ✅✅ | ✅ |
| Edukáció | ✅✅ | ✅✅ | ✅✅ | ✅ | ✅ |
| Storytelling | ✅ | ✅ | ✅ | ✅✅ | ✅ |
| VSL | ✅ | ✅ | ✅ | ✅ | ✅✅ |
| Komédia | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Tudomány | ❌ | ❌ | ❌ | ❌ | ❌ |
| Életmód | ✅ | ✅ | ✅ | ✅ | ✅ |
| Összehasonlítás | ✅✅ | ✅✅ | ✅ | ⚠️ | ✅ |
| Retargeting | ✅ | ✅ | ✅ | ✅ | ✅ |
| Meta | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Kihívás | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| UGC | ✅ | ✅ | ✅ | ✅ | ✅ |

### 2.2 Egyéb termékek (kampány-jellegű)

| Kategória | Lead Magnet | Webinár | Kihívás | Hosszabb program |
|-----------|-------------|---------|---------|-------------------|
| Testimonial | ✅ | ✅ | ✅ | ✅✅ |
| Termék Demo | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Alapító | ✅ | ✅✅ | ✅ | ✅ |
| Előtte/Utána | ✅ | ✅ | ✅✅ | ✅✅ |
| Edukáció | ✅✅ | ✅✅ | ✅ | ✅ |
| Storytelling | ✅✅ | ✅ | ✅ | ✅ |
| VSL | ✅ | ✅ | ⚠️ | ✅ |
| Komédia | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Tudomány | ❌ | ❌ | ❌ | ❌ |
| Életmód | ⚠️ | ⚠️ | ✅ | ✅ |
| Összehasonlítás | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Retargeting | ✅ | ✅ | ✅ | ✅ |
| Meta | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Kihívás | ⚠️ | ✅✅ | ✅✅ | ✅✅ |
| UGC | ✅ | ✅ | ✅✅ | ✅ |

✅✅ = ideális, ✅ = jó, ⚠️ = csak ha van rá kontextus, ❌ = nem releváns

---

## 2A. Termék típus profilok

| Termék típus | Tipikus CTA | CTA-ban szerepeljen | Speciális elem |
|---|---|---|---|
| **Önálló termék (kurzus, csomag stb.)** | „Vágj bele" / „Próbáld ki" | Termék neve | Tartalmi egységek száma, időtartam |
| **Cég-szintű előfizetés / tagság** | „Próbáld ki" / „Csatlakozz" | Tagság neve | Ár, tagság előnyei |
| **Lead magnet** | „Töltsd le ingyen" / „Kapd meg" | Lead magnet neve | NINCS ár, nincs kötelezettség |
| **Webinár** | „Foglald le a helyed" / „Regisztrálj" | Webinár neve + dátum | Dátum, időpont, élő esemény |
| **Kihívás** | „Csatlakozz a kihíváshoz" | Kihívás neve | Napok száma, feladatok |
| **Hosszabb program** | „Jelentkezz a [program]-ra" | Program neve | Időtartam, transzformáció |

---

## 2B. Wave-besorolási kritériumok

A wave-rendszer célja: a kész kontextusú sablonokat azonnal gyártani, a hiányosakat csak a pótlás után, az irreleváns vagy pótolhatatlan-elemű sablonokat pedig kihagyni. Ne pazarolj energiát olyan sablonra, amihez nincs meg az alap.

### Építőelem-kategóriák és kötelezőségük

| Építőelem | Wave 1 (kötelező) | Wave 2 (pótolható) | Wave 3 (hiánya = skip) |
|---|---|---|---|
| **Terméknév** | ✅ kötelező mindenhez | — | — |
| **Fő eredmény** | ✅ kötelező mindenhez | — | — |
| **Fő fájdalom** | ✅ a legtöbb sablonhoz | Pótolható ha a célcsoport-kontextusból deriválható | — |
| **Ügyfél-szám** | Testimonial sablonokhoz | Kihagyható ha nincs | — |
| **Testimonial idézet** | — | VS-002, VS-009 típusokhoz kell | Konkrét ügyfélnév nélkül skip |
| **Ár / kedvezmény** | VSL sablonokhoz | — | Ár nélkül a VSL sablonok gyengék |
| **Felelős / oktató személyes sztori** | — | Storytelling, Alapító sablonokhoz | Kontextusból deriválható |
| **Humoros kontextus** | — | — | Komédia sablonokhoz kell, nélküle skip |
| **Híres személy** | — | — | VS-001 típushoz kell, nélküle skip |
| **Kutatás / adat** | — | — | Tudomány sablonokhoz kell |
| **Kihívás-részletek** | Kihívás sablonokhoz | — | Név + napok nélkül skip |
| **UGC szereplő** | — | — | UGC sablonok egy részéhez kell |

### Wave besorolás szabálya

1. **Wave 1 (Ready):** A sablon MINDEN placeholder változójához van adat a kontextusban, VAGY a változó opcionális (pl. Megjegyzés).
2. **Wave 2 (Near-ready):** 1-2 kötelező elem hiányzik, de a felhasználó pótolhatja (pl. ügyfél név, aktuális ár, humoros kontextus). VAGY a sablon a hiányzó elem nélkül is működik, csak gyengébb.
3. **Wave 3 (Skip):** A sablon kategóriája nem releváns a termékhez (ld. relevancia-tábla ❌), VAGY 3+ kötelező elem hiányzik, VAGY a hiányzó elem természeténél fogva nem pótolható (pl. híres személy, tudományos kutatás).

---

## 3. Script-struktúra

### Hook (0-5 mp)

A legfontosabb rész. Ha ez nem ragadja meg a nézőt, a többi nem számít.

**Hook típusok a sablonokban:** meglepő állítás/szám, provokatív kérdés, személyes bevallás/vallomás, probléma/fájdalom-indítás, tévhit-leleplezés, termék-meglepetés, lépcsőzetes hook (crescendo).

**Szabály:** A hook legyen konkrét szöveg (amit a felelős/oktató elmondana), ne leírás.

### Body (5-90 mp)

Egy gondolat = egy videó. Ne zsúfold.

**Body építési minták:**
- Sztori: jelenet → probléma → fordulópont → megoldás
- Érvelés: állítás → bizonyíték → következtetés
- Demo: funkció → eredmény → hogyan
- Lista: pont 1 → pont 2 → pont 3
- Kontraszt: régen → most, rossz → jó, ők → mi

### CTA (utolsó 10-20 mp)

| Típus | Arány | Példák |
|-------|-------|--------|
| Rövid direkt | ~40% | „Csekkold a [terméket] és vágj bele." |
| Természetes átvezetés | ~30% | „Pont ezért csináltam a [terméket]. Ha érdekel, nézd meg." |
| Felelősség-átadás | ~20% | „Ha nem próbálod ki, meg se adod az esélyt magadnak." |
| Enyhe sürgősség | ~10% | „Hamarosan árat emelünk." (CSAK ha valós) |

**CTA szabályok:**
- Termék-specifikus hirdetésnél a termék neve legyen a CTA-ban.
- SOHA: „Kattints most!", „Ne hagyd ki!", „Csak ma!".
- CTA ige variálása: „Próbáld ki" / „Végezd el" / „Nézd meg" / „Vágj bele" / „Csatlakozz".
- Egy script = egy CTA.

---

## 4. Videó-hosszak

| Típus | Hossz | Mire jó | Mikor használd |
|-------|-------|---------|----------------|
| Rövid | 15-30 mp | Reels, TikTok, Facebook quick ad | 1 hook + 1 gondolat + 1 CTA |
| Standard | 40-60 mp | Facebook/Instagram ads, YouTube pre-roll | Hook + sztori/érvelés + CTA (ez az alap) |
| Hosszú | 60-90 mp | YouTube ads, organikus | Teljes személyes sztori + vélemény + CTA |

---

## 5. Szerkesztési minták

> 🟡 Saját márkahangra adaptáld a `00-agy/brand/markahang.md` szerint. Az alábbi az általános AI-hiba → emberi-javítás logika.

| AI tendencia | A felelős átírja | Példa |
|---|---|---|
| Túl hosszú body | Rövidít, töröl | 3 bekezdésből 2-t hagy |
| Irodalmi szó | Köznyelvire cserél | „kreálni" → „alkotni" |
| Ismétlődő CTA ige | Variál | Nem kétszer „Próbáld ki" |
| Felesleges bevezetés | Töröl | „Viszont", „Na most" |
| Retorikusan csiszolt záró | Egyszerűsít | Utolsó mondat rövid és ütős |
| Túl sok jelző | Csökkent | Egy jelző elég |

---

## 6. Tiltott szavak és minták

**Tiltott szavak:** „egyedülálló", „kihagyhatatlan", „forradalmi", „garantált" (kivéve tényleges garancia), „exkluzív", „csapatunk büszke", „örömmel jelentjük", „fantasztikus hír", „szenzációs", „hihetetlen", „páratlan", „tökéletes".

**Tiltott minták:**
- „Sziasztok! Ma arról fogok mesélni..." (köszönéssel indít)
- „Ebben a videóban..." (bejelentő stílus)
- „X ok, amiért..." (generikus lista-hook)
- „Nem X. Hanem Y." többször (max 1×)
- Redundancia, csupa nagybetű, felkiáltójelek halmozása
- „Kattints most!", hamis sürgősség

---

## 7. Script példa (kommentálva)

> 🟡 Az alábbi konkrét script egy szoftver-oktató termék példája. Csak a kommentár-logikát kövesd; a tartalmat saját termékre cseréld.

### Jó script — Testimonial + Edukáció kombináció

```
A [szoftver] irányítópultja kezdő szemnek ijesztő lehet.
← [HOOK: Probléma-indítás, azonnali azonosulás]

Funkciók, rétegek, beállítások, millió kis kapcsoló.
← [Fájdalom-konkretizálás, specifikus szakkifejezések]

Elsőnek én se tudtam, hova nézzek.
← [Személyes bevallás: „nekem is"]

Aztán pár nap alatt teljesen megváltozott a kép.
← [Fordulópont]

Több, mint [ügyfélszám] embert tanítottam már [téma]-ra, és pár nap alatt mindenki igazi haladást ért el.
← [Társadalmi bizonyíték, konkrét szám]

A [termék]-ben nulláról indulunk, lépésről-lépésre haladunk, és a végére magabiztosan dolgozol benne.
← [Termék-bemutatás]

Végezd el a [terméket], és légy te is otthon a [témában].
← [CTA: direkt, nem agresszív]
```

**Miért jó:** Hook azonnal azonosít, személyes elem, társadalmi bizonyíték számmal, CTA 1 mondat, ~30 mp.

### Rossz script — miért rossz

```
❌ „Sziasztok! Ma arról fogok mesélni nektek, hogy miért érdemes megtanulni a [téma]-t."
```
Köszönéssel nyit, bejelentő stílus, nincs hook. Az első 3 mp elveszett.

```
✅ „Múlt héten leültem dolgozni egy feladaton. 4 óra alatt kész volt. 3 évvel ezelőtt ehhez 3 hét kellett volna."
```
Személyes tapasztalat + előtte-utána + konkrét számok. Azonnal érdekessé teszi.

---

## 8. Mentális kapcsolók

Szórd szét a koncepciók között, ne használj mindent egyszerre.

### Bizalom

| Kapcsoló | Hogyan |
|----------|--------|
| Tekintély | [ügyfélszám]+ ügyfél/tanuló, [X] év tapasztalat |
| Társadalmi bizonyíték | Konkrét szám, visszajelzés-idézet |
| Hasonlóság | „Én is pont így voltam" |
| Átláthatóság | A felelős/oktató bevallja a hibáit |
| Közös ellenség | Rossz alternatívák, átverős guruk |

### Vágy és kíváncsiság

| Kapcsoló | Hogyan |
|----------|--------|
| Kíváncsiság | „Van egy trükk, amit a legtöbb [szakember] nem használ" |
| Meglepetés | Váratlan szám, tény |
| Vizualizáció | „Képzeld el, hogy magabiztosan csinálod a [konkrét eredmény]-t" |
| Személyesség | A felelős/oktató hibái, félelmei, küzdelmei |

### Cselekvés

| Kapcsoló | Hogyan |
|----------|--------|
| Kölcsönösség | Ingyen ad értéket → a termék a mélyebb szint |
| Egyszerűsítés | „Lépésről-lépésre, nem kell mindent tudni" |
| Személyes megszólítás | „Ha te is [specifikus helyzet]..." |
| Veszteségkerülés | „Mennyit vesztesz, ha nem cselekszel?" (etikusan) |
