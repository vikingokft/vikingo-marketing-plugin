# Flow-kártyák · webshop (29-36)

> A kurzus webshop flow-leckéinek lepárlása (2026-07-08). CSAK a kiválasztott flow kártyáját töltsd be.

---

# Webshop üdvözlő (kuponos) · flow-kártya (forrás: 29-es lecke)

**Mikor ajánld:** webshopoknak, ahol a feliratkozás egy felugró ablakos kedvezményhez kötődik. A cél itt nem a hosszú távú kapcsolatépítés, hanem az első vásárlás minél gyorsabb megszerzése, mert egy webshopnál a termékek impulzusvásárlósak és egy kattintásra megvehetők.
**Trigger:** feliratkozás popupon vagy űrlapon keresztül, jellemzően egy kedvezményes vásárlást ígérő csali (százalékos engedmény, fix összegű kedvezmény vagy ingyenes szállítás) átvételéért.
**Terjedelem:** a lecke nem ad pontos email-számot. A sorozat addig fut, amíg a feliratkozó nem vásárol, vagy amíg a kupon le nem jár. Nem sok levélről van szó, nem cél a folyamatos ismétlés.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | azonnal, feliratkozáskor | Üdvözlő (kód átadó) | köszöntés a márkánál és a kedvezménykód jól látható, egyértelmű átadása | ez a legjobb megnyitási arányú levél, a kód legyen a lényeg, ne rejtsd el; opcionálisan rövid sztori, USP, alapító-bemutatkozás fér bele, de csak kiegészítésként |
| 2 | pár nappal később | Emlékeztető | ismétli a kódot, és ha közeledik a lejárat, jelzi hogy hamarosan lejár | itt már mehet mélyebb sztorizás, eredettörténet |
| 3 | a lejáratig, több levélben | Ajánlat / Social proof | különböző üzenetmagokból építkezik: USP, vásárlói vélemények, céges értékek, termékelőnyök | mindegyik levél más szempontot emel ki, cél az első vásárlás felé terelés |
| 4 | a lejárat előtt, ha van konkrét határidő | Sürgetés | figyelmeztet, hogy a kód hamarosan végleg lejár | csak akkor releváns, ha van kezelt lejárati dátum |

## Elágazások

- vásárolt a sorozat közben → azonnali kilépés a flow-ból
- lejárt a sorozat vásárlás nélkül → bekerül a heti hírlevél-ritmusba, ott találkozik újra az ajánlatokkal, vagy átkerül egy másik meglévő automatizmusba, például a kosárelhagyásba

## Mire figyelj

- ne adj túl nagy első kedvezményt, mert azt fogják elvárni és mindig azon az áron akarnak majd vásárolni, a nagyobb akciókat tartogasd különleges alkalmakra
- a kupon-határidő kezelése szoftverfüggő: van, ahol egyedi, feliratkozáshoz kötött lejáratú kód natívan megoldható, máshol kiegészítő alkalmazás kell hozzá, vagy marad a havi rotáló kupon
- ha nincs konkrét lejárati határidő, az is működik, mert aki erre a kedvezményre iratkozott fel, már közelebb van a vásárláshoz
- a fő cél az első vásárlás megszerzése, nem a kapcsolat mélyítése, ezért nyomd ezt egészen addig, amíg meg nem történik a vásárlás
- webshopoknál esszenciális automatizmus, mert sokan iratkoznak fel a popupról, ezért érdemes gyakran nézni az eredményeket és fejleszteni

## Kontextus-igény

- van-e kedvezmény és milyen típusú (egyedi lejáratú kód vagy havi rotáló kód)
- milyen email-marketing szoftvert használnak, és az képes-e egyedi, feliratkozáshoz kötött lejáratra
- van-e a webshopnak már kosárelhagyó vagy más automatizmusa, ahova a nem konvertáló feliratkozó átkerülhet
- mennyi ideig fusson a sorozat, ha nincs konkrét kupon-lejárat

---

