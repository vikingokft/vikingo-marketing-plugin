# Hirdetés Szövegíró: Workflow Részletek

> Három mód: Formula (versenytárs elemzés + adaptáció), Szabad (batch generálás), Vezetett (elemfeltérképezés + irányított generálás). 3 fázis + Fázis 0.

## Tartalomjegyzék

1. Márkahang és formázás
2. Fázis 0: Mód és kontextus
3. Fázis 1: Építőelemek feltérképezése
4. Fázis 2: Elemzés / Generálás / Elemfeltérképezés
5. Fázis 3: Teljes hirdetés szöveg + Output
6. Minőségi checklist

---

## 1. Márkahang és formázás

A `00-agy/brand/markahang.md` az irányadó minden generált szövegben (output, sablon-kitöltés, javaslat): az I. Alapelvek, a II. Mit ne és a III. Hirdetés fejezet. Ha ezek még `KITÖLTENDŐ`-k, tartsd az alábbi alap-szabályokat:

- **Gondolatjel (– vagy —) mondat közben:** SOHA. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Megszólítás:** a cég-hang szerint (alapesetben tegezés, kivétel nélkül).
- **Szókincs:** ha van `00-agy/brand/markahang.md`, az I. Alapelvek bekezdéseit kövesd, és kerüld a II. Mit ne szekció anti-mintáit; ha nincs, kerüld a sablonos AI-szókincset és a fellengzős marketing-frázisokat.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor/bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan csiszolt mondatokat.
- **„Nem X, hanem Y" TILTÁS:** Az AI leggyakoribb és legfárasztóbb szerkezete. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi retorikai funkciója van. Helyettesítési stratégiák:
  - **Töröld az első felet.** Ha a „hanem" utáni rész önmagában megáll, a tagadó fél felesleges.
  - **Kezdd a lényeggel.** ❌ „Nem több funkció kell, hanem egy rendszer." → ✅ „Egy működő rendszer kell."
  - **Két külön mondat.** ❌ „Nem a technológia a fontos, hanem a folyamat." → ✅ „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** ❌ „Nem az a kérdés, melyik app jobb. Hanem az, hogy használod-e." → ✅ „A kérdés: használod-e egyáltalán?"

---

## 2. Fázis 0: Mód és kontextus

### Cél
Eldönteni melyik módban dolgozunk, betölteni a kontextust, azonosítani a terméket és platformot.

### Lépések

1. Kontextus betöltése a SKILL.md `## Bemenet` táblája szerint: `markahang.md` (I. Alapelvek + II. Mit ne + III. Hirdetés), `kontextus-elemek.md`, `uzenetek.md`, `celcsoport.md`, `testimonialok.md`. A kötelező hiányokat egyetlen üzenetben kérdezd meg, és írd a kanonikus fájlba.
2. Jelezd: „Hirdetés szövegeket írunk." Ha betöltöttél kontextust: „Betöltöttem a kontextust." Ha nem volt fájl: „Nincs kontextus-fájl, pár dolgot kérdezek."
3. Kérdezd: „Melyik módban dolgozunk?"

### Mód választás

| Mód | Mikor | Mit csinál |
|-----|-------|-----------|
| **Formula** | Van versenytárs hirdetés szöveg | Elemzés → formula kinyerés → adaptáció |
| **Szabad** | „Bízd rám", batch generálás kell | 50 címsor VAGY 50 elsődleges szöveg, elosztott típusokkal |
| **Vezetett** | Alaposan végig akarom gondolni | Kontextus elemek feltérképezése → irány választás → célzott generálás |

### Közös kérdések (max 4):

1. Mód? (Formula / Szabad / Vezetett)
2. Melyik termék? (ha nem derül ki a kontextusból)
3. Melyik platform? (Meta / Google / TikTok / mindegyik)
4. Mi a kampány célja? (forgalom / lead / értékesítés / webinár regisztráció)

### Ha Formula mód:
- A felhasználó beilleszti a versenytárs hirdetés(ek) szövegét
- Ha több mint 1 hirdetés → batch mód
- „Kaptam [X] hirdetés szöveget. Elemzem."

### Ha Szabad mód:
- Ha elérhető, töltsd be a termék kontextus-elemek fájlt. Fallback: a `kontextus.md` „Kontextus elemek" szekciója. Ha egyik sincs, kérdezd meg a kulcs-adatokat (terméknév, ár, fő ígéret, célcsoport) vagy dolgozz a beillesztett anyagból.
- Kérdezd: „Címsorokat vagy elsődleges szövegeket generáljak?"
- Kérdezd: „Van célcsoport szűkítés, vagy mindenkit célozunk?" (ha van több avatár)

