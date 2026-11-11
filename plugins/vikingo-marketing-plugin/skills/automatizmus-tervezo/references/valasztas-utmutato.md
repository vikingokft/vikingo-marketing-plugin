# Flow-választási segéd

> Ezt MINDIG töltsd be az elején. Innen választasz flow-t (vagy ajánlasz egyet a felhasználó céljára), a kiválasztott flow kártyáját pedig a megfelelő kártya-fájlból töltöd be.

## Flow-index

| Flow | Kártya-fájl | Mikor ez a jó választás |
|---|---|---|
| Üdvözlő sorozat (21) | flow-kartyak-szakertoi.md | Első sorozat minden feliratkozónak; sima, ajánlat nélküli csali után |
| Gondozó sorozat (22) | flow-kartyak-szakertoi.md | Az üdvözlő/csali-sorozat UTÁN, folyamatos örökzöld kapcsolat, ha még nincs rendszeres hírlevél |
| Termékbevezető / launch (23) | flow-kartyak-szakertoi.md | Fix időablakban nyitott-zárt ajánlat a meleg listának |
| Újraaktiválás (24) | flow-kartyak-szakertoi.md | Régóta nem nyitó feliratkozók; lista-tisztítás, kézbesíthetőség |
| Csali-tölcsér (25) | flow-kartyak-szakertoi.md | Csali + rá épülő azonnali, kisebb elköteleződésű fizetős ajánlat |
| Webinár-tölcsér (26) | flow-kartyak-szakertoi.md | Élő webinár köré épülő regisztráció + előmelegítés + utókövetés |
| Kihívás-tölcsér (27) | flow-kartyak-szakertoi.md | Nagy értékű ajánlat, napi feladatos, több alkalmas előmelegítés |
| Deadline Funnel (28) | flow-kartyak-szakertoi.md | Örökzöld ajánlat személyenkénti határidővel; CSAK érett, csapatos cégnek |
| Webshop üdvözlő, kuponos (29) | flow-kartyak-webshop.md | Popup-feliratkozás kedvezményért; cél az első vásárlás |
| Kosárelhagyás (30) | flow-kartyak-webshop.md | Megkezdett, be nem fejezett fizetés megmentése |
| Tranzakciós (31) | flow-kartyak-webshop.md | Rendelés-státusz emailek tudatos felépítése |
| Vásárlás utáni (32) | flow-kartyak-webshop.md | Köszönet + onboarding a vásárlás után, újravásárlás megalapozása |
| Vélemény / UGC (33) | flow-kartyak-webshop.md | Értékelés és felhasználói tartalom gyűjtése kézbesítés után |
| Utánrendelés (34) | flow-kartyak-webshop.md | Fogyóeszköz jellegű termék újrarendelése a fogyási ciklusra időzítve |
| Villámakció (35) | flow-kartyak-webshop.md | Naptári apropójú, rövid kedvezmény-ablak a meglévő kínálatra |
| Készlet-értesítő (36) | flow-kartyak-webshop.md | „Szólj, ha újra kapható" feliratkozás kiszolgálása |

**Gyors döntési szabályok:**

- Webshop vagy szakértő/szolgáltató/kurzus? Ez az első szűrő: a két család két külön fájl.
- Csali ajánlattal → 25; csali ajánlat nélkül → 21.
- Élő esemény van benne → 26 (egy alkalom) vagy 27 (több nap, feladatokkal).
- Ha a felhasználó „ügyfélszerző rendszert" mond konkrét flow nélkül: kérdezd meg, csali / webinár / kihívás alapú-e, és az életút-térképből mutasd meg, hova illeszkedik.

## Üzleti modell → flow-család térkép

| Üzleti modell | Flow-család | Megjegyzés |
|---|---|---|
| **Webshop** (fizikai vagy digitális termékek, kosaras vásárlás) | Webshop-kártyák (29-36) | Ha van edukációs oldala is (pl. tartalommal ad el), a szakértői üdvözlő/gondozó (21-22) is releváns mellé |
| **Kurzus / oktató / szakértő** | Szakértői kártyák (21-28) | A kurzus-launch = 23; webinárral / kihívással eladott kurzus = 26 / 27 |
| **Szolgáltató** (ügynökség, tanácsadó, kivitelező) | Szakértői kártyák (21-28) | A „vásárlás" gyakran ajánlatkérés vagy időpontfoglalás; a CTA-kat erre kell cserélni a tervben |
| **Szoftver / előfizetés (SaaS)** | Szakértői kártyák ADAPTÁLVA | ⚠️ A kurzus nem tanít SaaS-specifikus flow-t. Analógiák: trial-regisztráció = üdvözlő + onboarding (21 + a 32 onboarding-logikája); trial lejárata = SZEMÉLYENKÉNTI határidő, ezért a 28-as (Deadline Funnel) logikája a közelebbi analógia, a 23-as launch sürgetés-szabályaival kiegészítve; lemorzsolódó felhasználó = újraaktiválás (24); feature-bejelentés = launch (23). SaaS-nál a kártya-lista fölé egy kiegészítő kérdés szinte mindig kell: mi a termékhasználati aktivitás-jel (mit csinál a felhasználó a trialben, ami jósolja a vásárlást). A tervben mondd ki, hogy adaptáció, és a sablon „Eltérések a kártyától" szekciójában tételesen jelöld az eltéréseket |

