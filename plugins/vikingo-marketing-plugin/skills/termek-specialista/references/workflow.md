# Termék Specialista — Munkamenet

> Szakaszonkénti útmutató a termék-kontextus felépítéséhez. Magas automatizáció: az input-anyagokból ~60% auto-deriválható, a cég-szintű kontextusból további ~25%. A felhasználótól maximum 5 rövid válasz kell.
>
> Ez útmutató, nem merev script. Ha az input-anyag bőséges, szakaszokat összevonhatsz. A cél: a végén az ajánlat-mappa fájljai (a SKILL.md „Ezt írja” sora) ki legyenek töltve, és ne kérdezz olyat, ami az anyagokban már benne van.

## Tartalom

1. [Márkahang és formázás](#márkahang-és-formázás)
2. [Szakasz 0 — Betöltés + automatikus elemzés](#szakasz-0--betöltés--automatikus-elemzés)
3. [Szakasz 1 — Hiánypótlás](#szakasz-1--hiánypótlás)
4. [Szakasz 2 — Célcsoportok + marketing-üzenetek](#szakasz-2--célcsoportok--marketing-üzenetek)
5. [Szakasz 3 — Fájlok összeállítása + jóváhagyás](#szakasz-3--fájlok-összeállítása--jóváhagyás)
6. [Input-anyag parszolási szabályok](#input-anyag-parszolási-szabályok)
7. [Célcsoport deriválási logika](#célcsoport-deriválási-logika)

---

## Márkahang és formázás

Minden generált szövegben (output, sablon-kitöltés, javaslat) kövesd a `00-agy/brand/markahang.md` I. Alapelvek és II. Mit ne fejezetét. Ha ezek még `KITÖLTENDŐ`-k, kérdezd meg röviden a hangnemet (tegezés vagy magázás, stílus), írd be a `markahang.md`-be, és tartsd magad az alábbi alap-elvekhez:

- **Gondolatjel (– vagy —) mondat közben:** ne használd, mert a magyar szövegben ez az AI-írás egyik legfeltűnőbb jele. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra. (Listában OK: `**Fogalom** — magyarázat`.)
- **Tegezés / magázás:** ahogy a márkahang-szabály előírja (vagy ahogy a felhasználó kéri; default: tegezés).
- **Szókincs:** ha van szabálykönyv, annak I. Alapelvek bekezdéseit kövesd, kerüld a II. Mit ne anti-mintáit. Egyébként természetes, közvetlen szakmai hang.
- **Mondatszerkezet:** természetes ritmus, néhol tömör, néhol kifejtett. Max 3-4 sor / bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan csiszolt mondatokat, üres töltelékeket.
- **„Nem X, hanem Y" tiltás:** az AI leggyakoribb szerkezete. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi funkciója van. Helyettesítés:
  - **Töröld az első felet.** Ha a „hanem" utáni rész önmagában megáll, a tagadó fél felesleges.
  - **Kezdd a lényeggel.** „Nem több funkció kell, hanem rendszer." → „Egy működő rendszer kell."
  - **Két külön mondat.** „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** „A kérdés: használod-e egyáltalán?"

---

## Szakasz 0 — Betöltés + automatikus elemzés

### Cél
Betölteni a termék input-anyagait és minden elérhető kontextust, majd automatikusan kinyerni amit lehet, kérdések nélkül.

### Lépések

1. **Termék kiválasztás:** „Melyik termék kontextusát építjük fel?"
   - Ha a felhasználó megnevezi → nézd meg a portfólióban (`00-agy/brand/ajanlatok/_attekintes.md`).
   - Ha nem egyértelmű → mutasd a portfóliót (üres vagy részleges ajánlatok).

2. **Kontextus-betöltés (néma, csak jelezd mit töltesz be):** a SKILL.md `## Bemenet és kimenet` szakasza szerint — a márkahang, a cég-szintű brand-fájlok, a meglévő termék-mappa és az input-anyagok. Ami hiányzik, azt a Szakasz 1 hiánypótló kérdéseiből töltöd fel, és a válasz a termék kanonikus fájljába kerül.

3. **Automatikus elemzés (kérdések nélkül):**

   **a) Tartalmi struktúra parszolása:**
   - Tartalmi egységek azonosítása (modulok, fejezetek, fázisok, részek a fejléc-mintázat alapján).
   - Egységek számolása.
   - Tartalom-típus megállapítása (videó, szöveg, gyakorlat, sablon, kvíz, élő konzultáció).
   - Mellékletek, sablonok kinyerése (hivatkozások a szövegekben).

   **b) Tartalmi elemzés:**
   - Kulcskifejezések kinyerése (top 20: szakszavak, ismétlődő fogalmak).
   - Fő téma azonosítása (miről szól a termék, milyen szintű).
   - Termék célja / fő ígérete (a bevezetőből vagy összefoglalóból).
   - Előfeltételek (bevezető hivatkozásai, első egység tartalma).
   - Before–After (mit tud / hol van a vevő az elején vs. a végén).

   **c) Avatar-párosítás:**
   Ha vannak cég-szintű alap avatarok, közülük kiválasztod a legrelevánsabb 3-5-öt (termék-téma × avatar foglalkozás/célok). Ha az avatar-profilok még nincsenek meg (nincs vagy üres `celcsoport.md`) → ne állj le: a termék-anyagból és a felhasználó válaszaiból javasolj 2-3 célcsoportot, és jelezd, hogy ezeket később egy alap avatar-elemzéssel érdemes megerősíteni / mélyíteni.

   **d) Értékpiramis-javaslat:**
   A `references/modszertan.md` 30 eleméből válaszd ki a relevánsakat. Tipikus kiindulás:
   - Funkcionális: Oktat/tájékoztat, Időt takarít meg, Egyszerűsít, Rendszerez.
   - Érzelmi: Szorongás csökkentése, Vonzóvá tesz, Hozzáférést biztosít.
   - Életet megváltoztató: Motivációt ad, Önmegvalósítás, Tartozni valamihez.

   A piramis-elemek címkéit a `00-agy/brand/markahang.md` tiltólistájához igazítsd. Ne másold be a címkét idegen nyelven vagy tiltott regiszterben (pl. egy „Jó közérzet" elem ne kerüljön „Wellness" néven egy wellness-kerülő brand fájljába).

4. **Output a felhasználónak:**

```
📋 Automatikus elemzés: [Termék neve]

✅ Kinyertem:
- [X] tartalmi egység, [Y] szekció
- Egységek: [Egység 1 neve], [Egység 2 neve], ...
- Tartalom: [pl. videó + szöveg + mellékletek]
- Fő téma: [rövid összefoglaló]
- Kulcskifejezések: [top 10]

🎯 Javasolt célcsoportok (az alap avatarokból):
1. [Avatar neve]: [miért passzol, 1 mondat]
2. [Avatar neve]: [miért passzol]
3. [Avatar neve]: [miért passzol]
(4-5. ha releváns)

📊 Javasolt értékpiramis:
- Funkcionális: [elem1], [elem2], [elem3]
- Érzelmi: [elem1], [elem2]
- Életet megváltoztató: [elem1]

❓ Amire szükségem van (max 5 kérdés):
1. ...
```

Ha a felhasználó kampány-szöget is jelez (pl. „karrierváltás", „mellékjövedelem", „időmegtakarítás"), jegyezd fel — a célcsoportokat és a kontextus-elemeket ehhez a szöghöz élesítsd. Egy termék több kampány-szöghöz külön kontextust kaphat.

---

## Szakasz 1 — Hiánypótlás

### Cél
Begyűjteni azt a minimális információt, amit az input-anyagokból nem lehetett kinyerni.

### Kérdések (csak ami tényleg hiányzik — ha az anyagból kiderült, NE kérdezd)

1. **Termék terjedelme:** „Összesen hány óra / mennyi anyag / hány lecke / hány nap?"
2. **Felelős / Oktató:** „Ki a felelős / oktató / szakértő?" (Ha van cég-szintű csapat-fájl, pl. `00-agy/brand/csapat.md`, abból az alapértelmezett. Csak akkor kérdezd, ha nem derül ki.)
3. **Pozicionálás:** NE nyitott kérdésként. Javasolj a tartalom alapján:
   > „A tartalom alapján a [Termék] szerintem ide illik a vevő útján:
   > - Előtte ajánlott: [termék1], [termék2]
   > - Utána ajánlott: [termék1], [termék2]
   > - Magasabb-szintű program: [javaslat]
   > Stimmel, vagy módosítanál?"
4. **Ár és garancia:** ha a `kontextus-elemek.md` `ár / árképzés` vagy `garancia` mezője `KITÖLTENDŐ`, és a cég-szinten sincs érték: „Mennyibe kerül, és van-e garancia (ha igen, milyen)?” Ezt ne találd ki, mert minden hirdetés és sales-szöveg erre épül.
5. **Sales oldal:** „Van sales-oldal URL vagy szöveg?” (Ha van már megírt sales-oldal a kimeneti helyen, a közös szerződés „Hova kerül a kész anyag” része szerint, azt már betöltötted.)
6. **Visszajelzések:** „Van visszajelzés / testimonial ehhez a termékhez? Másold be, vagy jelezd, ha nincs."

### Szabályok
- **Egy menet, legfeljebb öt kérdés.** Minden kérdést egyszerre tegyél fel, ne csepegtess. Ha hatra jönne ki, a terjedelmet és a felelőst hagyd el (ezek pótolhatók később).
- Amit nem kapsz meg, az `KITÖLTENDŐ` marad a fájlban.
- Ha a felhasználó módosítja a Szakasz 0 javaslatokat (pl. más avatart kér) → adaptáld.
- A célcsoport-javaslatot erősítsd meg: „A javasolt 3-5 avatar jó, vagy cserélnél / bővítenél?"

---

## Szakasz 2 — Célcsoportok + marketing-üzenetek

### Cél
A skill legértékesebb szakasza. A termék tartalmából + az alap avatar-profilokból generálja a **termék-specifikus** célcsoportokat delta-formátumban. Hova melyik rész kerül (`celcsoport.md`, `kifogasok.md`, `uzenetek.md`): [sablonok.md](sablonok.md) §3.

Minden jóváhagyott avatarhoz generáld:

- **Termék-specifikus célok (4-6 db):** mit ér el KONKRÉTAN ezzel a termékkel. Ne generikus célok (azok az alap avatarban vannak), hanem termék-specifikusak. Deriválás: tartalmi egységek → milyen tudást/képességet/eredményt ad → ez az avatar szemszögéből mit jelent.
- **Termék-specifikus problémák (4-6 db):** mit old meg a termék ENNEK az avatarnak. Az avatar problémáit szűrd le erre a termék-témára, és adj hozzá 2-3 konkrétat az input-anyagok alapján.
- **Termék-specifikus vásárlási trigger (3-4 db):** a konkrét esemény/felismerés, amitől megvenné.
- **Kifogás-cáfolat (4-6 kifogás):** építs az avatar általános kifogásaira, de a cáfolat legyen termék-specifikus. Kategóriák: ár, idő, bizalom, szükséglet, halogatás, technikai (lásd `modszertan.md` kifogás-kategóriák). Ez a `kifogasok.md`-be kerül, nem a `celcsoport.md`-be, mert az író-skillek onnan olvassák.
- **Deal-killerek (3-4 db):** mikor NE ezt a terméket ajánljuk ennek az embernek.
- **Messaging insight:** belső monológ (egy bekezdés, ahogy az avatar gondolkodna a termékről, a saját szavaival, félelmeivel, reményeivel). A 3-5 hook (érzelem-, probléma-, eredmény-, kíváncsiság-alapú) az `uzenetek.md` üzenetmagjaihoz kerül.
- **Kapcsolódó üzenetmagok:** az `uzenetek.md` kategóriáiból (Érzelem, Probléma, Érték, Funkcionális) avatar + termék kombinációnként a top 3-4 legtalálóbb (elég a számra és a címre hivatkozni, a teljes szöveget nem kell bemásolni). Ha az `uzenetek.md` még üres, a termék-anyagból és a célcsoport-deltából fogalmazz meg 3-4 üzenetmagot kategóriánként, és írd be oda.

### Kimenet bemutatása
Célcsoportonként mutasd meg a teljes delta-profilt, és kérdezd:
> „Ez a [N]. célcsoport. Módosítanál rajta? Ha jó, megyek a következőre."

Amikor minden kész:
> „Minden célcsoport kész. Összeállítom a teljes kontextus-fájlt?"

---

## Szakasz 3 — Fájlok összeállítása + jóváhagyás

### Cél

Az ajánlat-mappa fájljait kitölteni, a `_sablon/` szerkezetében. Hogy melyik szakaszba mi kerül, és honnan: [sablonok.md](sablonok.md).

1. **`kontextus.md`:** a narratíva (mechanika, átalakulás, miért működik, értékpiramis, pozicionálás, kizáró tényezők). Értéket nem tartalmaz.
2. **`kontextus-elemek.md`:** a változó-értékek, mezőnként 3-5 variánssal, ha van hozzá anyag.
3. **`celcsoport.md`, `kifogasok.md`, `uzenetek.md`:** a Szakasz 2 deltája.
4. **`testimonialok.md`**, ha kaptál véleményt, és az ajánlat **`_attekintes.md`**-je.

> **Miért külön a narratíva és az érték?** Az író-skillek a `kontextus-elemek.md`-ből dolgoznak, árváltozásnál pedig csak azt kell átírni. A cég-szintű **keretek** (ár-keret, általános ügyfélszám, díj) a `00-agy/brand/kontextus-elemek.md`-ben élnek; az ajánlat-fájl felülírja őket, ha eltér.

**Ha az input régi, sokszekciós kontextus-fájl** (Alap infók, Tartalmi egységek, Sales oldal szöveg és hasonlók): a tartalmát a `sablonok.md` §1 táblája szerint oszd szét a `_sablon` szakaszaiba. Ne tartsd meg a régi szerkezetet mellette.

### Az érték-egyenlet és az ajánlat helye

Ha a termékhez van árazás, bónusz, garancia, limitálás vagy sürgetés:
- A `kontextus.md` „Mit ad el, és kinek” és „Az ajánlat mechanikája” része az értéket és a bónuszokat tartalmi szinten írja le.
- Az **érték-egyenlet** (vágyott eredmény / siker valószínűsége / várakozási idő / erőfeszítés) belső gondolkodási keret a fő ígéret és az átalakulás élesítéséhez, a metodikát lásd `modszertan.md`. Ha a felhasználó kéri, a „Miért működik” részbe írhatsz belőle egy rövid bekezdést.
- A konkrét ár, kuponkód és garancia-feltétel **ajánlat-szintű**: az ajánlat saját `kontextus-elemek.md`-jébe kerül.

### Önellenőrzés a kiírás előtt (kötelező)

Mielőtt kiírod a fájlokat, grep-eld a saját outputod:

- **Számold meg a „hanem"-eket.** Ha >1 az egész fájlban, írd át a feleslegeseket (lásd a [Márkahang és formázás](#márkahang-és-formázás) helyettesítő mintáit).
- **Keress em-dasht (—), ami NEM `**Fogalom** — magyarázat` lista-fejben van.** Prózában, hookban, kifogás-cáfolatban cseréld vesszőre, kettőspontra vagy két mondatra.
- **Ellenőrizd a talált tényeket.** Minden szám/ár/időtartam/külső tény vagy az input-anyagból jön, vagy `[becsült, megerősítendő]` jellel szerepel (lásd [Találgatás-jelölés](#input-anyag-parszolási-szabályok)).

A szabály le van írva a Márkahang szekcióban, de a hiba akkor csúszik be, ha a modell nem ellenőrzi magát végrehajtás előtt.

### Jóváhagyás

1. Mutasd meg a `kontextus.md`-t és a `kontextus-elemek.md`-t külön kódblokkban; a `celcsoport.md`, `kifogasok.md` és `uzenetek.md` tartalmát a Szakasz 2-ben már jóváhagyta.
2. Kérdezd: „Rendben van? Módosítanál valamit?"
3. Ha OK → írd ki az összes fájlt.
4. Frissítsd az ajánlat `_attekintes.md`-jének Státusz részét és a portfólió sorát.
5. Jelezd: „Kontextus kész. Innentől a többi skill (email-, sales-oldal-, hirdetés-szövegíró) ebből dolgozik. A cég-szintű keretekhez a `00-agy/brand/kontextus-elemek.md`-t használja."

---

## Input-anyag parszolási szabályok

### Egység-azonosítás
- `## Modul` / `## Fejezet` / `## Rész` / `## Fázis` fejlécek.
- Vagy `## [Szám] – [Név]` / `## [Név]`, ha az input így van strukturálva.
- Ha nincs explicit egység-bontás → a tartalom logikai egységei alapján javasold.

### Részlet-azonosítás
- `### [Részlet cím]` fejlécek (vagy `## `, ha az egységek `# ` szinten vannak).
- Részlet szövege: a fejléctől a következő fejlécig.
- Ha a részlet csak cím (nincs szöveg) → valószínűleg vázlat-only → jelöld.

### Melléklet/sablon azonosítás
- Minták a szövegben: „melléklet", „sablon", „letölthető", „fájl", „link", „kit", „csomag", „workbook", „checklist".
- Külső eszköz-fájl hivatkozások (pl. Figma-, Canva-, Notion-link).
- Kvíz, gyakorlat, feladat hivatkozások.

### Kulcskifejezés-kinyerés
- Szakkifejezések és ismétlődő fogalmak (2+ előfordulás).
- Szűrd ki a generikus szavakat (és, de, hogy stb.).
- Rangsorolj gyakoriság + specificitás alapján (top 20).

### Időadatok
- Ha az anyag tartalmaz időadatokat (pl. „(12:34)" vagy „Hossz: 12 perc") → gyűjtsd össze.
- Ha nincs → kérdezd Szakasz 1-ben.

### Találgatás-jelölés
Ha egy számot, árat, időtartamot vagy külső tényt (pl. versenytárs kiszállítási díja, recept-elkészítési idő, „X percen belül") az input-anyag NEM tartalmaz, akkor vagy **ne írd be**, vagy jelöld szögletes zárójellel: `[becsült, megerősítendő]`. Soha ne prezentálj találgatást tényként, főleg kifogás-cáfolatban, hookban vagy before-after-ben. Ez fogja meg a beillesztett-adatból nem alátámasztott szám- és díj-csúszásokat.

---

## Célcsoport deriválási logika

### Avatar-párosítás heurisztika

> 🟡 PÉLDA — az alábbi tábla minta. Illeszd a saját alap avatarjaiddal és termék-témáiddal.

| Termék téma | Tipikusan releváns avatarok |
|-------------|-----------------------------|
| [Design eszközök] | [Avatar 1], [Avatar 2], [Avatar 3] |
| [Webfejlesztés] | [Avatar 1], [Avatar 2] |
| [Marketing] | [Avatar 1], [Avatar 2] |
| [Személyes fejlődés] | [Avatar 1], [Avatar 2] |

Ez csak kiindulás, a tartalom-elemzés felülírhatja. Pl. ha egy design-termék kifejezetten vállalkozóknak szól → a vállalkozó-avatar kerül előre.

### Delta-generálás szabály

A delta-formátum azt jelenti: **csak ami ERRE a termékre specifikus.** Ne ismételd meg, amit az alap avatar-profil (`celcsoport.md`) már tartalmaz.

- ✅ „[Konkrét eszközben] magabiztosan eligazodni" → termék-specifikus cél
- ❌ „Anyagi biztonságot teremteni" → generikus cél, az avatarban van
- ✅ „Az üres [eszköz / vászon / dokumentum] előtt áll, nem tudja hol kezdje" → termék-specifikus probléma
- ❌ „Nem tudja hol kezdje a vállalkozást" → generikus probléma, az avatarban van