### Ha Vezetett mód:
- Ha elérhetők, töltsd be a termék kontextus-elemek fájlt + `uzenetek.md` + `celcsoport.md` (teljes avatár, nem csak tartalomjegyzék). Fallback: a `kontextus.md` „Kontextus elemek" szekciója. Ha egyik sincs, kérdezd meg a kulcs-adatokat (termék, fő ígéret, célcsoport, fő fájdalom, social proof) vagy dolgozz a beillesztett anyagból.
- „Feltérképezem az elérhető elemeket." (Ha volt fájl: „Betöltöttem a kontextust.")

**Összefoglalás:**

| Elem | Tartalom |
|------|----------|
| Mód | Formula / Szabad / Vezetett |
| Termék | [...] |
| Platform | Meta / Google / TikTok |
| Kampány cél | forgalom / lead / értékesítés |

→ „Stimmel? Ha igen, [elemzem / generálom / feltérképezem az elemeket]."

---

## 3. Fázis 1: Építőelemek feltérképezése

### Cél
Mielőtt bármit generálnánk, ellenőrizni hogy a kontextusban megvannak-e a sablonok kitöltéséhez szükséges változók. Ez megakadályozza, hogy olyan sablonokat használjunk, amihez nincs elég adat (→ hallucináció), és lehetőséget ad hiányzó elemek pótlására.

### Mikor fut
- **Formula módban:** KIHAGYHATÓ — itt versenytárs szöveget adaptálunk, nem kontextusból dolgozunk
- **Szabad és Vezetett módban:** fontos a generálás előtt — így nem hallucinálsz hiányzó adatot. A változókat kontextus-fájlból, a felhasználó válaszaiból vagy a beillesztett anyagból gyűjtöd össze; nem feltétel, hogy fájl legyen.

### Lépések

1. **Kontextus beolvasás:** Ha van kontextus-elemek fájl, keresd benne az „Építőelemek (hirdetési változók)" szekciót
   - Ha megvan → olvasd be, ez a fő forrás
   - Ha nincs ilyen szekció → a kontextus fájl egyéb szekcióiból deriválod (ajánlat, eredmény, probléma, stb.)
   - Ha a termék mappája még üres → a 2. pont kategóriáit használd kérdező-listaként, egyetlen üzenetben, és a válaszokat írd a `kontextus-elemek.md`-be.

2. **Változó ellenőrzés 6 kategóriában:**

| Kategória | Ellenőrzendő | Honnan |
|-----------|-------------|--------|
| **Ajánlat** | terméknév, ár, garancia, ingyenes ajánlat, csomag | kontextus Alap infók + Építőelemek |
| **Eredmény** | fő eredmény, időkeret, átalakulás, feature-ök, advantage | kontextus Termék célja + Before-After + USP |
| **Probléma** | fő fájdalom, félelem, akadály, rossz alternatíva | kontextus Célcsoportok + Kifogások |
| **Bizonyíték** | ügyfélszám, értékelés, testimonial, szakértő | kontextus Visszajelzések + Oktató |
| **Célcsoport** | megszólítás, szint, vágy, identitás | kontextus Célcsoportok |
| **CTA** | cselekvés, sürgősség, lökés | kontextus Ajánlat + kampány cél |

3. **Eredmény megmutatása:**

```
## Építőelemek ellenőrzés

### ✅ Megvan (használható sablonokhoz)
- Terméknév: „[termek]"
- Fő eredmény: „[fő eredmény]"
- Fő fájdalom: „[fő fájdalom]"
- Feature-ök: [...]
- Testimonial: „[eredménytörténet]"
- ... [összes elérhető]

### ⚠️ Kikövetkeztethető (használom, de ellenőrizd)
- Időkeret: ~[X] (kurzus/termék hosszából becsülve)
- Advantage: „[...]" (USP-ből deriválva)

### ❌ Hiányzik
- Ár / kedvezmény → Ajánlat/Akció sablonok KIHAGYVA
- Ügyfélszám → Társadalmi bizonyíték sablonok gyengébbek lesznek

### Sablon javaslat
Ezek a sablontípusok működnek a meglévő elemekkel:
- ✅ PAS, BAB, Storyselling (probléma + eredmény megvan)
- ✅ FAB (feature-ök megvannak)
- ✅ Előny-ígéret címsorok (eredmény + időkeret megvan)
- ⚠️ Társadalmi bizonyíték címsorok (testimonial van, de ügyfélszám hiányzik)
- ❌ Ajánlat/Akció címsorok (ár/kedvezmény hiányzik)
```