Vegyes modellnél (pl. webshop + kurzus) kérdezd meg, MELYIK termékhez készül most az automatizmus, és aszerint válassz családot.

## Szakértői életút-térkép

Egy feliratkozó útja a vásárlásig, körülbelül nyolc hét alatt:

- Belépési pont: a feliratkozó letölt egy sima, ajánlat nélküli csalit, ez indítja az Üdvözlő sorozatot (4 email). Ha a csalira azonnali fizetős ajánlat épül, ott már a Csali-tölcsért (25) építsd, nem az üdvözlőt.
- Az üdvözlő sorozat vége után a feliratkozó belép a Folyamatos gondozó sorozatba (örökzöld, heti ritmus, a példában hétfőnként).
- A gondozás mellett csütörtökönként megy egy önálló hírlevél is, ez a heti kétcsatornás ritmus.
- Amikor a meleg listának megnyílik egy launch-ablak, a gondozó sorozatból átlépnek a Termékbevezető kampányba: prelaunch, nyitás, utolsó hét, zárónap.
- A launch alatt a gondozó sorozat és a hírlevél is csendes napokra vált, hogy csak a launch szóljon. Ez kiemelt szabály.
- Zárónapon a vásárlás átadja a feliratkozót az ügyfél-onboardingnak (vásárlás utáni flow).
- A Webinár-tölcsér (26) és a Kihívás-tölcsér (27) ebben az életútban a launch alternatívái vagy előmelegítő kiegészítői.
- A Deadline Funnel (28) nem önálló belépési pont, hanem technikai réteg egy örökzöld ajánlat fölé, ha a vállalkozás már elég érett.

**Építési sorrend szakértőnek:** 1. Üdvözlő sorozat → 2. Gondozó sorozat → 3. Termékbevezető kampány → 4. Webinár- vagy Kihívás-tölcsér (ha illik a profilhoz) → Csali-tölcsér bármikor, amint van rá épülő ajánlat → Deadline Funnel legutoljára.

## Webshop életút-térkép

Vásárlás előtti szakasz:

- A feliratkozás a kuponra elindítja a Webshop üdvözlőt. Ezzel párhuzamosan, ha a vásárló checkoutig eljut és otthagyja, elindul a Kosárelhagyás-létra is. A két automatizmus átfedhet, ezért el kell dönteni, hogy mindkettő fusson egyszerre, vagy kizárják egymást.
- Ha egyik automatizmus alatt sem vásárol, a kontakt visszaesik a hírlevél-ütembe, és onnan egy naptári Villámakció-ablak húzhatja be a vásárlást.
- A heti hírlevél a kupon- és kosár-automatizmusok mellett is fut, ezért kizárási szabályokra és csendes napokra van szükség, hogy ne ütközzenek.

Vásárlás utáni szakasz:

- A vásárlás pillanatában egyszerre indul a Tranzakciós sorozat és a Vásárlás utáni sorozat.
- A Tranzakciós sorozat kézbesítés-eseménye időzíti a Véleménykérést (+14 nap); jó értékelés esetén a vásárló nagykövet-címkét kap, a tartalma visszaforog a hirdetésekbe és a sales-oldalra.
- A fogyási ciklus vége indítja az Utánrendelést, amit minden újabb vásárlás újraindít.
- Elégedett vásárlóként a kontakt visszakerül a hírlevél-ütembe, és új vásárlási ciklusba lép. Arra kell figyelni, hogy a friss vásárló ne kapjon egyszerre túl sok emailt.

**Építési sorrend webshopnak:** 1. a belépő páros (Webshop üdvözlő + Kosárelhagyás) és a Tranzakciós + Vásárlás utáni sorozat (ezek hozzák a bevétel zömét) → 2. Véleménykérés és Utánrendelés (ha van fogyó termék) → 3. kiegészítő réteg: Villámakció (ha van naptári apropó) és Készlet-értesítő (csak visszatérő készlethiánynál).