# Kosárelhagyás-létra (fizetés-elhagyás) · flow-kártya (forrás: 30-as lecke)

**Mikor ajánld:** minden webshopnak, ahol be lehet állítani, hogy a megkezdett, de be nem fejezett fizetés triggereljen egy levélsorozatot. Ez az egyik legegyszerűbben megvalósítható és legjobban megtérülő automatizmus, mert a látogató itt már a lehető legközelebb volt a vásárláshoz.
**Trigger:** a fizetési folyamat megszakítása (checkout elkezdve, de nincs sikeres fizetés). Nem indul annak, aki közben mégis befejezte a vásárlást, és nem indul újra annak, akinek ugyanez a sorozat elment már az elmúlt 14 vagy 30 napban.
**Terjedelem:** 4 email, körülbelül 3 nap alatt.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | kb. 1 óra a félbehagyás után | Emlékeztető | tiszta emlékeztető a kosár tartalmáról, nagy termékfotóval, kedvezmény nélkül | ez konvertál a legjobban a sorozatban, aki idáig eljutott nem kódra várt, csak elkalandozott |
| 2 | +1 nap | Értékadó | a termékhez vagy termékcsoporthoz kapcsolódó tipikus üzenetmagos tartalom | |
| 3 | +1 nap | Social proof / új szög | eddig nem használt előny vagy vásárlói történet, még mindig emlékeztető jelleggel | dinamikusan szerepelhet benne a kosár tartalma is |
| 4 | +1 nap | Sürgetés | utolsó emlékeztető, hogy a kosár még megvan | ennél tovább ne nyújtsd, az ötödik-hatodik levél után esik a szándék és nő a spam-jelölés kockázata |

## Elágazások

- fizetett bármelyik levélnél → kilép a sorozatból, átkerül a vásárlás utáni flow-ba, ahol már szállítás-visszaigazolásról, használati tippekről, esetleg kapcsolódó termékről szól a kommunikáció
- a négy levél után sem vásárolt → kilép a sorozatból, innentől már nem a kosárra emlékeztetsz, hanem a szokásos kampányok, edukáció következik
- ha ez már bevált és van rá kapacitás, ugyanez a logika kiépíthető gyengébb triggerekre is, konkrétan a kosárba tett de nem checkoutolt termékre, vagy a csak megnézett termékre, de ez már komplikáltabb rendszer és több tapasztalatot igényel

## Mire figyelj

- a checkout-elhagyás nem ugyanaz, mint a kosár-elhagyás, a termék-böngészés elhagyása vagy az oldal-elhagyás, a platformok gyakran összekeverik ezeket a neveket, ami beállítási hibákat okoz
- az első levélben soha ne adj kedvezményt, mert azzal megtanítod a vásárlóidnak, hogy érdemes félbehagyni a fizetést és megvárni az ajánlatot, ez hosszú távon csökkenti a teljes áras vásárlásokat
- adatkezelési szempontból fizetés-megszakításnál megvan a jogalap az emailre, kosár- vagy böngészés-elhagyásnál csak akkor küldhetsz, ha az illető már korábbi vásárló vagy feliratkozó, tehát megvan a marketing hozzájárulása
- kezelheted egy kalap alatt az új és a korábbi vásárlókat is, vagy szét is bonthatod különböző automatizmusokra
- ezek az automatizmusok 3-15 százalékát meg tudják menteni a be nem fejezett vásárlásoknak

## Kontextus-igény

- milyen platformon fut a webshop, és az mennyire különbözteti meg pontosan a checkout-elhagyást a kosár- vagy böngészés-elhagyástól
- van-e szándék külön kezelni az új és a korábbi vásárlókat
- akarnak-e a checkout-flow beválása után bővíteni kosár- vagy böngészés-elhagyásra is
- fut-e párhuzamosan más flow (pl. kuponos üdvözlő), és hogyan kezeljük az átfedést (kizárás vagy együtt-futás)

---

# Tranzakciós / rendelés-státusz · flow-kártya (forrás: 31-es lecke)

