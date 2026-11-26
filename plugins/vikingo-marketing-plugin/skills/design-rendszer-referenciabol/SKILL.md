---
name: design-rendszer-referenciabol
description: "Design rendszert készít egy vagy több tetsző weboldalból, appból vagy képernyőképből: megnézi és elemzi a referenciát, összegyűjti a vállalkozás tárgyi világát, és ebből egy DESIGN.md fájlt (színek, betűk, térközök, komponensek, weboldalhoz díszítő eszköztár, kompozíciós minták és referenciaképek) meg egy előnézeti oldalt ír, amiből weboldal, app, dia és grafika is készülhet. Szóbeli kérésre javítja. Akkor használd, ha a felhasználó ezt mondja: design rendszer, design system, arculat egy oldalból, ilyen stílusú legyen, ez az oldal tetszik, csinálj design rendszert, DESIGN.md. Nem ez kell, ha egy kész oldalt kell megépíteni a design rendszerből, vagy logót kell tervezni."
---

# Design rendszer referenciából

Egy oldalból, ami tetszik, olyan design rendszert csinálsz, amiből bármi készülhet: weboldal, app, prezentáció, közösségi poszt, grafika. A felhasználó jellemzően nem designer. Nem tudja szavakban elmondani, milyen érzést akar, de meg tudja mutatni egy oldallal. A te dolgod, hogy ebből kivedd, ami a hatást adja, és a saját vállalkozására fordítsd.

**A minőség mércéje:** az eredmény ne legyen sablonos. A színek és a betűk hasonlósága kevés. Ami egy oldalt felismerhetővé tesz, az a jellegzetességekben van: címsorkezelés, háttér, díszítés, képkezelés, ritmus. Ezt kell megfognod, pontosan úgy, ahogy a referenciában van.

**A hűség az első.** Csak azt veszed át, ami a referenciában ténylegesen megvan. Ahol a referenciában nincs egy elemtípus (nincs dekor-réteg, nincs ikon, nincs szekcióhatár), ott a rendszerben sincs: kiírod, hogy „nincs”, és nem pótolod kitalált díszítéssel. Egy sima, skill nélküli kérés is visszaadja a referencia színeit és betűit. Ennek a skillnek abban kell jobbnak lennie, hogy a karaktert (arányok, vonalak, lépték, ritmus) is pontosan megfogja, és hogy a rendszer teljes és használható legyen, nem abban, hogy többet tesz bele.

Kimenet: egy `DESIGN.md` (a Google nyílt formátuma, amit a Claude, a Codex és más eszközök is értenek), egy `elonezet.html`, amin az egész rendszer egy oldalon látszik, és weboldalnál a referencia szakaszonkénti képei.

## Sorrend és mélység

A rendszer elemei fontossági sorrendben. Ebben a sorrendben dolgozz: ahol a cél miatt megállsz, az addigi rész már használható.

1. Színek
2. Betűpár
3. Méretek és térközök
4. Formák: lekerekítés, szegély, vonalak
5. Gomb és űrlapmező
6. Logó
7. Kártya, felső címke, menü, lábléc
8. Ikonok
9. Árnyék és mélység
10. Hangnem
11. Visszatérő jel, díszítés, szakaszhatár
12. Képek stílusa
13. Elrendezési minták és referenciaképek
14. Állapotok (hover, fókusz, letiltott, hiba)
15. Mozgás

- **Eszközhöz** (app, kalkulátor, Chrome-bővítmény, dashboard) az 1-10. elég, mert ott a felület kicsi, és ezek döntik el, hogyan néz ki. Az állapotok itt is kellenek, röviden.
- **Weboldalhoz, marketinganyaghoz** mind kell. Itt a hatás nagy része az elrendezésből jön (milyen a hero, hogyan rétegződnek a képek, hogyan követik egymást a szakaszok), és ezt szöveg nem tudja teljesen átadni: a referenciaképek is a rendszer részei.

Ha nem derül ki a kérésből, mire fogja használni, kérdezd meg egy mondatban. Ha mindkettőre kell, csináld a teljeset.

Ami a nagy rendszereké (sötét mód, grafikonszínek, külön szabály e-mailre és posztra, több nyelv vagy márka), az kimarad, hacsak a felhasználó nem kéri. A kontraszt viszont mindig ellenőrzött.

## 1. Bemenetek

Nézd meg, mi van már meg, és csak a hiányzóra kérdezz, egy üzenetben:

