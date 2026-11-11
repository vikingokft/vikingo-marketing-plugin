---
name: landing-szovegiro
description: "Megírja egy landing oldal szövegét a márka-agyból (00-agy/brand/), a 25 landing-recept (L1-L25: letölthető csali, webinár és esemény, kihívás, értékesítési oldal, szolgáltatás) bármelyike szerint: az elején ajánl egy receptet az ajánlat kategóriája szerint, és rákérdez. Blokkonként szabadon ír, a végén a szöveg-emberiesítővel átnézeti, és egy szoveg.md-t ad, amiből a landing-design vagy a landing-epito HTML-t épít. Előfeltétel: a brand-specialista és a termek-specialista felépítette a márka-agyat és az ajánlat mappáját. Akkor használd, ha ezt kérik: 'írd meg a landing oldal szövegét', 'landing szöveg', 'feliratkozó oldal szövege', 'webinár-regisztrációs oldal szövege', 'jöhet a landing szöveg'. Hosszú, sablonos kurzus-sales oldalhoz a sales-oldal-iro, a HTML megépítéséhez a landing-design való."
---

# Landing szövegíró

A márka-agyból (`00-agy/brand/`) megírja egy landing oldal szövegét, **a választott recept** blokkjainak sorrendjében. Mind a 25 receptet ismeri (`references/receptek.md`), és mind a 24 blokkot (`references/blokklista.md`: mindegyiknél ott áll, mi a dolga, melyik mentális kapcsolót nyomja meg, és honnan jön hozzá az anyag). Hogy melyik receptre épül a szöveg, azt az elején megkérdezi.

**A szöveg az első, a forma utána.** Blokkonként úgy írsz, ahogy a gondolat kívánja: annyi mondattal, bekezdéssel, felsorolással, amennyi kell. Hogy ebből milyen designelemek lesznek (kártyák, ikonsorok, oszlopok), azt az építés dönti el, nem te.

Nem épít HTML-t (az a landing-design vagy a landing-epito dolga), a választott recept sorrendjén nem változtat (csak a lent leírt kiegészítésekkel), és nem talál ki tényt.

## 1. Ellenőrzés

1. Keresd meg a márka-agyat (`00-agy/brand/`), a [`../_kozos/marketing-kontextus.md`](../_kozos/marketing-kontextus.md) „Hol él a márka-agy” része szerint. Ha nincs, állj meg, és mondd, hogy előbb a **brand-specialista** építse fel.
2. Melyik ajánlatra készül az oldal? Ha a `00-agy/brand/ajanlatok/` alatt egy mappa van (a `_sablon` nem számít), az. Ha több, kérdezz rá egy mondatban. Ha egy sincs, állj meg, és ajánld a **termek-specialista**-t (csalihoz annak csali módját).
3. Olvasd be az ajánlat mappájából: `_attekintes.md`, `kontextus.md`, `kontextus-elemek.md`, `celcsoport.md`, `versenytarsak.md`, `testimonialok.md`, `kifogasok.md`, `uzenetek.md`, `gyengesegek.md`; a cég-szintről: `markahang.md`, `uzleti-profil.md`, `celcsoport.md`, `csapat.md`, `sztoribank.md`, `arculat.md`. A cég-szintű és az ajánlat-szintű fájl öröklési sorrendje a közös szerződésben van.
4. **A mindig kötelező mag** nélkül nem írsz: a márka és a szakértő neve, a megszólítás, a fő ígéret, a következő lépés (mit tesz a látogató), és eseménynél az időpont. Ha valami hiányzik, sorold fel egy üzenetben, és a válasz a megfelelő agy-fájlba kerül (a közös szerződés hiány-protokollja szerint).

## 2. A recept

Mielőtt írni kezdesz, kérdezd meg, melyik receptre épüljön a szöveg. Ezt akkor is megkérdezed, ha az ajánlat `_attekintes.md`-jében már áll egy recept; ilyenkor azt ajánlod elsőnek.

1. Olvasd el a `references/receptek.md`-t.
2. Döntsd el a kategóriát (A-E) abból, mit tesz a látogató az oldalon (a `kontextus.md` ajánlattípusa és következő lépése alapján).
3. Egy üzenetben kérdezz, ebben a formában:

   > Melyik receptre épüljön a szöveg? A **[kategória]** receptjei:
   > - **L8 · Webinár · hosszú** (a kategória alapoldala, ezt ajánlom): Hero → Problémák → … (a blokkok sora)
   > - **L7 · Webinár · rövid**: …
   > - …
   >
   > Az ajánlásom: **[recept]**, mert [egy mondat a látogató hőfokáról és a döntés méretéről, a márka-agy alapján]. Ha másik kategória receptje kell, vagy bármelyik másik (L1-L25), írd meg a számát.

   Az ajánlott recept az `_attekintes.md`-ben álló, ha van; ha nincs, a kategória alapoldala (L3, L8, L12, L16, L1), hacsak a receptek.md kategória-táblája mást nem mond (például hideg forgalom és kis döntés: a rövid recept). **Ha az `_attekintes.md`-ben már a végleges, kiegészített blokksor áll, az ajánlott receptnél azt írd ki, ne a receptek.md nyers sorát**, és egy félmondatban mondd meg, melyik blokk jött a kiegészítésből; a többi recept sora maradhat nyers.
