# Hirdetés Videó Script Író — Workflow-részletek

> Smart Factory mód: szisztematikus gyártósor. Teljes kontextus + minden sablon betöltése → Factory Manifest → prioritás-alapú generálás hullámokban.

## Tartalomjegyzék

1. [Márkahang és formázás](#márkahang-és-formázás)
2. [Fázis 0 — Termék és kontextus](#fázis-0--termék-és-kontextus)
3. [Fázis 1 — Factory Manifest](#fázis-1--factory-manifest)
4. [Fázis 2 — Hiányzó elemek kikérdezése](#fázis-2--hiányzó-elemek-kikérdezése)
5. [Fázis 3 — Generálás loop](#fázis-3--generálás-loop)
6. [Fázis 4 — Review + Variációk](#fázis-4--review--variációk)
7. [Resume protokoll](#resume-protokoll)
8. [Progress fájl formátum](#progress-fájl-formátum)
9. [Minőségi checklist](#minőségi-checklist)

---

## Márkahang és formázás

Minden generált szövegben (output, sablon-kitöltés, javaslat) kövesd a `00-agy/brand/markahang.md` szabályait (I. Alapelvek + II. Mit ne + ha van, III. Hirdetés / videoszkript):

- **Gondolatjel (– vagy —) mondat közben:** SOHA. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Tegezés / magázás:** a `00-agy/brand/markahang.md` szerint (default: tegezés).
- **Szókincs:** a `00-agy/brand/markahang.md` I. Alapelvek bekezdéseit (Hang, Tartalom-elvek) kövesd, és kerüld a II. Mit ne szekció anti-mintáit.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor/bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan csiszolt mondatokat.
- **„Nem X, hanem Y" tiltás:** max 1× az EGÉSZ batch-ben (nem scriptenként). A tiltás kiterjed a rejtett ok-cáfolat variánsokra is, mert ezeket a per-script ellenőrzés átengedi: „Nem azért…, hanem…", „Nem a [valami]-vel/-dal van baj", „Nem [X], csak [Y]". Mindegyik ugyanaz a kontrasztív LLM-séma. Helyettesítési stratégiák:
  - **Töröld az első felet.** ❌ „Nem az appokkal volt a baj. Hanem azzal, hogy nem rendszert építettél." → ✅ „Nem rendszert építettél, csak egy újabb helyet csináltál."
  - **Kezdd a lényeggel.** ❌ „Nem több funkció kell, hanem egy rendszer." → ✅ „Egy működő rendszer kell."
  - **Két külön mondat.** ❌ „Nem a technológia a fontos, hanem a folyamat." → ✅ „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** ❌ „Nem az a kérdés, melyik app jobb. Hanem az, hogy használod-e." → ✅ „A kérdés: használod-e egyáltalán?"

---

## Fázis 0 — Termék és kontextus

### Cél
Kiválasztani a terméket, betölteni a teljes kontextust, ellenőrizni, van-e korábbi progress.

### Lépések

1. **Sablonok betöltése (mindig):** MIND a 15 sablon fájl (`assets/sablonok/*.md`) — ezek a skill része.
2. **Kontextus betöltése:** a SKILL.md `## Bemenet` táblája szerint. A `00-agy/brand/markahang.md`-ből különösen a II. Mit ne és a III. Hirdetés / videó-szkript fejezet kell; mellé a termék `kontextus.md`-je, `kontextus-elemek.md`-je, `uzenetek.md`-je, `celcsoport.md`-je és `testimonialok.md`-je. Ami `KITÖLTENDŐ`, az a wave-besorolásban jelenik meg: a hiányos elemű sablonok Wave 2-be kerülnek, és a Fázis 2-ben pótolod.
3. Jelezd: „Hirdetés videó script gyártósor. Sablonok betöltve[, kontextus betöltve / kontextus-fájl nincs, pótolom kérdésekkel]."
4. Kérdezd: „Melyik termékhez / ajánlathoz készítünk scripteket?"

### Termék kiválasztás

A felhasználó megadja a terméket. **Hierarchia minden terméknél (a forrás csak akkor használandó, ha létezik):**
1. Univerzális (cég-szintű) alap, ha van: `00-agy/brand/ajanlatok/_attekintes.md` (+ `00-agy/brand/uzleti-profil.md` ha van).
2. Termék-specifikus override, ha van: `00-agy/brand/ajanlatok/<ajanlat>/kontextus-elemek.md`.
3. Narratív kiegészítés (a sablonokhoz), ha van: a teljes `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md` fájl.

Ha ezek a fájlok nincsenek meg, a felhasználótól begyűjtött kulcsadatok (terméknév, fő eredmény, fő fájdalom, célcsoport, ár, bizonyíték) töltik be ezt a szerepet.

A termék fajtája szerint:
- **Önálló termék:** töltsd be (ha van) (a) `kontextus-elemek.md` (override-ok), (b) `kontextus.md` (narratíva), (c) meglévő script fájl (a SKILL.md Mentés helyén lévő `scriptek.md`).
- **Cég-szintű előfizetés / tagság:** az univerzális cég-szintű fájlok adják a változókat és a narratívát, ha léteznek; különben kikérdezésből.
- **Lead magnet / Webinár / Kihívás / Kampány:** kérd a kontextust (Notion URL / fájl / felhasználó input). Az univerzális cég-szintű elemek alapként érvényesek, ha elérhetők.

### Resume check

Ellenőrizd: van-e `progress.md` a Mentés helyén?
- **Ha van:** olvasd be. „Korábbi gyártás találva: [X]/[Y] sablon kész. Folytassam, ahol abbahagytad, vagy kezdjünk újat?"
- **Ha nincs:** új gyártás indul.

### Meglévő scriptek

Ha van meglévő script fájl, keresd ki a meglévő angle-eket. Ezeket NE ismételd a gyártás során.

### Összefoglalás

```
## Fázis 0 — Összefoglaló

| Elem | Tartalom |
|------|----------|
| Termék | [termék neve] |
| Termék típus | önálló / előfizetés / lead magnet / webinár / kihívás / hosszabb program |
| Kontextus forrás | [fájlnév / Notion URL / felhasználó input] |
| Meglévő scriptek | [X db] (angle-ek: [...]) |
| Resume | Új gyártás / Folytatás ([X]/[Y] kész) |
```

→ „Stimmel? Ha igen, készítem a Factory Manifest-et."

---

## Fázis 1 — Factory Manifest

### Cél
Minden 207 sablont értékelni a betöltött kontextus tükrében. Wave 1 / Wave 2 / Wave 3 besorolás.

### Lépések

1. **Építőelemek kinyerése a kontextusból** (a 6 kategória szerint, ld. sablonok-katalogus.md 2B szekció):

```
## Elérhető építőelemek

### ✅ Megvan
- Terméknév: „[...]"
- Fő eredmény: „[...]"
- Fő fájdalom: „[...]"
- Ügyfél-szám: [szám]
- Felelős/oktató személyes sztori: „[...]"
- [stb.]

### ⚠️ Kikövetkeztethető
- Időkeret: ~[X] hét (termék terjedelméből becsülve)
- [stb.]

### ❌ Hiányzik
- Ár/kedvezmény
- Konkrét ügyfél név
- Humoros kontextus
- [stb.]
```

2. **Kategória-relevancia ellenőrzés.** A sablonok-katalogus.md 2.1/2.2 mátrixa alapján: melyik kategóriák relevánsak ehhez a termék-típushoz?

3. **Wave besorolás.** Minden 207 sablont besorolni (sablonok-katalogus.md 2B kritériumai alapján):

```
## Factory Manifest — [Termék neve]

### Wave 1 — Azonnal generálható ([X] sablon)

| Kategória | Sablonok | db |
|---|---|---|
| Testimonial | VS-004, VS-005, VS-006, VS-007, VS-008, VS-010, ... | 16 |
| Termék Demo | VS-021, VS-022, VS-023, VS-025, ... | X |
| Edukáció | VS-071, VS-072, VS-073, ... | X |
| [stb.] | | |

### Wave 2 — 1-2 elem hiányzik ([X] sablon)

| Kategória | Sablonok | Hiányzó elem |
|---|---|---|
| Testimonial | VS-002, VS-003, VS-009 | ügyfél név |
| Komédia | VS-126, VS-127, VS-128, ... | humoros kontextus |
| VSL | VS-111, VS-112, ... | ár/kedvezmény |
| [stb.] | | |

### Wave 3 — Kihagyva ([X] sablon)

| Kategória | Sablonok | Ok |
|---|---|---|
| Tudomány | VS-141..VS-155 | Nem releváns |
| Testimonial | VS-001 | Híres személy szükséges |
| [stb.] | | |

### Összesítés
- Wave 1: [X] sablon — azonnal generálható
- Wave 2: [X] sablon — [Y] elem pótlása után generálható
- Wave 3: [X] sablon — kihagyva
- Meglévő (nem ismétlendő): [X] angle
- **Becsült batch-ek száma:** ~[X] (10-12 script/batch)
```

4. **Felhasználó jóváhagyás.** → „Ez a Factory Manifest. Stimmel a besorolás? Ha igen, kikérdezem a hiányzó elemeket."

### Fontos szabályok
- NE hallucináld a hiányzó adatokat: ha nincs a kontextusban, jelezd.
- A „Kikövetkeztethető" kategóriát csak akkor használd, ha a forrás egyértelmű.
- Ha a meglévő scriptek között van olyan angle, ami egy sablonra illeszkedik, azt a sablont jelöld „Már lefedve" jelzéssel.
- **Szám-forrás kötelező.** Minden konkrét szám, évszám, időtartam (pl. „15 év tapasztalat", „3 hét alatt", „200 ügyfél") csak akkor kerülhet egy scriptbe, ha a brief, az avatar vagy a betöltött kontextus megadja. A script Megjegyzés-blokkjában jelöld a forrást (melyik brief-sor vagy avatar-elem). Ha nincs forrás, ne írd le a számot, fogalmazz forrás nélkül. A talált adatot soha ne találd ki, hogy a hook „erősebb" legyen.

---

## Fázis 2 — Hiányzó elemek kikérdezése

### Cél
A Wave 2 sablonok hiányzó elemeit egyszeri, konszolidált kérdéskörben begyűjteni.

### Lépések

1. **Csoportosítás elem-típusonként** (NEM sablononként):

```
## Hiányzó elemek — kérdések

A következő elemek pótlásával további [X] sablon válik generálhatóvá:

1. **Konkrét ügyfél név** ([X] sablon függ tőle: VS-002, VS-003, VS-009, ...)
   → Adj meg 2-3 ügyfél/tanuló nevet, akikre hivatkozhatunk.

2. **Ár / aktuális kedvezmény** ([X] sablon: VS-111, VS-112, ...)
   → Van most érvényes ár vagy kedvezmény?

3. **Humoros kontextus** ([X] sablon: VS-126, VS-127, ...)
   → Van valami vicces sztori, helyzet, ami a felelőssel/oktatóval történt?

4. [stb.]
```

2. **Felhasználó válaszol.** Amit megad, az bekerül az építőelemek közé. Amit nem tud, ahhoz tartozó sablonok Wave 3-ba kerülnek (skip).

3. **Manifest frissítés.** „Köszönöm! [X] további sablon generálható. [Y] sablon áthelyezve Wave 3-ba. Összesen [Z] sablonból generálunk. Indulhat?"

---

## Fázis 3 — Generálás loop

### Cél
Szisztematikusan végigmenni az összes Wave 1 + Wave 2 sablonon, kategóriánként haladva, batch-ekben generálva.

### Sorrend
A kategória-relevancia tábla alapján: ✅✅ kategóriák előbb, ✅ utána, ⚠️ legvégül. Ezen belül: Wave 1 sablonok előbb, Wave 2 utána.

### Batch méret
**10-12 teljes script per batch.** Minden script tartalmazza: teljes Hook + Body + CTA szöveg, felvétel-lista (modulonként min. 2 vizuális opció), megjegyzés, UTM-sablon.

### Sablon követés
**KRITIKUS:** minden scriptnél a sablon struktúráját kövesd. A sablon adja a Hook + Body + CTA váz-szerkezetét, te a kontextus építőelemeivel töltöd ki a változókat.

**NE generálj fejből.** Ha egy sablon pl. VS-006 (Szám-Első Eredmény Testimonial), akkor annak a struktúráját kövesd: szám a hook-ban, „nem vagyok különleges" relatálhatóság, 1 specifikus dolog ami máshol nincs, második eredmény-szám.

### Output formátum (minden scriptnél)

```
# [SORSZÁM] — [CÍM]

## Script

**Sablon:** VS-[XXX] ([kategória])
**Angle:** [egy mondatos szög]
**Célcsoport:** [kik]
**Videó hossz:** Rövid (15-30 mp) / Standard (40-60 mp) / Hosszú (60-90 mp)

---

[script szövege bekezdésenként]

[Minden gondolat új bekezdés.]

[CTA mondat az utolsó bekezdésben.]

## Felvétel lista

| Modul | Szöveg | Mi történik |
| --- | --- | --- |
| Hook | [hook szöveg ~10 szó] | **1)** [konkrét vizuális ötlet] **2)** [másik vizuális ötlet] |
| Body 1 | [body szöveg ~10 szó] | **1)** [konkrét vizuális ötlet] **2)** [másik vizuális ötlet] |
| Body 2 | [ha van] | **1)** ... **2)** ... |
| CTA | [cta szöveg] | **1)** [vizuális ötlet] **2)** [vizuális ötlet] |

## Megjegyzés
[Milyen sablon alapján, mit érdemes figyelni a felvételnél]

## UTM
```
utm_source={{site_source_name}}&utm_medium=social&utm_campaign={{campaign.name}}&utm_content={{adset.name}}&utm_term={{ad.name}}
```
```

### Felvétel lista szabályok
- Minimum **2 vizuális opció** modulonként, számozva: **1)**, **2)**.
- Csak **konkrét, kreatív** vizuális ötletek.
- **NE** írd: „A felelős kamerába néz" (az az alapértelmezett).
- Legyen **konkrét**: ne „valami animáció", hanem pl. „Számláló: 0 → [ügyfélszám] forog gyorsan".

### Batch lezárás

Minden batch (10-12 script) után:

1. **Mentés:** fűzd hozzá a `scriptek.md`-hez (a SKILL.md Mentés sora szerint). Határozd meg a következő sorszámot a meglévő fájlban.
2. **Progress frissítés:** frissítsd a `progress.md`-t ugyanott.
3. **Jelzés:**

```
---
**Batch [X] kész.** [Y] script generálva ebben a batch-ben.

Kategória haladás:
- [Kategória neve]: [X]/[Y] sablon kész

Következő batch: [Kategória neve] — [Wave X] — VS-[XXX]..VS-[XXX]

Összes haladás: [X]/[Y] sablon generálva ([Z]%)

→ „Folytassuk?"
```

### Kategória váltás

Ha egy kategória összes sablonja kész:

```
---
**[Kategória neve] KÉSZ!** [X]/[X] sablon generálva.

Következő kategória: [Kategória neve] ([X] sablon)
→ „Folytassuk a következő kategóriával?"
```

---

## Fázis 4 — Review + Variációk

### Cél
Az összes generált script áttekintése, kedvencek jelölése, variációk készítése.

### Mikor fut
- A felhasználó bármikor kérheti (batch közben is).
- Automatikusan a gyártás végén.

### Variáció típusok

Ha a felhasználó kéri:
- **Hook variáció:** más hook-típus, ugyanaz a body/CTA.
- **Hossz variáció:** rövid verzió egy standard scriptből (vagy fordítva).
- **Célcsoport variáció:** más célcsoportra átírva.
- **Termék variáció:** másik termékre adaptálva (ha van kontextus).

---

## Resume protokoll

Ha a felhasználó egy korábbi gyártást folytat:

1. Olvasd be a `progress.md`-t.
2. Olvasd be a meglévő script fájlt (angle-ek miatt).
3. Azonosítsd: hol hagytuk abba? Melyik kategória, melyik sablon?
4. Jelezd: „Folytatom a [Kategória] kategóriánál, VS-[XXX]-tól. [X]/[Y] sablon van hátra."
5. Folytasd a Fázis 3-mal a megfelelő ponttól.

---

## Progress fájl formátum

```markdown
# [Termék neve] — Factory Progress

- Indítás: [dátum]
- Termék típus: [típus]
- Kontextus forrás: [fájlnév / Notion URL]

## Összesítés
- Wave 1: [X] sablon | Generált: [Y] | Hátralévő: [Z]
- Wave 2: [X] sablon | Generált: [Y] | Hátralévő: [Z]
- Wave 3: [X] sablon | Kihagyva

## Pótolt elemek
- Ügyfél nevek: [név1, név2, ...]
- Ár: [...]
- [stb.]

## Részletes haladás

### testimonial (20 sablon)
- Wave 1: VS-004 ✅, VS-005 ✅, VS-006 ⬜, VS-007 ⬜, ...
- Wave 2: VS-002 ⬜ (ügyfél_név), VS-003 ⬜ (ügyfél_név)
- Wave 3: VS-001 ❌ (híres_személy)

### termek-demo (20 sablon)
- Wave 1: VS-021 ⬜, VS-022 ⬜, ...
[stb. minden kategóriához]

## Utolsó session
- Dátum: [dátum]
- Utolsó generált: VS-[XXX] ([kategória])
- Következő: VS-[XXX] ([kategória])
```

---

## Minőségi checklist

Minden generált scriptnél ellenőrizd:

- [ ] Hook megállítja a görgetést? (nem köszönéssel indít)
- [ ] Egy gondolat = egy videó? (nem zsúfolt)
- [ ] Van konkrét részlet? (szám, név, helyzet, évszám)
- [ ] Van személyes/sebezhető mozzanat? (felelős/oktató hiba, félelem)
- [ ] CTA nem agresszív? (felelősség-átadás)
- [ ] Termék neve a CTA-ban? (nem általános „a portfólió" — kivéve cég-szintű előfizetés/tagság hirdetés)
- [ ] Tegezés / a brand-hang szerinti megszólítás mindenhol?
- [ ] Nincs gondolatjel mondat közben?
- [ ] „Nem X, hanem Y" max 1× per szöveg?
- [ ] Nincs tiltott szó/frázis?
- [ ] Nincs redundancia?
- [ ] Mondatok egyszerűek, beszélt nyelven?
- [ ] Sablon-struktúrát követi? (nem fejből generált)
- [ ] Nem ismétli a meglévő angle-eket?
- [ ] Felvétel listában min. 2 vizuális opció modulonként?
- [ ] CTA-igék variálva? (nem kétszer „Próbáld ki" egymás után)
- [ ] Minden konkrét szám/évszám/időtartamnak van forrása a Megjegyzés-blokkban? (ha nincs, ki kell venni)

### Batch-szintű ellenőrzés (a batch lezárása előtt, az egész 10-12 scriptre)

A fenti checklist scriptenként mér. Ezek a batch egészét nézik, mert a slop pont a script-ek közti ismétlésben jelenik meg:

- [ ] **Rejtett ok-cáfolat formula** („Nem a …-vel van baj", „Nem azért…, hanem…") max 1× az EGÉSZ batch-ben?
- [ ] **CTA-diverzitás:** a záró CTA-formulát (terméknév + garancia) szó szerint max a scriptek 40%-ában ismétled? A többit variáld: kérdés, kihívás, kockázat-nélküliségre utaló zárás, időbeli sürgősség. Példa-sablonok (a brand-hangra igazítva):
  - **Kérdés-zárás:** „Megnézed magadnak a [terméknév]-et, vagy maradsz ott, ahol most vagy?"
  - **Kihívás-zárás:** „Add neki egy hetet. Ha addigra nem mozdul, visszakapod az árát."
  - **Kockázat-nélküli zárás:** „Nincs vesztenivalód: [garancia röviden]. A link a leírásban."
  - **Sürgősség-zárás:** „[kedvezmény / határidő] még [időkeret]-ig él. Utána a teljes ár megy."
  - **Felelősség-átadó (default) zárás:** „A [terméknév] ott van. A döntés a tiéd."
