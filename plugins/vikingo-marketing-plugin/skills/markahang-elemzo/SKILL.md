---
name: markahang-elemzo
description: "Márkahang elemzése szövegminták alapján. Két üzemmód: Cég-mód (`00-agy/brand/markahang.md` frissítése I-II-III struktúrában) és Külső mód (új markahang.md sablon más cégnek 1. + 2.1–2.5 struktúrában). Mér: 8 hangnem dimenzió 10-es skálán, szókincs-kategóriák, mondatszerkezet, retorikai eszközök, anti-minták. Akkor használd, ha a felhasználó ezt mondja: 'márkahang', 'markahang', 'hangnem elemzés', 'márkahang guide', 'brand voice', 'írásstílus elemzés', 'voice profile', vagy egy cég szövegmintáit hozza elemzésre."
---

# Márkahang Elemző

Szövegmintákat elemzel, és vagy a cég saját szövegírási guide-ját tartod karban, vagy más cégeknek készítesz `00-agy/brand/markahang.md` sablont. Belső kontextus-karbantartó skill.

## Két üzemmód

### Cég-mód — saját guide frissítése
Új szövegminták elemzése → a cég márkahang-guide-jának (ha van, pl. `00-agy/brand/markahang.md`) finomhangolása az **I-II-III struktúrában**. Ha még nincs guide, ez a mód az első verziót állítja fel a mintákból:
- **I. Alapelvek** (Ki ír, Hang, Tartalom-elvek, Lélek, Mondatszerkezet, Történetmesélés)
- **II. Mit ne** (Tiltott nyitások, Központozás, „Nem X hanem Y", AI-drama stb.)
- **III. Helyzetek** (Email, Sales-oldal, Lecke, Hirdetés / videoszkript, Ügyfélszolgálati, Prezentáció)

### Külső mód — új sablon más cégnek
Más cég szövegmintáit elemzed → új `00-agy/brand/markahang.md` sablon a **1. + 2.1–2.5 struktúrában**. Output helyét a felhasználó adja meg (pl. egy projekt-mappa); ha nem ad meg, kérdezd meg, hova mentsd.

Az `assets/markahang-md-sablon.md` a kitölthető váz a Külső módhoz.

## Bemenet és kimenet

Ez a skill **az agyat tölti fel**: nyers anyagból kanonikus fájlt ír. A szerződés: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md).

| | |
|---|---|
| **Nyersanyag** | Szövegminták: e-mail, poszt, sales-oldal, videó-átirat; a felhasználó illeszti be, vagy a `01-nyers/`-ben van |
| **Ezt írja** | `00-agy/brand/markahang.md` (Cég-mód), vagy egy külső cég sablonja a megadott projekt-mappában (Külső mód) |
| **Erre támaszkodik** | a meglévő `markahang.md` viszonyítási alapnak: anti-minták, csatorna-alapértékek, szókincs |

Ez az a család, amelyik kérdezhet és kutathat. De előbb mindig nézd meg, mi van már a kanonikus fájlban: azt erősítsd meg, ne kérdezd újra. Amit megírsz, az a fájlba kerül, nem csak a beszélgetésbe.

A Külső módhoz az `assets/markahang-md-sablon.md` a kitölthető váz. A `references/` fájljait csak akkor olvasd, amikor az adott fázis igényli.

---

## A 8 hangnem dimenzió

Minden dimenzió 1-10 skálán mérhető. Konkrét szövegbeli idézet kötelező az értékhez.

**Anti-fabrikáció (főleg Külső mód):** ha NINCS valódi szövegminta a vizsgált cégtől, a dimenzió-táblát NE töltsd ki kitalált idézetekkel. Helyette: hagyd a bizonyíték-cellát „nincs minta — pontosítandó" jelzéssel, a dimenzió-értéket pedig jelöld becsültként (pl. `7?`). Kitalált idézet pontszám alá tilos, mert sérti az idézet-alapú elvet. Inkább kérj több mintát.