4. Várd meg a választ. Ha a felhasználó azt mondja, „mindegy” vagy „válassz te”, az ajánlottal mész tovább, és ezt kimondod.
5. A választott recept blokksora lesz a szöveg váza. Alkalmazd a receptek.md **kiegészítéseit**, ha az ajánlatra illenek (fizetős esemény, helyszíni esemény, ismétlődő esemény, fizikai termék): ezek blokkot tehetnek hozzá vagy kötelezővé tehetnek. Mondd ki egy mondatban, milyen kiegészítést alkalmaztál.
6. **Az anyag a választott receptre:** nézd át, hogy a recept blokkjaihoz (például Árak, Garancia, Bónuszok, Limitek) megvan-e az anyag a márka-agyban (a blokklista „Anyag” sora mondja meg, hol keresd). Ami hiányzik, azt az írás előtt sorold fel, és kérdezd meg: pótolja most (a válasz a megfelelő agy-fájlba kerül), vagy a blokk `[KITÖLTENDŐ]` / `Kimarad` jelöléssel készüljön.
7. A végleges blokksort (a kiegészítésekkel) írd be az ajánlat `_attekintes.md`-jébe egy „Landing oldal” sorba (recept és blokksor), hogy a következő futás és az építő skill is lássa.

## 3. Írás

Olvasd el a `references/szabalyok.md`-t, a `references/blokklista.md`-t és a `references/cimsorok.md`-t, és nézd meg a `markahang.md` szövegmintáit. Aztán írd meg a szöveget blokkonként, sorrendben.

- **Előbb gondold végig az egészet.** Mi az az egy gondolat, amit az oldal elad, és hogyan vezeti végig rajta az olvasót a recept íve? A formula szerinti receptek (PAS, BAB, AIDA, QUEST, 4P, ACCA, StoryBrand) íve a nevükben van: ezt kövesd. A blokkok egy gondolatmenet részei, nem különálló dobozok: egymásra épülnek, és nem ismétlik egymást.
- **Minden blokknál** a blokklista „dolga” és „kapcsoló” sora az irány, a recept zárójeles megjegyzése (például „napi bontás”, „benne űrlap”, „értékösszesítő”) a pontosítás, a „fogás” egy ötlet, amit használhatsz. Az „anyag” sor mondja meg, melyik fájlban keresd a tényeket.
- **Címsorok:** a blokk szövege után írd meg őket, a `cimsorok.md` szerint: blokkonként a minta, felvezető csak ritkán, rövid címkeként, a Hero és a CTA címsorához 4-6 jelöltből választva, a végén az ellenőrző kérdésekkel.
- **Elhagyható (✱) blokk:** ha nincs hozzá valódi anyag (vélemény, eset, logó, valódi határidő, garancia), a blokk egyetlen sora: `Kimarad: nincs anyag (…).`
- **Kétszer álló blokk** (Limitek, Visszajelzések, CTA szakasz): mindkettő külön blokk a saját sorszámával, más szereppel (a blokklista „fogás” sora szerint). A második ne ismételje az elsőt.
- **Ha egy blokknak nincs saját tartalma,** mert minden, amit mondana, egy másik blokkban már elhangzott (egyszerű szolgáltatásnál gyakori), ne ismételd más szavakkal. Két út közül választhatsz:
  - **kihagyod**, és a blokk egyetlen sora: `Kimarad: nincs saját tartalma (…).` Ezt a nem ✱-os blokkokra is megteheted;
  - **kutatsz hozzá** (a témában, a versenytársak oldalain, a vásárlók kérdéseiben), és amit találsz, forrással beírod a `00-agy/brand/` megfelelő fájljába, `(piaci hang)` vagy `(következtetés, erősítsd meg)` jelöléssel, aztán abból írod meg a blokkot.
  Az átadásban mondd el, melyiket választottad, és miért.
- **Ha egy tény hiányzik,** de a blokk enélkül is megírható, írd meg nélküle, és a hiányt sorold fel az átadásban. Ha nélküle nem írható meg, a helyére `[KITÖLTENDŐ: mi hiányzik]` kerül.