4. **Döntés:**
   - Ha minden fontos változó megvan → „Minden megvan, indulhatunk!"
   - Ha hiányzik valami pótolható → „Ezek hiányoznak: [...]. Pótoljuk, vagy kihagyjuk az érintett sablonokat?"
   - Ha sok hiányzik → „A kontextus hiányos. Javaslom, hogy először futtasd a kontextus-építő skillt az Építőelemek szekció kitöltéséhez."

### Fontos szabályok
- NE hallucináld a hiányzó adatokat — ha nincs ár, ne találj ki egyet
- A „Kikövetkeztethető" kategóriát csak akkor használd, ha a forrás egyértelmű
- A sablon javaslat a `references/placeholder-registry.md` illesztési logikáját követi
- Formula módban ez a fázis KIHAGYHATÓ

---

## 4. Fázis 2: Elemzés / Generálás / Elemfeltérképezés

### Formula mód: Elemzés

**Single mód (1 hirdetés):**

```
## Hirdetés elemzés

**Címsor típus:** [7-ből]
**Elsődleges szöveg formula:** [10-ből]
**Triggerek:** [33-ból + kognitív torzítások, konkrét idézettel]
**Célcsoport:** [becslés]
**Awareness szint:** [5-ből]
**CTA:** [erős / átmeneti / gyenge + szöveg]

### Hatékonyság (1-10)
| Szempont | Pont |
|----------|------|
| Hook erőssége | [1-3] |
| Érzelmi bevonás | [1-3] |
| CTA egyértelműsége | [1-2] |
| Célcsoport illesztés | [1-2] |
| **Összesen** | **[X]/10** |

### Kinyert formula
[Brand-független, újrahasználható séma]

### Alkalmazhatóság a saját ajánlatra
[Illeszkedik-e, melyik célcsoport, kell-e módosítani]
```

**Batch mód (5-10 hirdetés):**
Mindegyikhez rövid elemzés + összesítő:
- Top mintázatok (melyik címsor típus / formula dominál)
- Trigger-térkép (melyik triggerek a leggyakoribbak)
- Awareness szint eloszlás
- Top 3 újrahasználható formula, rangsorolva

→ „Melyik formulá(ka)t adaptáljam?"

---

### Szabad mód: Batch generálás

**Címsor generálás (50 db):**

Elosztás a 7 típus között:

| Típus | Db | Arány |
|-------|----|-------|
| Ajánlat / Akció | 8-9 | ~18% |
| Előny-ígéret | 8-9 | ~18% |
| Termékleírás | 7-8 | ~15% |
| Társadalmi bizonyíték | 6-7 | ~12% |
| Meglepő állítás | 5-6 | ~10% |
| Probléma-megoldás | 5-6 | ~10% |
| Kíváncsiság-keltés | 4-5 | ~8% |
| **Vegyes / kísérletező** | 4-5 | ~8% |

**Sablon betöltés:** Generálás előtt töltsd be a releváns címsor sablon fájlokat az `assets/sablonok/cimsor/` mappából. Batch módnál töltsd be mind a 7-et (ajanlat-akcio.md, elony-igeret.md, problema-megoldas.md, meglepo-allitas.md, tarsadalmi-bizonyitek.md, termekleiras.md, kivancisag-keltes.md). A sablonokban konkrét struktúrák és példák vannak, ezeket kövesd.

**Szabályok:**
- Minden típusból legalább 4 db
- A sablon fájlokból merítsd a struktúrákat, ne generálj fejből
- Variáld a triggereket: ne legyen 10 egymás után ugyanazzal a triggerrel
- Jelöld a típust minden címsor mellett
- Platform limit betartása (Meta: 40 kar, Google: 30 kar)

**Output: táblázat**

| # | Típus | Címsor | Kar | Trigger |
|---|-------|--------|-----|---------|
| 1 | Ajánlat | „7 nap ingyen. Törlöd, ha nem tetszik." | 38 | Garancia |
| 2 | Meglepő | „2 millió Ft-ot kerestem [készség]gel" | 34 | Specifikusság |
| ... | ... | ... | ... | ... |

**Elsődleges szöveg generálás (50 db):**

Elosztás a 10 formula között:

| Formula | Db | Arány |
|---------|----|-------|
| FAB | 7-8 | ~15% |
| 4P | 6-7 | ~13% |
| Storyselling | 6-7 | ~13% |
| PAS | 5-6 | ~11% |
| AIDA | 5-6 | ~11% |
| QUEST | 4-5 | ~9% |
| BAB | 3-4 | ~7% |
| Feel-Felt-Found | 3-4 | ~7% |
| ACCA | 2-3 | ~5% |
| StoryBrand | 2-3 | ~5% |
| **Vegyes / kísérletező** | 2-3 | ~5% |