**Mikor ajánld:** minden webshopnak vagy fizikai terméket szállító vállalkozásnak. Ezek a rendszer-üzenetek amúgy is kimennek, a kérdés csak az, hogy száraz státusz-üzenetek maradnak, vagy tudatosan felépítve dolgoznak a vállalkozásért. Ez a sorozat lő elsőként a vásárlás után, még a vásárlás utáni köszönő-sorozat (32-es flow) előtt.
**Trigger:** a rendelés-státusz változása: visszaigazolás, feladás, fennakadás vagy késés, kézbesítés. Esemény-vezérelt, minden levél a hozzá tartozó státusz-változáskor megy ki, nem előre beállított naptár szerint.
**Terjedelem:** 4 érintési pont, ebből az egyik (fennakadás/késés) csak feltételesen megy ki.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | azonnal, rendeléskor | Tranzakciós (visszaigazolás) | megerősíti hogy a rendelés átment, és mit fog kapni a vásárló | ez szinte mindenkinél megnyílik, itt jó helyen kérdezhetsz meg egy dolgot a vásárlóról, de ne told túl, egy javaslat elég |
| 2 | feladáskor | Tranzakciós (követés) | nyomkövetési adat, közben egy kis márkaépítő tartalom vagy emlékeztető, mire számíthat | könnyebbé teszi a várakozást |
| 3 | csak ha történik fennakadás vagy késés | Tranzakciós (probléma-kezelő) | elmondja mi történt, mit tesznek érte, és hogy figyelik | ez előzi meg a dühös emailt és a rossz értékelést, ha van rá kapacitás, ide érdemes ügyfélszolgálatos kollégát is bevonni |
| 4 | kézbesítéskor | Onboarding (használati tipp) | konkrét használati tipp, amitől a vásárló jobban jár a megvett termékkel | csökkenti a visszaküldést, előkészíti a későbbi véleménykérést |

## Elágazások

- a 3. levél (fennakadás/késés) csak akkor megy ki, ha ténylegesen csúszik vagy elakad a szállítás, egyébként kimarad a sorozatból
- a sorozat végén a vásárló átkerül a vásárlás utáni és a véleménykérő flow-ba

## Mire figyelj

- ez a legalábecsültebb sorozat, miközben szinte mindenki megkapja és meg is nyitja
- itt kivétel az általános szabály, hogy sok levél árt, ezt nem lehet igazán túlkommunikálni, mert a vásárló ilyenkor a legizgatottabb
- ez fut más automatizmusok mellett is, mert szolgáltatás-jellegű, nem marketing-döntés, a szokásos „mikor ne induljon el" kérdés itt kevésbé releváns
- vihető emailben és SMS-ben is, a szokásos hírlevél-ritmustól teljesen függetlenül
- ezt jellemzően nem az email-marketing szoftverben állítod be, hanem a webshop-szoftverben, de illeszd a designt a márka konzisztenciájához
- profibb shopoknál működhet egy kiegészítő termék felajánlása az eredeti rendeléssel kiszállítva, de ez technikailag komplex, alapból nem ajánlott

## Kontextus-igény

- milyen webshop-platform kezeli a rendelés-eseményeket, és hogyan állíthatók be rajta a státusz-triggerek
- van-e SMS-csatorna is a levelezés mellett
- van-e ügyfélszolgálati kapacitás a fennakadás-ág kezelésére
- akarnak-e kis kérdést vagy kérdőívet beépíteni az első, visszaigazoló levélbe

---

# Vásárlás utáni köszönő és onboarding · flow-kártya (forrás: 32-es lecke)