**Mentés:** `<LANDING>/szoveg.md`. A `<LANDING>` a közös [kimeneti-hely szabály](../_kozos/marketing-kontextus.md#hova-kerül-a-kész-anyag) helye a `landing` típusra: önállóan `kimenetek/landing/<ajanlat>`, AI-oprendszerben `03-projektek/<projekt>/landing/<ajanlat>` (vagy a birtokló terület). Az `<ajanlat>` az ajánlat mappájának neve. Ugyanezt a `<LANDING>`-et használja a `landing-design`, a `landing-epito` és a `landing-elesites` is, így a skillek egymás fájljait találják. Ha már van `szoveg.md`, a régit nevezd át `szoveg-elozo-ÉÉÉÉ-HH-NN.md`-re. A formája:

```markdown
---
cim: <az oldal címe>
recept: <a választott recept, például L8 · Webinár · hosszú>
ajanlat: <az ajánlat mappájának neve>
---

# <az oldal címe>

## 1. Hero

### <a blokk címsora>

<a blokk szövege, szabadon: bekezdések, felsorolás, gombszöveg, ahogy a gondolat kívánja>

## 2. Problémák és következményeik

…
```

Néhány szokás kötött, mert ezek segítik az építést:

- a blokk címsora `###` (a logósornak nem kell); ha ritkán felvezető is kell, az a címsor fölött áll: `**Felvezető:** …`;
- ha a blokk felsorol (problémák, lépések, kérdések), az Markdown-lista legyen;
- a gomb, az űrlap és a jelölőnégyzet így áll:

  ```markdown
  **Gomb:** Kérem a helyem
  **Űrlap:** Keresztnév, E-mail-cím
  **Jelölőnégyzet:** Elolvastam és elfogadom az adatkezelési tájékoztatót.
  ```

- ha egy link még hiányzik (például az adatkezelési tájékoztatóé), a szöveg marad, és utána külön áll a jelölés: `… adatkezelési tájékoztatót. [KITÖLTENDŐ: az adatkezelési tájékoztató linkje]`. Linkbe ne tedd a jelölést (`[szöveg]([KITÖLTENDŐ])`), mert az építő ellenőrzője azt hibás linknek veszi;
- a blokkok `##` címsora sorszám és pontosan a blokklista neve, a `✱` jel és a recept zárójeles megjegyzése nélkül (a recept „CTA + űrlap” és „CTA” blokkja: `CTA szakasz`; a „Problémák”: `Problémák és következményeik`; a „Termékjellemzők”: `Termékjellemzők, funkciók`);
- a kiegészítéssel hozzáadott blokk ugyanígy, a helyén;
- az összehasonlító táblázat Markdown-tábla, a galéria képei `**Kép:** …` sorok.

Ha kész, futtasd az ellenőrzést (a skill gyökere az a mappa, amelyikben ez a `SKILL.md` van):

```bash
python3 "<a skill gyökere>/scripts/ellenoriz.py" <LANDING>/szoveg.md
```

A szkript a fejléc `recept:` sorából keresi ki a receptet, és megnézi, hogy a blokkjai megvannak-e sorrendben; a kiegészítéssel hozzáadott blokkot „plusz blokknak” jelzi, ezeket nézd át.

## 4. Emberiesítés

Futtasd a **szöveg-emberiesítő** skillt a `szoveg.md`-n: cél-felület landing oldal, hang-forrás a `00-agy/brand/markahang.md`, normál szigorúság, a futás-mappája a `<LANDING>/emberiesites/`. Ennek a pluginnak a saját `szoveg-emberiesito`-ját használd (Claude-ban `vikingo-marketing-plugin:szoveg-emberiesito`), mert egy AI-oprendszerben lehet azonos nevű skill is, és az nem ismeri a `--landing` módot. A scanner közvetlen útja a skill mappájához képest `../szoveg-emberiesito/scripts/scan.py`:

```bash
python3 "<a skill gyökere>/../szoveg-emberiesito/scripts/scan.py" --landing <LANDING>/szoveg.md
```

Mondd meg neki, hogy a véleményeket és a vásárló idézőjeles mondatait ne írja át, a `##` blokk-címsorokhoz, a `[KITÖLTENDŐ: …]` helyekhez és a `**Felvezető:**`, `**Gomb:**`, `**Űrlap:**`, `**Jelölőnégyzet:**`, `**Kép:**` jelölésekhez ne nyúljon, és a scannert `--landing` kapcsolóval futtassa (így a listacímkéket és a GYIK-kérdéseket sem jelzi; az 1-es kilépési kód csak azt jelenti, hogy van jelölt). A záró átírás a `szoveg.md`-be kerül vissza; külön végleges fájl nincs.

Ha a szöveg-emberiesítő nincs telepítve, olvasd végig a szöveget a `szabalyok.md` 9. pontja szerint, és írd át, ami fordításnak hangzik.

Utána futtasd újra az ellenőrzést.

## 5. Végső ellenőrzés

Olvasd végig a kész `szoveg.md`-t, és válaszolj igennel vagy nemmel:

1. A Hero után tudja az olvasó, mi ez, kinek szól, és mit kap?
2. A CTA szakasz a Hero ígéretét adja vissza?
3. Minden szám, név, vélemény, ár és határidő a `00-agy/brand/`-ből jön, vagy `[KITÖLTENDŐ]` áll a helyén?
4. Semmi nem lépi át a `markahang.md` „Amit soha nem állítunk” és „A mi tiltott szavaink” részét, sem az ajánlat `gyengesegek.md`-jében leírt korlátokat?
5. A jellemzők mellett ott van, mit nyer vele az olvasó?
6. A címsorok mondanak valamit, nem csak a blokk nevét (kivéve a funkcionális blokkokat)?
7. Hangosan felolvasva úgy szól, mint a `markahang.md` mintái?
8. A szöveg a választott recept íve szerint halad (a formula receptjeinél a formula lépései felismerhetők), és a kétszer álló blokkok nem ismétlik egymást?

Ahol nem, javítsd. Ha a javításhoz adat kell, ami nincs a `00-agy/brand/`-ben, az átadásba írd.

## 6. Átadás

Rövid összefoglaló a felhasználónak:

- hol a `szoveg.md`, melyik receptre épült (és milyen kiegészítéssel), és hogy ebből dolgozik a landing-design (vagy a landing-epito);
- melyik blokk maradt ki, és miért; hol maradt `[KITÖLTENDŐ]`;
- **amit érdemes átnéznie:** a jelölt (például `(következtetés, erősítsd meg)`, `(piaci hang)`) vagy következtetett adatból írt részeket, a kihagyott kockázatos állításokat, és ha a `00-agy/brand/` fájljai ellentmondtak egymásnak;
- az emberiesítő mérésének két-három sora.

Kérd meg, hogy olvassa végig a szöveget hangosan: ő ismeri a piacát, a vevőit és az ajánlatát, itt tud a legtöbbet hozzáadni.

## Ha új változatot kérnek

Alapból egy változatot írsz. Csak akkor írsz többet, ha kérik.

**Egy-két blokk új változatban:**
1. Olvasd be a `00-agy/brand/`-et és a kész `szoveg.md`-t, hogy a többi blokkot ismerd, és ne ismételd őket.
2. Írd meg a kért blokkot 2-3 változatban, mindegyiket más irányból (például az egyik a problémából, a másik az eredményből indul; a címsor más-más típusból a `cimsorok.md` szerint).
3. A változatok a `<LANDING>/valtozatok/<blokk>-ÉÉÉÉ-HH-NN.md` fájlba kerülnek; a `szoveg.md`-hez ne nyúlj.
4. Emberiesítés csak az új szövegeken; a végső ellenőrzésből csak a blokkra vonatkozó kérdések (ha a Hero vagy a CTA változik, a 2. kérdés is).
5. Add át egymás mellett, változatonként egy mondattal, miben más. Ha a felhasználó választott, cseréld be a `szoveg.md`-be (előtte mentsd el a régit `szoveg-elozo-ÉÉÉÉ-HH-NN.md` néven), és futtasd az ellenőrző szkriptet.

**Az egész oldal új változatban:** kérdezd meg egy mondatban, miben legyen más (fő gondolat, hangnem, hossz, célcsoport, vagy másik recept). Ha nem mond semmit, válassz más fő gondolatot, mint az elsőnél. Futtasd a 3-6. lépést (az 1. kimaradhat, ha az agy nem változott; a 2. csak akkor kell, ha más receptre kéri); a kimenet `szoveg-b.md`, az első megmarad. Az átadásban két mondatban írd le, miben más a két változat.

## Kapcsolódó skillek

- **brand-specialista** és **termek-specialista:** felépítik a márka-agyat és az ajánlat mappáját, amiből ez a skill dolgozik.
- **szoveg-emberiesito:** a 4. lépésben átnézi a szöveget.
- **landing-design:** a `szoveg.md`-ből és a tetsző oldalakból (inspirációból) megtervezi és megépíti az oldalt. A **landing-epito** a régebbi, mintaoldalakból dolgozó építő; bármelyik jó.
- **landing-elesites:** a kész oldalt FTP-re és WordPressbe csomagolja.