**Sablon betöltés:** Generálás előtt töltsd be a releváns elsődleges szöveg sablon fájlokat az `assets/sablonok/elsodleges-szoveg/` mappából. Batch módnál töltsd be mind a 10-et (fab.md, 4p.md, storyselling.md, pas.md, aida.md, quest.md, bab.md, feel-felt-found.md, acca.md, storybrand.md).

**Szabályok:**
- Minden formulából legalább 2 db
- A sablon fájlokból merítsd a struktúrákat, ne generálj fejből
- Első 125 karakter a legfontosabb (Meta hajtás feletti)
- Jelöld a formulát és awareness szintet minden szöveg mellett
- Awareness szinteket is elosztd (ne legyen mind „termék-tudatos")

**Output: táblázat + szövegek**

| # | Formula | Awareness | Első 125 kar | Trigger |
|---|---------|-----------|--------------|---------|
| 1 | PAS | Probléma-tudatos | „3 éve tanulod egyedül a [készség]t..." | Fájdalom |
| ... | ... | ... | ... | ... |

Utána a teljes szövegek kifejtve, sorszámmal.

→ „Jelöld meg a kedvenceidet (sorszámmal), és azokból csinálok A/B variációkat + kreatív briefet."

---

### Vezetett mód: Elemfeltérképezés

**1. lépés: Kontextus elemek kinyerése**

A betöltött fájlokból nyerd ki és prezentáld az elemeket: `kontextus-elemek.md`, `uzenetek.md`, `celcsoport.md`, `testimonialok.md`, tartalékként a `kontextus.md` megfelelő szekciója. A hiányzó elemeket jelöld, és a kötelezőket kérdezd meg:

```
## Elérhető kontextus elemek

### Termék értékek (tulajdonság → funkció → előny)
| Tulajdonság | Funkció | Előny (hirdetésben) |
|-------------|---------|---------------------|
| [pl. [termék-szám] termék] | [Minden témát egy helyen tanulhatsz] | [Nem kell több helyen keresgélned] |
| ... | ... | ... |

### Marketing üzenetek (üzenetmagok)
| # | Üzenetmag | Hook lehetőség |
|---|-----------|----------------|
| 1 | [pl. „Rendszert építs, ne appokat gyűjts"] | Meglepő állítás / Probléma-megoldás |
| ... | ... | ... |

### Célcsoport szegmensek
| Avatár | Fő fájdalom | Fő vágy |
|--------|-------------|---------|
| [pl. 1. avatar] | [Nem kap elég ügyfelet] | [Stabil megélhetés] |
| ... | ... | ... |

### Social proof elemek
| Típus | Idézet/szám | Trigger |
|-------|-------------|---------|
| [Testimonial] | [„Két hónap alatt megtérült..."] | Társadalmi bizonyíték |
| ... | ... | ... |

### Ajánlat elemek (ha van)
- Ár: [...]
- Garancia: [...]
- Bónuszok: [...]
```

→ „Ezek az elérhető elemek. Most válasszunk irányt."

**2. lépés: Irány választás**

Kérdezd meg:
- „Melyik üzenetmag(ok)ra fókuszáljunk?" (1-3 kiválasztás)
- „Melyik avatárra célzunk elsősorban?"
- „Melyik awareness szinten vannak? (tudattalan / probléma-tudatos / megoldás-tudatos / termék-tudatos / legtudatosabb)"
- „Van preferenciád a címsor típusra vagy formulára?"

**3. lépés: Eszköz választás**

A felhasználó által választott irány + awareness szint alapján javasolj:

```
## Javasolt megközelítés

**Awareness szint:** [X] → ehhez illik:
- **Címsor típusok:** [2-3 javasolt típus, indoklással]
- **Formulák:** [2-3 javasolt formula, indoklással]
- **Triggerek:** [3-5 javasolt trigger, indoklással]

**Generálási terv:**
- [X] db címsor ([típus elosztás])
- [X] db elsődleges szöveg ([formula elosztás])
```

→ „Stimmel ez az irány, vagy módosítanál?"

**4. lépés: Célzott generálás**

**Sablon betöltés:** Töltsd be CSAK a javasolt típus/formula sablon fájlokat (max 3-4 fájl). Pl. ha PAS + Storyselling formulát javasoltál és Probléma-megoldás + Meglepő állítás címsort, töltsd be: `assets/sablonok/elsodleges-szoveg/pas.md`, `assets/sablonok/elsodleges-szoveg/storyselling.md`, `assets/sablonok/cimsor/problema-megoldas.md`, `assets/sablonok/cimsor/meglepo-allitas.md`.

A jóváhagyott irány alapján generálj 10-20 címsort és/vagy 5-10 elsődleges szöveget. A Szabad módnál kevesebb, de célzottabb output.

Output formátum: ugyanaz mint a Szabad módnál (táblázat + teljes szövegek), de szűkebb típus/formula elosztással.

→ „Melyikeket fejlesszem ki A/B variációkkal?"

---

## 5. Fázis 3: Teljes hirdetés szöveg + Output

### Cél
Kiválasztott szövegekhez teljes hirdetés formátum, A/B variációk, kreatív brief.

**Sablon betöltés:** Ha még nem töltötted be, töltsd be a releváns sablon fájlokat a használt típus/formula alapján. Formula módnál: az elemzésben azonosított típus + formula fájlokat.

### Facebook / Meta formátum

```
**Címsor:** [max 40 kar] ([X] karakter)
**Elsődleges szöveg:**
[Hook-kal indít, max 1000 kar, első 125 kar a legfontosabb]

**Leírás:** [max 30 kar] ([X] karakter)
**CTA gomb:** [típus]
```

### Google Ads formátum

```
**Címsor 1:** [max 30 kar] ([X] karakter)
**Címsor 2:** [max 30 kar] ([X] karakter)
**Címsor 3:** [max 30 kar] ([X] karakter)
**Leírás 1:** [max 90 kar] ([X] karakter)
**Leírás 2:** [max 90 kar] ([X] karakter)
**Display URL:** [ceg-domain]/[útvonal]
```

### TikTok Ads formátum

```
**Hirdetés szöveg:** [max 100 kar] ([X] karakter)
**CTA gomb:** [típus]
```

### A/B variációk

Minden kiválasztott szöveghez 2 variáció:
- **A variáció:** Az eredeti hook/formula
- **B variáció:** Más címsor típus VAGY más formula, valódi alternatíva, nem szó-csere

### Kreatív brief (opcionális)

Ha a felhasználó kéri vagy releváns:

```
### Kreatív brief
**Típus:** Kép / Videó / Carousel
**Vizuál irány:** [leírás: mi legyen rajta]
**Szöveg overlay:** [max 20% felület, kulcsüzenet]
**Hangulat:** [milyen érzést keltsen]
```

### Összesítés + Output

**Sablon:**

```
## [Kampány neve]: Hirdetés szövegek

### Összefoglaló
- **Platform:** [Meta / Google / TikTok / mindegyik]
- **Termék:** [...]
- **Kampány cél:** [...]
- **Mód:** [Formula / Szabad / Vezetett]
- **Hirdetések száma:** [X szöveg, X×2 variáció]

### Típus / formula elosztás

| Címsor típus | Db |
|---|---|
| [típus] | [X] |
| ... | ... |

| Formula | Db |
|---|---|
| [formula] | [X] |
| ... | ... |

---

### Hirdetés 1: [Név]
**Címsor típus:** [típus] | **Formula:** [formula] | **Awareness:** [szint]
**Célcsoport:** [kik]
**Triggerek:** [használt triggerek]

#### A variáció
**Címsor:** [...]
**Elsődleges szöveg:** [...]
**Leírás:** [...]
**CTA gomb:** [...]

#### B variáció
[...]

---
[... minden hirdetés ...]
```

**Mentés:** a fájlba a SKILL.md Mentés sora szerint (`hirdetes/<ajanlat>/<platform>.md`). Notionbe csak akkor, ha a felhasználó kéri: „Tegyem fel a Notion kampány oldalra is?"

**Minden 3-4 hirdetés után:** „Eddig stimmel?"

---

## 6. Minőségi checklist

Minden generált szövegnél ellenőrizd:

- [ ] Hook az első mondatban? (nem köszönéssel indít)
- [ ] Egy hirdetés = egy üzenet = egy CTA?
- [ ] Megszólítás konzisztens (a cég-hang szerint)?
- [ ] Nincs gondolatjel mondat közben?
- [ ] „Nem X, hanem Y" max 1× per szöveg?
- [ ] Karakterlimitek betartva (platform-specifikus)?
- [ ] CTA felelősség-átadás, nem nyomás?
- [ ] Konkrét részletek (számok, nevek)?
- [ ] Awareness szinthez illő megközelítés?
- [ ] A/B variáció valódi alternatíva (más típus/formula)?
- [ ] Tiltott szavak/minták kerülve? (lásd `references/hirdetes-formulak.md`)