**Mikor ajánld:** bárkinek, akinél lehetséges az újravásárlás, tehát nemcsak webshopoknak, hanem szolgáltatásoknak, kurzusoknak, előfizetéseknek is. A cél, hogy a vásárló elégedett legyen és jól használja a terméket, mert ez alapozza meg a jövőbeli újravásárlást.
**Trigger:** a sikeres, tényleges vásárlás (a lemondott vagy visszatérített rendelések nem számítanak), 1 napos késleltetéssel. Ügyelni kell, hogy ne induljon el kétszer ugyanarra a rendelésre, és ne mosódjon össze a tranzakciós sorozattal, ami ezt megelőzően fut.
**Terjedelem:** 2 fő levél, a véleménykérés (review) ettől külön flow (33-as lecke).

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | legalább 1 nappal a vásárlás után | Köszönet (új vs visszatérő elágazással) | levesz egy terhet a vásárlóról, hogy jól döntött-e, elkezdi a közösségépítést és a kapcsolat mélyítését | az első vásárlót a tranzakciós köszöntésen felül is üdvözölni kell, a visszatérőnél ez rövidebb lehet |
| 2 | a köszönő után | Onboarding (használati, segítő levél) | megmutatja hogyan érje el a vásárló azt az eredményt, amiért a terméket vette | itt nem eladni akarsz, hanem segíteni a termék jó használatában, ez csökkenti a visszaküldést és panaszt |

## Elágazások

- első vásárló → teljes köszöntés, megnyugtatás, közösségépítés indítása
- visszatérő vásárló → rövidebb köszönet, nem kell újratanítani a termékhasználatot, például egy táplálékkiegészítőnél nem kell minden hónapban újra elmagyarázni a használatot
- sok terméket áruló webshop → a segítő levélhez tudni kell mit vásárolt; egytermékes webshopoknál és nem-webshop modelleknél (szolgáltatás, kurzus, előfizetés) ez könnyebb, sok-termékes webshopnál csak a legtöbbet vásárolt termékekre érdemes egyedi segítő levelet írni
- a véleménykérést a kurzus önálló flow-ként kezeli (33-as lecke), bár technikailag egybe is építhető

## Mire figyelj

- ne induljon el kétszer ugyanarra a rendelésre, és ne keveredjen össze a tranzakciós sorozattal, ez utána következik
- úgy időzítsd, hogy számolj a tranzakciós emailekkel (visszaigazolás, feladás, megérkezett) is, hogy a vásárló ne kapjon feleslegesen párhuzamos üzeneteket
- a cél nem az azonnali upsell, hanem hogy a vásárló elégedett legyen és jól használja a terméket, ez alapozza meg a következő vásárlást
- minél ügyesebben tudja használni a terméket és minél nagyobb eredményt ér el vele, annál könnyebben megy majd a következő eladás és a véleménykérés is

## Kontextus-igény

- webshop vagy szolgáltatás, kurzus, előfizetés modellről van-e szó
- egy vagy több terméket árulnak, és van-e kiemelt, legtöbbet vásárolt terméklista, amire egyedi segítő levelet érdemes írni
- hogyan különbözteti meg a rendszer az első és a visszatérő vásárlót
- van-e már külön kiépített véleménykérő flow, vagy ezt is ebbe a sorozatba kell építeni

---

# Vélemény- és UGC-kérés · flow-kártya (forrás: 33-as lecke)

**Mikor ajánld:** webshopoknak (vagy vélemény/ajánlás-gyűjtésre bármilyen vállalkozásnak), amikor a vásárló már ténylegesen használta a terméket, és a cél nem eladás, hanem olyan anyag szerzése, ami visszaforog a hirdetésekbe, sales-oldalra és közösségi bizonyítékként.
**Trigger:** rendelés kézbesítve + X nap. Ne induljon, ha a rendelést közben visszaküldték vagy stornózták.
**Terjedelem:** 2 email, ~19 nap (kézbesítés +14 nap, majd +5 nap).

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | Kézbesítés +14 nap | Értékelés-kérés | Megkérdezni, elégedett-e a vásárló, és csillagos értékelést/véleményt kérni, minél kevesebb kattintással | Ha a termék tanulást igényel, tehető elé egy rövid használati emlékeztető: csökkenti a visszaküldést és javítja az értékelést |
| 2 | +5 nap az 1. után | UGC-kérés | Felhasználói tartalom kérése: kép a termékkel, előtte-utána fotó, rövid videó vagy saját sztori; közösségi hangú, a márka köré hívja a vásárlót | Adható ösztönző (sorsolás, apró kedvezmény), de nem kötelező, sokan enélkül is szívesen megosztanak |