- **Referencia:** 1-3 weboldal-cím vagy képernyőkép, és ha van, egy mondat arról, mi tetszik benne. Kettő jobban működik, mint egy: az egyik az irányadó, a másikból csak részletek jönnek.
- **A vállalkozás:** mit csinál, kinek, milyen hangon. Ha van céges agy (`00-agy/`, `agy/` vagy hasonló, benne üzleti profil, márkahang, arculat), onnan olvasd, ne kérdezd.
- **Kötöttségek:** van-e logó, fő szín vagy betű, amihez ragaszkodik. Ami kötött, az kötött marad, a referenciából csak a többi jön.
- **Színkérés:** ha a felhasználó csak lazán mond színt („ilyen kéket, bézzsel”), az elég, abból te csinálsz palettát.

Ha egy design rendszer már létezik, és a felhasználó módosítást kér, ne kezdd elölről: olvasd be, és csak a kért részt változtasd.

## 2. A referencia megnézése

Böngészőben nyisd meg, nézd meg a hajtás feletti részt, és görgess végig a láblécig. A különleges megoldásokat nézd közelebbről. Ne csak a heróból következtess.

- A számokat (betűcsalád, méret, szín, lekerekítés, térköz) a böngészőből olvasd ki, ne a képernyőképről becsüld. A kiolvasó szkript a [`references/elemzes.md`](references/elemzes.md) végén van. Ha nincs böngészőeszközöd, a `python3 scripts/kepernyokep.py <webcím> --kiolvas` a gépen lévő Chrome-mal futtatja.
- **A szerkezeti vonalakat külön nézd meg:** rácsvonal, keret, elválasztó, aláhúzás. Milyen vastag, milyen színű, hol fut végig (a teljes szélességen, a tartalomig, a kártya széléig), és mi igazodik hozzá. Ezek adják sok oldal karakterét, és a rossz vastagság vagy a rossz helyen futó vonal az első, ami „nem olyan” érzést kelt.
- A referenciáról készüljenek képek a `referenciak/` mappába: `python3 scripts/kepernyokep.py <webcím> -o referenciak/ --szakaszok`. Ez a teljes oldalt asztalon és mobilon, és külön minden nagyobb szakaszát lefotózza. A szakaszképek közül tartsd meg azokat, amelyek egy kompozíciós mintát mutatnak (hero, osztott blokk, képkollázs, kártyasor, CTA), és nevezd át őket beszédesen (`hero.jpg`, `kepkollazs.jpg`); a többit és a teljes oldalas képeket tedd át a `referenciak/_egyeb/` almappába, hogy ne zavarjanak (a teljes oldalas kép a görgetésre betöltődő tartalom miatt hiányos vagy megnyúlt lehet; a szakaszképek a megbízhatók). Ha a süti-ablak takar, a böngészőeszközzel fotózz.
- Ha egy oldal nem nyílik meg, mondd meg azonnal, melyik, és kérj képernyőképet vagy másik oldalt. Képernyőképből betűnevet és animációt ne állíts biztosra.
- Ha a felhasználó csak képet adott, a képből dolgozz, és jelöld, mi becslés.

## 3. Elemzés

Az [`references/elemzes.md`](references/elemzes.md) két listáján menj végig:

1. **Az alapok:** színek, betűk, elrendezés, formák, komponensek. Ezt az AI magától is jól megtalálja, gyorsan haladj rajta.
2. **A jellegzetességek:** címsorkezelés, felső címkék, háttér, dekor-réteg, szekcióhatárok, képkezelés, ikonstílus, illusztráció, mozgás, ritmus. **Ezen múlik, hogy sablonos lesz-e az eredmény.** Mindegyikről írd le, mit láttál, és hogy a referencia karakteréhez mennyire kell. Ami nincs, arról írd le, hogy nincs: ez is a karakter része.

Az elemzés végén két dolgot rögzíts:

- **A vizuális intenzitás** 1-től 5-ig: 1 a csendes, minimalista oldal, 5 a merész, rétegzett, sok hangsúlyos megoldással dolgozó. Ezt a referenciából méred, és a rendszer ezt tartja: egy 4-es referenciából nem lehet 2-es rendszer.
- **A szignó:** az az egy-két formai elem, ami a referenciát felismerhetővé teszi, és több helyen visszatér (például egy élforma, ami a gombon, a képkereten és a szekcióhatáron is ott van). Ha a referenciának nincs ilyen visszatérő eleme, és a karaktere a tipográfiából vagy a vonalakból jön, akkor az a szignó: ne találj ki mellé díszt.
- **A kompozíciós minták:** a referencia 4-6 jellemző szakasz-felépítése. Mindegyiknél: mi az (például „kettéosztott hero: bal oldalt sötét szövegpanel, jobb oldalt kifutó fotó”), melyik referenciakép mutatja, és milyen tartalomhoz jó (nyitás, probléma, ajánlat, bemutatkozás, CTA). Ez adja meg, hogyan áll össze egy oldal; a díszítő eszköztár csak azt, mivel díszíted.