| Dimenzió | 1 (alacsony) | 5 (közepes) | 10 (magas) | Mit keress |
|---|---|---|---|---|
| **Közvetlenség** | Kertelős | Strukturált | Nulla kertelés | Mondathossz, hányadik mondatban jut a lényegre |
| **Őszinteség** | Csak pozitívumok | Néhány korlát | Hibák, önző motivációk, kudarcok | „bevallom", „őszintén", önkritika |
| **Humor** | Nulla | Néha | Gyakori, kreatív | Zárójeles kommentár, „na jó", absurd |
| **Lelkesedés** | Monoton | Visszafogott | Túlfűtött | Erősítők, felkiáltások, jelzők |
| **Nyomásgyakorlás** | Csak informál | Emlékeztet | Erős sürgetés | Határidők, scarcity, FOMO |
| **Formalitás** | Szleng | Köznyelvi | Hivatalos | Megszólítás, szóválasztás |
| **Sebezhetőség** | Mindig erős | Néha emberi | Nyíltan megosztja | Küzdelmek, félelmek |
| **Biztonságérzet** | Kihívás-fókusz | Egyensúly | Folyamatos megnyugtatás | „ne aggódj", „ez normális" |

### Csatorna-specifikus alap-értékek (cég-referencia)

A cég `00-agy/brand/markahang.md`-jéből kiolvasott alap-tónus csatornánként. Az alábbi tábla a kitöltendő váz — a konkrét számokat a cég saját szövegmintáiból mérd be.

| Dimenzió | Alap | Email | Videó | Edukáció | Sales |
|---|---|---|---|---|---|
| Közvetlenség | [X] | [X] | [X] | [X] | [X] |
| Őszinteség | [X] | — | — | — | — |
| Humor | [X] | [X] | [X] | [X] | [X] |
| Lelkesedés | [X] | [X] | [X] | [X] | [X] |
| Nyomásgyakorlás | [X] | [X] | [X] | [X] | [X] |
| Formalitás | [X] | — | — | — | — |
| Sebezhetőség | [X] | [X] | — | [X] | [X] |
| Biztonságérzet | [X] | [X] | — | [X] | [X] |

(`—` = a csatorna nem definiálja külön, az alapérték örökölődik.)

Cég-módban ezek a viszonyítási értékek. Külső módban az új cég szövegmintáiból mérsz, és az ő alap-értékeit építed be a sablonba.

---

## Indulás előtt

### 1. Üzemmód-választás
„Cég-mód (saját guide frissítése) vagy Külső mód (új cégnek sablon)?"

### 2a. Cég-mód esetén
- Ha van márkahang-guide (pl. `00-agy/brand/markahang.md`), olvasd be. Ha nincs, jelezd: az elemzés a beillesztett mintákból építi fel az alap-tónust, és az eredményt felajánlhatjuk egy új guide első verziójának.
- Ha van guide: kérdezd „Melyik szekciót finomítjuk?" (III. Email / Sales-oldal / Lecke / Hirdetés / Ügyfélszolgálati / Prezentáció / I. Alapelvek / II. Mit ne), és jelezd a jelenlegi állapotot röviden.
- Kérd a szövegmintákat (minél több, annál pontosabb)

### 2b. Külső mód esetén
- Kérdezd: „Melyik cégnek készítjük a sablont?" (név + opc. URL)
- Kérdezd: „Milyen szövegmintáid vannak?" (weboldal, email, social, hirdetés, videó átirat, sales)
- Kérdezd: „Hova mentsem az output-ot?" (egy projekt-mappa `00-agy/brand/markahang.md`-je)

### 3. Korpusz áttekintés
Számold meg: hány szöveg, milyen típusok, hozzávetőleges szómennyiség, időszak. Ha 10+ szöveg jön, jelezd: „X szövegmintát kaptam. Elemzem mindegyiket."

---

## Workflow

### Fázis 1 — Autonóm elemzés

Minden szövegmintát (vagy az összest aggregáltan) elemzed 5 dimenzió mentén:

1. **8 hangnem dimenzió pontozása** — minden dimenzióhoz konkrét idézet
2. **Szókincs elemzés** — lásd `references/voice-profiling.md` (kategóriák: erősítők, köznyelvi, átmeneti, őszinteség-jelzők stb.)
3. **Mondatszerkezet és ritmus** — átlag mondathossz, bekezdés hossz, ritmus-minta, kiemelések
4. **Retorikai eszközök** — Hook-Story-Pitch, sztori, ellentétpárok, relativizálás, paradox CTA, zárójelezés
5. **Anti-minta keresés** — két külön kör, ne keverd őket. Az **univerzális** AI-reflexeket a `szoveg-emberiesito` méri: futtasd rá a mintát a [`../szoveg-emberiesito/scripts/scan.py`](../szoveg-emberiesito/scripts/scan.py)-jal (a skill mappájához képest), és a [`szoveg-emberiesito/references/patterns.md`](../szoveg-emberiesito/references/patterns.md) szerint olvasd. A **cégspecifikus** anti-mintákat Cég-módban a `markahang.md` II. Mit ne fejezete adja (ha van kitöltve) — az csak arról szól, ami *nálunk* tilos. Külső módban cégspecifikus lista nincs, tehát ott csak az emberiesítő fut.