## Elágazások

- Jó értékelés/válasz esetén → „nagykövet" címke, hogy később külön megkeresés jöhessen (hosszabb testimonial, újabb felhívás, nagyköveti program).
- Rossz értékelés (1-2 csillag) esetén → ne menjen tovább a szokásos úton, irányítsd ügyfélszolgálat felé, kérdezd meg mi ment rosszul, adj esélyt a javításra.

## Mire figyelj

- Az időzítés kulcskérdés: túl korán felületes a válasz, túl későn elhalványul az élmény.
- Ez a bizalomépítés folytatása, nem eladás; ha csak folytatod az értékesítést, azt üzened, hogy csak a pénze kellett.
- Legyen sorrend: előbb a kételyt oszlatod el és megerősíted a döntést, csak utána jön a véleménykérés.
- Tartsd könnyen kitölthetőnek az első levelet, minél kevesebb kattintás, annál több válasz jön.
- Külön review-platform (Yotpo, Stamped, Okendo) esetén ugyanez a logika áll emailből is.

## Kontextus-igény

- A kézbesítési adat elérhetősége (mikor ért a termék a vásárlóhoz).
- Visszaküldés/sztornó-adat a kizáráshoz.
- Van-e külön review-platform integráció.
- Van-e ösztönző (kedvezmény, sorsolás) az UGC-kéréshez.

---

# Utánrendelés · flow-kártya (forrás: 34-es lecke)

**Mikor ajánld:** webshopoknak, akiknek van rendszeresen elfogyó, fogyóeszköz jellegű terméke (pl. táplálékkiegészítő). A lecke szerint akkor felesleges, ha a webshop egyébként is rendszeresen kampányol, mindig van valamilyen ajánlat aktívan futó hírlevél-szinten.
**Trigger:** kiszállítás (nem a rendelés leadása) után X nap, a becsült fogyási ciklusra időzítve, kicsit korábbra. Ne induljon, ha a vásárló időközben már rendelt.
**Terjedelem:** 3 email, a fogyási ciklushoz igazítva; a lecke csak azt adja meg, hogy a 2. és 3. levél „pár nappal", illetve „még pár nappal" később megy, konkrét napszámot nem tanít.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | Becsült fogyásra időzítve | Utánrendelés / kereszt-ajánlat | Fogyó terméknél a kényelem a fő üzenet: egy kattintás, régi tétel a kosárban, ideális esetben pénztárhoz vivő linkkel. Kiegészítő terméknél: „ezt vetted, ezt szokták hozzá venni" | Kis kedvezmény vagy időkorlát nem kötelező, de növeli az azonnali kattintás esélyét |
| 2 | Pár nappal az 1. után | Kereszt-ajánlat más kategóriából | Egy még nem birtokolt kategóriából ajánl, a kosarat tágítja másik irányba, megmutatja mi mást is csinál a márka | Fő üzenet: „ezt is sokan viszik hozzá" |
| 3 | Még pár nappal később | Hűség / erősebb ajánlat | Visszatérő vásárlót jutalmaz: hűség-pont, VIP-státusz vagy egyedi ajánlat csak korábbi vásárlóknak; a sorozat legerősebb kedvezménye | Az üzenet az elismerés, hogy nem először vásárol |

## Elágazások

- Ha bármelyik levélre vásárol → a flow nem zárul, hanem a vásárlás újraindítja a ciklust az elejéről, a következő fogyás vagy kiszállítás után újra belép. A termékajánlás is a saját vásárlásához igazodik, más fő terméknél más irányú kiegészítő megy.
- Ha nem történik vásárlás → visszakerül a heti hírlevél-ritmusba a következő vásárlásig, ami újraindítja a ciklust.

## Mire figyelj