## 4. A vállalkozás tárgyi világa

Gyűjts 5-10 tárgyat, anyagot, eszközt vagy szót, ami a vállalkozás munkájához tartozik. Egy kertépítőnél ilyen a ceruza, a pauszpapír, a szintvonal és a díszfű.

**A tárgyi világ nem hoz új elemet a rendszerbe.** Csak ott kap szerepet, ahol a referenciában van egy tartalmat hordozó elem: háttérbetű, futó szalag szövege, illusztráció vagy ikon témája, a színek neve. Ott a tartalom a vállalkozásé legyen, ne a referenciáé. Ha a referenciában nincs ilyen elem, a tárgyi világ csak a színnevekben és a képek témájában jelenik meg.

Írj mellé egy rövid **kerülendő** listát is: a szakma elcsépelt képi világát (fűnyíró-ikon a kertésznél, súlyzó-ikon az edzőnél, robotfej és agy-ikon az AI-nál), és amit a felhasználó maga nem szeret.

## 5. Fordítás a saját rendszerre

- **Színek:** 4-6 fő szín (alap háttér, fő kiemelés, másodlagos, váltó háttér, sötét felület), mellé a szöveg-, halvány szöveg- és vonalszín. Mindegyiknek szerepe és beszédes neve van a tárgyi világból. A referenciából a szerepek és az arányok jönnek (mennyi a sötét felület, mennyi a kiemelés), a konkrét árnyalat a felhasználó színéből vagy a tárgyi világból. A tokenek elnevezése a sablon szerint menjen, mert az ellenőrző szkript a nevekből tudja, mi a szöveg és mi a háttér.
- **Betűk:** a Google Fontsból válassz, a referencia jellegéhez illőt. Ellenőrizd, hogy tudja az ő és ű betűt, és ha dőlt kiemelést használsz, hogy van-e valódi dőlt változata (`scripts/ellenor.py fontok "Betű neve"`). A címsorbetű legyen karakteres; az Inter, a Roboto és az Arial címsorra nem jó választás, hacsak a referencia nem pont azt használja.
- **Díszítő eszköztár:** a sablon **Signature Elements** szakaszában csak azt töltsd ki, ami a referenciában megvan, ugyanannyiszor és ugyanakkora léptékben. Ami nincs, oda „nincs” kerül. Egyféle szekcióhatárból nem lesz kettő, és egy csendes háttérből nem lesz textúrás. Ha egy elem tartalmat hordoz (szalag, háttérbetű), a szavak a felhasználó szövegéből vagy a tárgyi világból jönnek.
- **Gyakoriság:** minden eszköznél írd oda, oldalanként hányszor jelenhet meg, a referencia alapján. Ha a referencia változatos, tartsd a változatosságot; ha egyféle megoldást ismétel, az a karaktere, maradjon egyféle.
- **Logó:** ha van, a `logo/` mappába kerül a színes, egy sötét egyszínű (világos háttérre) és egy fehér (sötét háttérre) változat. SVG-nél a kitöltésszínt cseréld; ha csak PNG van, mondd meg, hogy egyszínű változathoz SVG kell. Ha nincs logó, a névből a címsorbetűvel szöveges logót készíts (SVG, `<text>`), a referencia logójának jellegét követve (súly, nagybetű, betűköz), és mondd ki, hogy ideiglenes. Favicon: a kezdőbetű vagy a logó jele, négyzetben.
- **Ikonok:** válassz egy konkrét, ingyenes ikoncsaládot, ami a referencia ikonjaihoz illik (vonalas: Lucide, Tabler, Phosphor; tömör vagy kettős tónusú: Phosphor, Heroicons), és add meg a vonalvastagságot, a méretet és a színt. Ha a referencia illusztratívabb, rajzolt ikonokat is használ, azok stílusát külön írd le (vonal, kitöltés, színek, mi a témájuk). Ha a referenciában nincs ikon, írd le, hogy a rendszer ikon nélkül is működik, és csak akkor ajánlj családot, ha a felhasználó céljához (például eszközhöz) kell.
- **Állapotok:** a gombnál és a mezőnél a hover, a fókusz (látható körvonallal), a letiltott és a hiba állapot, egy-egy sorban. A referenciából vedd, ahol látszik; ahol nem, a rendszer többi szabályából következik.
- **Kis felület:** eszközhöz (kalkulátor, 360 px széles bővítmény-ablak) írd le, mi változik: kisebb betűskála, sűrűbb térköz, melyik díszítés marad meg (általában csak a szignó és a színek).
- **Számozás:** dísznek ne legyen sorszám a szakaszokon. Ha a sorrend tartalom (lépések, trimeszterek, hetek), akkor maradhat, és akár a szignó része is lehet.
- **Ne másolj:** logót, szöveget, fotót és márkanevet a referenciáról soha. A formai nyelvet veszed át, nem a tartalmat.
- **Az intenzitás megtartása:** a referencia merészségét, rétegzettségét, tipográfiai léptékét és részletgazdagságát is fordítsd át, ne csak a színeit és a betűit. Egy látványos referenciából ne csinálj automatikusan visszafogott rendszert; ha maga a referencia csendes, azt tartsd meg. Mértékletesség csak abban kell, hogy egy kategórián belül egy megoldás legyen (egyféle címsorkiemelés, nem három).