**Output formátum (Fázis 1):**

```
🔍 Szövegminta elemzés: [csatorna/forrás]
**Minták száma:** X ([típus])
**Összes szómennyiség:** ~ X szó

### Hangnem profil
| Dimenzió | Mért | Cég-alap | Eltérés |
|---|---|---|---|
| Közvetlenség | X/10 | Y/10 | [+/-Z] |
| ... | ... | ... | ... |

### Szókincs
**Új szavak/kifejezések (a guide-ban nincsenek):**
- „[szó]": X× előfordulás, kontextus: [hogyan használja]

**Leggyakoribb átmeneti kifejezések:**
- [szó]: X× | [szó]: X×

### Mondatszerkezet
- Átlag mondathossz: X szó
- Bekezdés: Y% 1 soros, Z% 2 soros, ...
- Ritmus: [jellemzés]

### Retorikai eszközök
- [eszköz]: [példa]

### Anti-minták
- [ha van: mi és hol]
- [ha nincs: „Nem találtam anti-mintát."]
```

A csatorna-specifikus mélyítéshez (Email-specifikus tárgysor-elemzés, Videó-specifikus hook, stb.) lásd `references/csatorna-szempontok.md`.

### Fázis 2 — Összehasonlítás vagy szintézis

**Cég-módban:** ha van guide, vesd össze a Fázis 1 eredményét a guide aktuális tartalmával (a kiválasztott szekcióval). Ha nincs guide, a Fázis 1 mért profilja maga a javaslat egy új guide első verziójához:

```
📊 Összehasonlítás: [szekció] jelenlegi vs. új minták

### Szókincs változások
**Új szavak (hozzáadás javasolt):**
- „[szó]": X× előfordulás. Javaslat: [hol vegyük be]

**Erősödő minták:** [már a guide-ban, de nagyobb súly]
**Gyengülő minták:** [a guide-ban van, de ritkábban]

### Javaslat
A guide [szekció] szekciójában frissíteném:
1. [konkrét változtatás]
2. ...
```

Ha még nincs guide, a „Javaslat" rész helyett az új guide első vázát ajánld fel (I-II-III struktúra a mért profilból).

**Külső módban:** szintetizálj egy `00-agy/brand/markahang.md` sablont az `assets/markahang-md-sablon.md` váza alapján. A struktúra: **1. Alap-elvek + 2.1 Edukáció + 2.2 Hirdetés-videó + 2.3 Email + 2.4 Sales + 2.5 Social.** Csak azokat az alfejezeteket töltsd ki, amelyikre van minta — a többit „alfejezet készenlétben — minta hiányzik" jelzéssel hagyd.

A részletes Külső mód keretrendszer (pozicionálás, megszólítás, értékígéret stílusa, differenciáló elem) a `references/kulso-mod-keretrendszer.md`-ban.

### Fázis 3 — Output + jóváhagyás

1. Mutasd meg az összehasonlítás vagy szintézis eredményét + javaslatokat
2. Kérdezd: „Stimmelnek a javaslatok? Mit vegyünk be, mit ne?"
3. Ha jóváhagyja:
   - **Cég-mód:** frissítsd a meglévő guide-ot a kiválasztott szekcióban; ha nem volt guide, hozd létre az elsőt a felhasználó által megadott helyen
   - **Külső mód:** mentsd az új `00-agy/brand/markahang.md`-t a target helyre
4. Jelezd: „A [fájl] frissítve / létrehozva: [röviden mit változtattál]"
5. Kérdezd: „Van még szövegminta amit elemezzünk?"

---

## Speciális módok

### Batch mód
Több csatornához egyszerre jött minta:
1. Fázis 0: csatornák azonosítása
2. Fázis 1: csatornánként külön elemzés, egy összefoglalóban
3. Fázis 2: csatornánkénti összehasonlítás
4. Fázis 3: összesített javaslatok → jóváhagyás → fájlonkénti frissítés