- Csak akkor éri meg igazán, ha van tényleges fogyási ciklusú termék; kiegészítő terméknél, fogyási ciklus nélkül, koncentráld a flow-t a vásárlás utáni néhány hétre.
- Ha rendszeresen kampányolsz és mindig van ajánlatod, ez a flow feleslegessé válhat.
- Ismétlődő körben ne legyen ugyanaz az értékadó levél, mert az furcsa.
- Néha ellenőrizd, hogy a ciklus-becslés még mindig helyes-e, főleg ha változott a kiszerelés vagy a vásárlói szokás.
- Elhatárolás: ez NEM a vásárlás utáni (32-es lecke) azonnali upsellje; az rögtön a rendelés után megy, ez a kiszállítás után, hosszabb késleltetéssel, a fogyási ciklusra időzítve.

## Kontextus-igény

- Van-e fogyó/elhasználódó fő termék, és mennyi az átlagos fogyási ideje.
- Van-e rendszeres kampányolás vagy hírlevél-ajánlat (ha van, a flow létjogosultsága megkérdőjeleződik).
- Milyen kereszt-kategóriák/kiegészítő termékek tartoznak az egyes főtermékekhez.
- Van-e hűség-program vagy VIP-státusz, amit a 3. levélben fel lehet kínálni.

---

# Villámakció · flow-kártya (forrás: 35-ös lecke)

**Mikor ajánld:** webshopoknak, amikor egy naptárhoz kötött, rövid ablakban nyíló kedvezményt hirdetnek a meglévő kínálatra (szezonális esemény, saját kreált esemény, vagy áremelés előtti utolsó esély), nem új terméket vezetnek be.
**Trigger:** akció-ablak indul (szezon, Black Friday, áremelés előtti utolsó esély). Ne menjen annak, aki ebben az akcióban már vásárolt, vagy már végigment a leveleken.
**Terjedelem:** 7 email, az akció-ablak hosszához igazítva; a levelek nem egyenletesen oszlanak el, elején lazábban, a vég felé egyre sűrűbben, a záró napon akár 2-3 levél is mehet.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | Az ablak megnyitása előtt | Soft-promo | Jelzi, hogy készül valami, megmutatja mekkora érték jön, felkelti a figyelmet | Még nem fedi fel a kedvezményt |
| 2 | Az ablak nyitásakor | Ajánlat | Felfedi a kedvezményt és a kódot, kristálytisztán: mi az ajánlat, meddig tart, mit kell tenni | Lehet rövid vagy hosszabb, de az ajánlat legyen a lényeg |
| 3-5 | Az ablak közepén, sűrűsödő ütemben | Social proof / kifogáskezelő | Ugyanaz a kedvezmény, de minden levél más terméket, más előnyt vagy más keretet emel ki; egy levél kifogás-kezelő | Sorra veszi mi tartja vissza az embereket és válaszol rá; mindig legyen ok az olvasásra, ne csak „AKCIÓ" |
| 6 | Utolsó teljes nap | Sürgetés | Eszkalált sürgetés, egyértelműen kimondva, hogy ez az utolsó teljes nap; a kedvezmény-keret átfordítható „elveszíthető" keretbe | Az emberek jobban félnek elveszíteni valamit, mint lemaradni egy kedvezményről |
| 7 | Lejárat előtti utolsó órák | Zárás (visszaszámláló) | Rövid, direkt, órákban/percekben sürget, jól látható visszaszámlálóval | Jellemzően a lejárat előtti utolsó órában megy |

## Elágazások

- Ha a vásárló a határidő alatt vásárol → átvezetés a vásárlás utáni flow-ba, ne maradjon az akció-listán.
- Ha nem vásárol a határidőig → visszakerül a rendes hírlevél-ritmusba.

## Mire figyelj