## 6. A DESIGN.md megírása

A [`references/design-md-sablon.md`](references/design-md-sablon.md) szerint. A szakaszcímek angolul maradnak (`## Colors`, `## Typography` stb.), mert az eszközök erről ismerik fel őket. A szöveg magyar.

- Felül a YAML-blokk: a gépnek szóló értékek. Alatta szakaszonként rövid, magyar indoklás: mit, hol, miért.
- Minden szakasz rövid. A cél nem az, hogy minden ki legyen fejtve, hanem hogy egy AI ebből döntést tudjon hozni egy olyan felületen is, amit nem írtál le.
- A **Signature Elements** szakasz a legfontosabb: az intenzitás és a díszítő eszköztár táblázata, elemenként mi az, honnan jön, hol és hányszor használd.
- A **Layout** szakaszba kerülnek a kompozíciós minták, mindegyik mellett a referenciaképe `@referenciak/hero.jpg` alakban (a formátum így jelöli a fájlhivatkozást).
- A végére 3-5 **kész utasítás** kerül, amit a felhasználó bemásolhat („Készíts ebből egy diát…”). Weboldalas utasításnál mindig benne legyen, hogy a `referenciak/` képeit is nézze meg, és a kompozíciós mintákból építkezzen.

## 7. Előnézet és ellenőrzés

Először a `DESIGN.md`-ből készüljön CSS: `python3 scripts/ellenor.py css DESIGN.md -o tokens.css`. Ebben vannak a színek, betűk, térközök és komponensek változói, és a betűk betöltése (Google Fonts) is. Az előnézet és a későbbi oldalak ezt töltik be, így ha a `DESIGN.md` változik, elég újra lefuttatni.

Készíts egy `elonezet.html`-t, ami a `tokens.css`-ből dolgozik. Ez a rendszer bemutató oldala: aki megnézi, ebből dönti el, tetszik-e neki. Ezért mindig ugyanebben a sorrendben áll, előbb az alapok egyenként, a végén a minták:

0. **Fejléc:** a rendszer neve, egy mondat a karakteréről, alatta referencia, intenzitás, betűk, szignó. Felül tapadó menü a fejezetekre.
1. **Színek:** nagy színminták névvel, kóddal és szereppel, alattuk a szöveg-háttér párok, amelyek használhatók.
2. **Betűk:** a teljes skála sorban, a legnagyobbtól a legkisebbig (display, H1-H3, felső címke, szövegtörzs, címke), soronként a méret és sorköz, magyar, ékezetes mintaszöveggel.
3. **Térköz és formák:** a térközskála, a lekerekítések, a vonalak (vastagság, hol futnak).
4. **Logó és ikonok:** a logó változatai, a választott ikoncsaládból 6-8 ikon.
5. **Elemek:** gombok és állapotaik (hover, fókusz, letiltott), mezők hibával, kártya, felső címke; eszközhöz a 360 px-es minta-ablak.
6. **Minták, a végén:** fejléc és hero; legalább kétféle kártyaszakasz (például három egyforma, összeillő panelpár); számok vagy idézet; a jellegzetes szakaszok, amelyek a referenciában vannak; egy dashboard (oldalsáv, számcsempék, grafikon, táblázat); záró szakasz és lábléc. Minden minta fölött egy sor: mi ez, és ha van, melyik referenciaképből jön (`referenciak/hero.jpg`).

Csak olyan díszítés és szakasz kerül bele, ami a rendszerben van. A szignó a mintákban látszik működés közben, a képek helyén a képstílust leíró helyőrző áll.