### Social media mód
Ha a cég guide-ja **nem** tartalmaz Social szekciót (vagy nincs guide), és social szöveget elemzünk Cég-módban:

1. **Új III. Social szekció létrehozása** — ha a felhasználó jóváhagyja
2. **Vagy átadás** a `social-tartalom-tervezo` skillnek — Fázis 1 outputja kontextus lesz

Külső módban a Social szekció a 2.5-be kerül (a sablon-struktúrában szerepel).

---

## Markahang-fájl frissítési szabályok

### Mit szabad frissíteni
- **Dimenzió-értékek** — ha 10+ szöveg konzisztens eltérést mutat
- **Szókincs-listák** — új ismétlődő szó/kifejezés
- **Típus-eloszlások** — pl. hook-típusok arányai
- **Új szekció** — ha új minta jelent meg
- **Anti-minták** — új kerülendő

### Mit NE frissíts
- **Alap identitás** (ki vagyok, szerepem) — ritkán változik, külön döntés
- **Formázási szabályok** (emoji, gondolatjel stb.) — rögzítettek
- **Referencia-statisztikák** — konkrét elemzések eredményei, nem becslések

### Formátum-szabály
A meglévő struktúrát és formátumot kövesd. Tábla-formátum, szekció-sorrend, „Utolsó frissítés" fejléc. Miért: a guide több session-ön át épül, a konzisztens forma teszi diffelhetővé és követhetővé.

---

## Minőségi checklist (átadás előtt)

- [ ] Mind a 8 dimenzió pontozva van, idézettel?
- [ ] A szókincs elemzés kategorizált (nem ömlesztett lista)?
- [ ] Van mondatszerkezet elemzés (mondathossz, bekezdés, ritmus)?
- [ ] Az anti-minták **mind a két körben** ellenőrizve: az emberiesítő lefutott, és Cég-módban a `markahang.md` II. Mit ne is átnézve (ha ki van töltve)?
- [ ] A javaslatok KONKRÉTAK? (nem „frissítsd a szókincset", hanem „a 'sajnos' szót add a III. Email átmeneti kifejezések közé")
- [ ] Ha van guide: a jelenlegi tartalommal való összehasonlítás megtörtént (nem csak az új mintát elemzed, hanem a különbséget)? Ha nincs guide: a mért profil önmagában teljes?

---

## Referenciák (csak amikor kell)

- `references/voice-profiling.md` — szókincs-kategóriák, mondatszerkezet-mérés, retorikai eszközök részletesen
- `references/csatorna-szempontok.md` — 5 csatorna-specifikus elemzési szempont (Email, Hirdetés-videó, Edukáció, Sales, Social)
- `references/kulso-mod-keretrendszer.md` — Külső hang elemzés (pozicionálás, megszólítás, értékígéret, differenciáló) + output-formátum
- `assets/markahang-md-sablon.md` — a `00-agy/brand/markahang.md` kitölthető váz a Külső módhoz
- A cég márkahang-guide-ja (pl. `00-agy/brand/markahang.md`) — ha létezik, Cég-módban viszonyítási alap

## Stílus

- A cég márkahang-guide-ja szerint, ha van; alapesetben magyar nyelven, ékezetekkel.
- Az író-output is a márkahang szabályai alá esik, akkor is, ha épp a márkahang-elvet magyarázod.
- Az elemzés objektív, idézet-alapú, ne „úgy érzem"-mondatok.
- Fázisonként várd meg a felhasználói választ.

---

## Önellenőrzés kiadás előtt

Futtasd le a hat közös pontot a saját outputodon — gondolatjel, „Nem X, hanem Y", üres szuperlatívusz, kitöltetlen helyőrző, kitalált adat, csonka output —, a [`marketing-kontextus.md` § Kiadás előtti önellenőrzés](../_kozos/marketing-kontextus.md#kiadás-előtti-önellenőrzés) szerint.

Ezen felül, erre a skillre:

- [ ] Nincs kitalált idézet vagy szám pontszám alatt. Valós minta híján „nincs minta — pontosítandó" jelölés vagy becsült érték (`7?`) szerepel.
- [ ] A dimenzió-táblák `[X]` vázát vagy beméred, vagy jelölöd, hogy minta hiányzik; nyersen nem hagyod.

Ha bármelyik bukik, írd át, mielőtt átadod.