- A launch-hoz (23-as lecke) képest itt nem új terméket vezetsz be, hanem a meglévő kínálatra nyitsz kedvezményes ablakot, az erejét a határidő adja.
- A közös launch-elvek is érvényesek: valódi naptári határidő, egy levél egy szög, a záró nap sűrít, ne fedd fel mindent az elején.
- Ugyanazt az akciót forgatod, nem ismétled: egyetlen ajánlat, több szögből bemutatva.
- A határidő legyen valódi, hamis határidőt soha ne adj, a lista átlátja.
- Legyenek olyan időszakok is, amikor teljes áron kapható a termék, különben arra tanítod a vásárlóidat, hogy sose vegyenek teljes áron.
- A sűrű levél-ritmus ne csússzon egybe más flow-k leveleivel.

## Kontextus-igény

- Az esemény/apropó és a pontos akció-ablak (kezdő és záró dátum).
- A kedvezmény mértéke és a kód.
- Mely termékkategóriák/termékek kerülnek elő a 3-5. levelekben más szögekből.
- A leggyakoribb vásárlói kifogások, amikre a kifogáskezelő levél válaszol.

---

# Készlet-értesítő · flow-kártya (forrás: 36-os lecke)

**Mikor ajánld:** webshopoknak, amikor egy keresett termék elfogy és a logisztika csúszik; azoknak a feliratkozóknak szól, akik már döntöttek a termék mellett, csak a készlet hiányzik.
**Trigger:** feliratkozás egy elfogyott termék „szólj, ha újra kapható" értesítőjére. Ne induljon el, ha a vásárló közben máshol megvette, vagy ha csak duplikált feliratkozás történt ugyanarra a termékre.
**Terjedelem:** 3 email; az 1. a feliratkozás után 5 perccel megy, a 2. a készlet visszaérésekor (változó időpont), a 3. az előző után +1 nap.

## Slotok

| # | Időzítés | Email-típus | A levél célja | Variánsok / megjegyzés |
|---|---|---|---|---|
| 1 | Feliratkozás után +5 perc | Visszaigazolás | Megerősíti a feliratkozást, és mellétesz egy másik, éppen elérhető, hasonló igényt kielégítő terméket | Csak akkor, ha van releváns alternatíva; olyanoktól is hozhat bevételt, akik amúgy nem várnának ki |
| 2 | A készlet visszaérésekor | Eladás | A sorozat fő pillanata, legmagasabb konverziójú levél: tiszta felépítés, egyetlen erős gomb a termékre, semmi felesleges körítés | Aki idáig várt, készen áll |
| 3 | +1 nap a 2. után (ha nem vásárolt) | Sürgetés | Végső lökés: azon a hangsúly, hogy egyszer már kimaradt, amikor a termék elfogyott, ne ismétlődjön | Csak akkor küldd, ha valóban korlátozott a mennyiség, vagy tényleg gyorsan fogy |

## Elágazások

- Ha a 2. vagy 3. levélre vásárol → átvezetés a vásárlás utáni flow-ba.
- Ha egyikre sem reagál → visszakerül a normál hírlevél-ritmusba, legközelebb máshogy vagy más csatornán próbálod elérni.

## Mire figyelj

- Ne hagyd üresen a várakozást: a hagyományos egy-leveles készlet-értesítő üres időt hagy, ami pénzt veszít.
- A sürgetés csak akkor hiteles, ha igaz. Ez az egyetlen flow, ahol a feliratkozó pontosan tudja, hogy már várt egy hiányra; egy hamis „mindjárt elfogy" üzenet itt a legtöbbet árt a bizalomnak.
- Itt nincs meggyőzési munka, csak jó időzítés kell, mert a feliratkozó már döntött, csak a készlet hiányzott.
- Rövid, de bevétel-érzékeny sorozat, a három levél pontosan annyit tesz, amennyi kell.

## Kontextus-igény

- Van-e a webshop-szoftverben beállítható „szólj, ha újra kapható" feliratkozás.
- Van-e a hiányzó termékhez hasonló igényt kielégítő, éppen elérhető alternatíva.
- Tényleg korlátozott-e a visszatérő készlet mennyisége (a 3. levél sürgetéséhez).
- A készlet visszaérésének várható időzítése/gyakorisága.