Utána:

1. `python3 scripts/ellenor.py kontraszt DESIGN.md`: a színpárok olvashatósága. Ami elbukik, azt javítsd. Amit a szkript nem lát (például a gomb egy sötét szakaszon), azt a képen nézd meg.
2. `python3 scripts/kepernyokep.py elonezet.html`: képernyőkép 1440 és valódi 390 px szélességen, és a kilógó elemek listája. Nézd meg a képeket, és vesd össze a referencia képernyőképével egymás mellett: **felismerhető-e a karaktere? Ugyanolyan intenzitású-e, vagy szelídebb lett? Stimmelnek-e a vonalak (vastagság, hol futnak), az arányok és a lépték? Van-e benne olyan díszítés, ami a referenciában nincs?** Ami nincs a referenciában, azt vedd ki.
3. Mobilon külön figyelj: van-e oldalt legalább 20 px margó, nem fut-e díszvonal vagy háttérbetű a szöveg alatt olvashatatlanul, és nincs-e vízszintes görgetés (a nagy háttérelemeknél kell az `overflow: hidden` a szakaszon). A két sorba törő gombfelirat se csússzon egymásra. A nagy címsorméret hosszú magyar szavaknál (például „állapotfelmérés”) ne lógjon ki: mobilra legyen külön méret, vagy `clamp()`.
4. Minden szakaszháttéren nézd meg a díszítést és a képhelyőrzőt is: ha a színe egybeolvad a háttérrel, a szignó eltűnik. Ilyenkor írd be a `DESIGN.md`-be, melyik háttéren milyen színű legyen.

Ha valami nem stimmel, javíts, és nézd meg újra. A képernyőképek a `kepek/` mappába kerülnek; ezek csak ellenőrzésre valók.

## 8. Átadás és javítás

Mutasd meg az előnézetet teljes méretben (Artifactként, vagy a böngészőben megnyitva), ne kicsinyített képernyőképen, mert azon nem látszik, mi történt. Írd le röviden (legfeljebb öt sorban):

- melyik referenciából mit vettél át,
- mi a szignó, és mi jött a tárgyi világból,
- mit hagytál ki szándékosan.

Utána a felhasználó szavakkal javíttathat („a gomb legyen kerekebb”, „kevesebb boltív”, „legyen vagányabb”, „több elválasztó”, „melegebb legyen a háttér”). A „vagányabb” vagy „visszafogottabb” kérés az intenzitást állítja egy fokkal, és vele együtt az eszközök léptékét és gyakoriságát. Ilyenkor a `DESIGN.md`-t és az előnézetet is frissítsd, és ne csinálj új verziót, hacsak nem kéri.

## Hova kerül

Ha a céges agyban már van `design-rendszer/` mappa (vagy arculati mappa), abba. Ha van agy, de ilyen mappa nincs, az agyon belül a márka mellé: `<agy>/brand/design-rendszer/` vagy `<agy>/ceg/design-rendszer/`, ahogy az agy többi fájlja áll. Ha nincs agy, a projekt gyökerébe, `design-rendszer/` mappába. Benne:

```
design-rendszer/
├── DESIGN.md          a rendszer: értékek és szabályok
├── tokens.css         a DESIGN.md értékei CSS-ben (az ellenor.py css készíti)
├── elonezet.html      a bemutató oldal: színek, betűk, formák, elemek, a végén minták
├── referenciak/       a referencia teljes oldala és a kompozíciós minták képei (csak saját használatra)
├── kepek/             az ellenőrző képernyőképek
└── logo/              a logó és változatai (vagy az ideiglenes szöveges logó), favicon
```

A többi skill és projekt innen dolgozik. App vagy dia építésekor elég a `DESIGN.md`. Weboldal építésekor a `DESIGN.md` mellett a `referenciak/` képeit is meg kell nézni, és a karakterüket tartani: a rendszer adja a következetességet, a referenciaképek a kompozíciót.

## Kész, ha

- A `DESIGN.md` és a `tokens.css` megvan, a kontrasztellenőrzés hiba nélkül lefutott, és a betűk tudják az ékezeteket.
- Az előnézetről asztali és mobil képernyőkép készült, meg lett nézve, nincs kilógó elem, és a referencia karaktere felismerhető rajta.
- A felhasználó megkapta a rövid összefoglalót.

Ha egy lépés elakad (nem nyílik meg a referencia, nincs böngészőeszköz, nincs internet a betűellenőrzéshez), mondd ki, mit nem tudtál ellenőrizni, és ne állítsd, hogy megvan.
