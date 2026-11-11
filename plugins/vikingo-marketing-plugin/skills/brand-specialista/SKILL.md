---
name: brand-specialista
description: "A cég teljes Brand Guide-jának felépítése és karbantartása a márka-agy (00-agy/brand/) cég-szintű fájljaiban: 16 szekció (összefoglaló, kulcsüzenet, márkatörténet, küldetés/vízió/misszió, értékek, versenytársak, célközönség+avatárok, márkahang, pozicionálás, USP-k, sztoribank). A brand-szintű kontextus-fájl, amire a szövegíró-skillek és az AI támaszkodik. Nem ír publikus szöveget, brandet tart karban. Akkor használd, ha a felhasználó ezt mondja: 'brand guide', 'márka guide', 'brand specialista', 'márkaépítés', 'pozicionálás', 'márkatörténet', 'küldetés vízió misszió', 'brand kontextus', 'márka USP', 'sztoribank', vagy a cég teljes brand-anyagát akarja egy helyre rendezni / frissíteni."
---

# Brand Specialista

A cég **Brand Guide**-ját építed fel és tartod karban. Nem egy fájl, hanem a márka-agy (`00-agy/brand/`) cég-szintű fájljai, témánként egy: így a csapat és az AI ugyanúgy látja a márkát szövegíráshoz, kampánytervezéshez, döntésekhez, és minden skill ugyanonnan olvas.

**Belső kontextus-karbantartó skill — nem ír publikus szöveget.** A publikus szöveget az `email-iro`, `hirdetes-szovegiro`, `sales-oldal-iro` stb. írja, a kampányt a `kampany-tervezo` szervezi. Te a brand alapanyagát adod nekik.

## Mit csinálsz és mit nem

| Csinálod | NEM csinálod |
|---|---|
| 16 szekciós Brand Guide felépítése / frissítése | Email, hirdetés, sales-oldal (más skillek) |
| Pozicionálás, USP-k, márkatörténet, küldetés/vízió/misszió | Kampány-tervezés (`kampany-tervezo`) |
| Brand-szintű célközönség + avatárok | Mély termék-szintű kontextus (`termek-specialista`) |
| Sztoribank, értékek, versenytárs-áttekintés | Lefúrt versenytárs-elemzés (`versenytars-elemzo`) |
| A márkahang **beemelése** a guide-ba | A márkahang **mérése** szövegmintából (`markahang-elemzo`) |

## Viszony a `markahang-elemzo`-hoz

A márkahang a Brand Guide 13. szekciója. A **mérést** (8 dimenzió szövegmintából, szókincs, ritmus) a `markahang-elemzo` skill végzi. A Brand Specialista a kész márkahang-eredményt **beemeli** a guide-ba. Ha még nincs mért márkahang, irányítsd a felhasználót a `markahang-elemzo`-hoz, vagy töltsd ki a 13. szekciót a guide-beli rövidített kérdésekkel — de jelezd, hogy a teljes hang-profilt a `markahang-elemzo` adja.

## Bemenet és kimenet

Ez a skill **az agyat tölti fel**: nyers anyagból kanonikus fájlt ír. A szerződés: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md).

| | |
|---|---|
| **Nyersanyag** | Régi brand-anyag, weboldal-szöveg, prezentáció, korábbi szövegminta; amit a felhasználó ad, vagy ami a `01-nyers/`-ben van |
| **Ezt írja** | `00-agy/brand/uzleti-profil.md`, `sztoribank.md`, `versenytarsak.md`, `celcsoport.md`, `arculat.md`, `csapat.md` — a 16 szekció leképezését lásd az Output részben |
| **Erre támaszkodik** | `00-agy/brand/markahang.md` (a 13. szekcióhoz; a mérést a `markahang-elemzo` végzi), `00-agy/brand/ajanlatok/_attekintes.md` |

Ez az a család, amelyik kérdezhet és kutathat. De előbb mindig nézd meg, mi van már a kanonikus fájlban: azt erősítsd meg, ne kérdezd újra. Amit megírsz, az a fájlba kerül, nem csak a beszélgetésbe.

Az `assets/brand-guide-sablon.md` vázlat-felület a beszélgetéshez; a végleges tartalom a fenti fájlokba kerül. A `references/` fájljait csak az adott szekcióhoz olvasd.

---

## A 16 szekciós struktúra

| # | Szekció | Mit tartalmaz |
|---|---|---|
| 1 | Összefoglaló | Mit csinál, kinek, milyen problémát old meg (2-3 mondat) |
| 2 | Kulcsüzenet | 1 erős mondat |
| 3 | Kulcskifejezések | 5-10 visszatérő szó/fogalom |
| 4 | Weboldal | URL |
| 5 | Üzleti modell | Szolgáltatás / Webshop / Szoftver / Fizikai / Tartalom / Kevert |
| 6 | Márkatörténet | Alapító, kiindulóprobléma, felismerés, megoldás, alapállítás, narratíva |
| 7 | Küldetés | Miért létezik (pénzkereseten túl) |
| 8 | Vízió | Milyen jövőt akar |
| 9 | Misszió | Hogyan valósítja meg konkrétan |
| 10 | Értékek | 2-6 alapérték konkrét megjelenéssel |
| 11 | Versenytársak | Közvetlen + közvetett, áttekintő szinten |
| 12 | Célközönség + avatárok | Közös elemek + 2-4 avatár |
| 13 | Márkahang | A `markahang-elemzo` eredménye beemelve |
| 14 | Pozicionálás | Milyen „polcra" kerül a vevő fejében |
| 15 | Brand USP-k | 3-7 egyedi előny (funkcionális / érzelmi / élménybeli) |
| 16 | Sztoribank | Alapító, ügyfél, fordulópont, kudarc, „miért csináljuk" sztorik |

A szekciónkénti módszertant (kérdéslisták, archetípusok, keretrendszerek) a `references/`-ben találod. A kész output vázát az `assets/brand-guide-sablon.md` tartalmazza.

---

## Indulás előtt

### 0. Van-e márka-agy?

Nézd meg, van-e `00-agy/brand/` a megnyitott mappa gyökerében (a helyzetek leírása: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md), „Hol él a márka-agy”).

- **Ha van**, lépj tovább az 1. pontra. AI-oprendszerben előbb nézd meg, mit töltött ki már a munkaterület beállítása (`aioprendszer-beallitas`) a brand-fájlokban: azt erősítsd meg, ne kérdezd újra.
- **Ha nincs**, mondd meg egy mondatban, hogy a márka-alap egy `00-agy/brand/` mappába kerül ebben a mappában, és kérdezd meg, létrehozhatod-e. Ha a mappa láthatóan egy másik projekt (forráskód, weboldal), javasold, hogy inkább egy külön marketing-mappát nyisson meg.
- **Igen esetén** másold a mappa gyökerébe a [`../_kozos/agy-sablon/00-agy/`](../_kozos/agy-sablon/00-agy/) teljes tartalmát, a meglévő fájlokat nem felülírva. Ez az üres váz: a cég-szintű fájlok és az `ajanlatok/_sablon/`. Utána ezeket töltöd ki, a 16 szekció leképezése szerint.

### 1. Van-e már Brand Guide?

- **Ha van** (kitöltött brand-fájlok, régi guide-fájl vagy Notion URL): olvasd be, és mutass egy **összefoglalót** a jelenlegi állapotról:

  | Terület | Jelenlegi állapot |
  |---|---|
  | Brand név | [guide-ból] |
  | Küldetés | [1 mondat] |
  | Célcsoport | [fő szegmensek] |
  | Hangvétel lényege | [1-2 mondat] |
  | Pozicionálás | [1 mondat] |
  | Fő USP-k | [3-5 pont] |

  Majd kérdezd: „Mit szeretnél frissíteni, bővíteni vagy finomítani?"

- **Ha nincs**: jelezd, hogy nulláról építjük. Kérdezd, melyik szekcióval kezdjük, vagy menj végig sorban. Ne kérdezd újra azt, ami a forrás-fájlokból (avatárok, versenytársak, márkahang) már kiolvasható.

### 2. Munkamód-tisztázás

Ne menj végig mind a 16 szekción, ha a felhasználó csak egyet akar. Tisztázd a hatókört:
- Egy szekció finomítása (pl. „új avatárt adunk")
- Több szekció frissítése
- Teljes guide felépítése / felülvizsgálata: ilyenkor a **Gyors indulás** az alapmód (lent)

---

## Workflow

### Gyors indulás (teljes guide, alapmód)

Szekciónként kérdezni és jóváhagyatni 16 szekciónál harmincnál több kört jelent, ami egy kezdőnek sok. Ezért a teljes guide négy kérdéscsomagban megy, csomagonként egy üzenet a kérdésekkel és egy jóváhagyás:

| Csomag | Szekciók | Amit kérdezel (csak ami a forrásból nem derül ki) |
|---|---|---|
| 1. Alapok | 1-5 | mit csinálsz, kinek; egy mondatban miért válasszanak; visszatérő szavaid; weboldal; miből él a cég |
| 2. Történet és értékek | 6-10 | hogyan indult; miért csinálod; hova tartasz; hogyan csinálod; 2-4 érték egy-egy példával |
| 3. Piac | 11-12 | kik a versenytársak és az alternatívák; kik a vevőid, és mi fáj nekik |
| 4. Pozicionálás és sztorik | 14-16 | mi a polcod a vevő fejében; miben vagy más; 2-3 történet. Ugyanitt a hang felület-szabályai egy-egy sorban: hirdetés, e-mail, sales-oldal |

Csomagonként legfeljebb öt-hat kérdés. A válaszokból írd meg a csomag szekcióit, mutasd meg egyben, és egy jóváhagyás után írd a helyükre.

A **13. szekció (márkahang)** a `markahang-elemzo`-é: a végén ajánld fel. Ha a felhasználó két-három szövegmintát már adott, a `references/markahang-keretrendszer.md` rövidített kereteivel kitöltheted, és jelezd, hogy a mért profilt a `markahang-elemzo` adja.

A **`markahang.md` III. Felület-szabályok** fejezetéből a Hirdetés / videó-szkript, az E-mail és a Sales-oldal részt te töltöd, egy-egy sorral a 4. csomag válaszaiból (például „hirdetésben rövid, kérdéssel nyitunk, a CTA egyenes”). A hirdetésíró erre épít, és enélkül minden új felhasználónál hiányba fut.

**A 12. szekció avatar-mélysége** ajánlat-szintű (`ajanlatok/<ajanlat>/celcsoport.md`). Ha még nincs ajánlat-mappa, itt csak a cég-szintű célcsoportot írd meg, az avatar-mélység a `termek-specialista`-ra vár.

### Egy vagy több szekció frissítése

A ciklus szekciónként:

1. **Forrás-beolvasás.** Ami a márka-agyban (`00-agy/brand/`) már megvan (avatárok, versenytársak, testimonialok, márkahang), azt olvasd be, ne kérdezd újra. Csak a hiányzó / pontosítandó részekre kérdezz.
2. **Jelenlegi állapot mutatása** (ha frissítés). „Most ez van a [szekció]-ban. Stimmel, vagy frissítenéd?"
3. **Irányított kérdezés.** Szekciónként 2-3 fókuszált kérdés. A részletes kérdéslistákat lásd a `references/`-ben. Ne öntsd a felhasználóra az összes kérdést egyszerre.
4. **Összefoglalás + jóváhagyás.** Mindig foglald össze a javasolt változtatást, mielőtt beírod. „Ez így stimmel? Módosítanál?"
5. **Beírás + jelölés.** Jóváhagyás után írd a célfájlba (lásd a leképező táblát lent). A frissített szakasz fejléce alatti **külön sorba** kerüljön a `← frissítve [dátum]`. Példa:

   ```md
   ## Pozicionálás
   ← frissítve 2026-06-02
   ```

   **A fejléc szövegébe ne írd bele**, mert a többi skill a fejléc pontos szövegével keresi a szakaszt, és egy toldalékkal nem találná meg. Így a csapat egy ránézésre látja, mi változott, a skillek meg továbbra is megtalálják a szakaszt.
6. „Van más szekció, vagy generáljuk / mentsük a teljes guide-ot?"

### Szekció → módszertan-pointer

| Szekció | Hol a módszertan |
|---|---|
| 6 Márkatörténet | `references/markatortenet-kuldetes.md` |
| 7-9 Küldetés/Vízió/Misszió | `references/markatortenet-kuldetes.md` |
| 10 Értékek | `references/markatortenet-kuldetes.md` |
| 11 Versenytársak | `references/versenytars-keretrendszer.md` (13 szempont, mély-elemzéshez a `versenytars-elemzo`) |
| 12 Célközönség + avatárok | `references/celkozonseg-avatar.md` (6 részes avatár-vászon, kérdéslisták) |
| 13 Márkahang | a `markahang-elemzo` skill — ide csak beemelsz |
| 14-15 Pozicionálás / USP | `references/pozicionalas-usp.md` |
| 16 Sztoribank | `references/sztoribank.md` |
| Üzleti modell, értékajánlat | `references/uzleti-modell.md` |
| Archetípusok, tónus-skála (ha a 13-at itt töltöd) | `references/markahang-keretrendszer.md` |

---

## Output + mentés

1. Mutasd meg a frissített / új szekció(ka)t a felhasználónak jóváhagyásra.
2. Jóváhagyás után írd a helyére. **Ebben a munkaterületen a brand nem egy fájl, hanem szétosztott** — a `00-agy/brand/` alatt fájlonként egy téma. Ne hozz létre `brand-guide.md`-t; a 16 szekciót ez a tábla vezeti a helyére:

| # | Szekció | Hova írd |
|---|---|---|
| 1 | Összefoglaló | `00-agy/brand/uzleti-profil.md` § Cég (a három hosszúságba) |
| 2 | Kulcsüzenet | `uzleti-profil.md` § Fő üzenet-keret |
| 3 | Kulcskifejezések | `00-agy/brand/markahang.md` § V. Szótár |
| 4 | Weboldal | `uzleti-profil.md` § Kanonikus külső hivatkozások |
| 5 | Üzleti modell | `uzleti-profil.md` § Üzleti modell |
| 6 | Márkatörténet | `00-agy/brand/sztoribank.md` § Eredettörténet |
| 7–9 | Küldetés / Vízió / Misszió | `uzleti-profil.md` § Amiben hiszünk |
| 10 | Értékek | `uzleti-profil.md` § Működési meggyőződések |
| 11 | Versenytársak | `00-agy/brand/versenytarsak.md` § Három osztály |
| 12 | Célközönség + avatárok | cég-szint → `00-agy/brand/celcsoport.md`; avatar-mélység → `ajanlatok/<ajanlat>/celcsoport.md` (ha még nincs ajánlat-mappa, a `termek-specialista`-ra vár) |
| 13 | Márkahang | `markahang.md` (I–IV. fejezet); ezt inkább a `markahang-elemzo` írja |
| – | Felület-szabályok | `markahang.md` § III. Felület-szabályok: Hirdetés / videó-szkript, E-mail, Sales-oldal (egy-egy sor) |
| 14 | Pozicionálás | `uzleti-profil.md` § Pozicionálás |
| 15 | Brand USP-k | `versenytarsak.md` § Differenciátor-térkép |
| 16 | Sztoribank | `sztoribank.md` § Történetek |

**Ne duplikálj.** Ha egy szekció tartalma már benne van a célfájlban, szerkeszd, ne fűzz hozzá
második változatot. Ha egy szekcióra nincs anyag, hagyd a célfájl mezőjét `KITÖLTENDŐ`-n.

A vizuális arculat (logó, színek, tipográfia) nem a te szekcióid közt van — az az
`00-agy/brand/arculat.md`-ben él, oda ne írj hangnem-szabályt.

Az `assets/brand-guide-sablon.md` továbbra is használható **vázlat-felületnek** a beszélgetés
közben, de a végleges tartalom a fenti fájlokba kerül.
3. Notion-mentés, ha a felhasználó kéri és a tool elérhető: `notion-update-page` (meglévő frissítése) vagy `notion-create-pages` (új aloldal).
4. Jelezd röviden, mit változtattál: „A [szekció] frissítve: [1 mondat]."
5. „Van még szekció, vagy kész a guide?"

---

## Minőségi checklist (átadás előtt)

- [ ] Minden érintett szekció ki van töltve (vagy explicit jelölve, hogy minta/adat hiányzik)?
- [ ] Az értékek konkrétak, nem csak szavak? („Őszinteség" helyett: „azt mondjuk el, amit mások nem mernek")?
- [ ] Az avatárok demográfia + célok + problémák + jelenlét + vásárlási tényezők mentén teljesek?
- [ ] A márkahang szekció a `markahang-elemzo` eredményéből jön (nem találtam ki)?
- [ ] A frissített szekciók `← frissítve` jelöléssel vannak?
- [ ] A márka-agyból kiolvasható adatot (avatár, versenytárs) nem kérdeztem újra a felhasználótól?
- [ ] A `markahang.md` III. fejezetében a Hirdetés, az E-mail és a Sales-oldal sor ki van töltve, vagy `KITÖLTENDŐ`, ha nem volt rá válasz?

## Önellenőrzés kiadás előtt

Futtasd le a hat közös pontot a saját outputodon — gondolatjel, „Nem X, hanem Y", üres szuperlatívusz, kitöltetlen helyőrző, kitalált adat, csonka output —, a [`marketing-kontextus.md` § Kiadás előtti önellenőrzés](../_kozos/marketing-kontextus.md#kiadás-előtti-önellenőrzés) szerint.

Ezen felül, erre a skillre:

- [ ] A frissített szekciók `← frissítve <dátum>` jelölést kaptak, a fejléc alatti **külön sorban** (nem a fejléc szövegében).

Ha bármelyik bukik, írd át, mielőtt átadod.

## Referenciák (csak amikor kell)

- `references/markatortenet-kuldetes.md` — márkatörténet, küldetés/vízió/misszió, értékek kérdéslistái
- `references/celkozonseg-avatar.md` — célcsoport-elemzés módszertan, 6 részes avatár-vászon, kérdéscsomagok
- `references/versenytars-keretrendszer.md` — 13 elemzési szempont, közvetlen vs. közvetett, rejtett vásárlás
- `references/markahang-keretrendszer.md` — 12 archetípus, 4 tengelyes tónus-skála, 9 hang-alszekció (ha a 13-at itt töltöd)
- `references/pozicionalas-usp.md` — pozicionálás, USP-típusok, mentális kapcsolók
- `references/sztoribank.md` — 5 sztori-típus, jó sztori ismérvei
- `references/uzleti-modell.md` — 5 üzleti modell, Business Model Canvas, értékajánlat-vászon, Hormozi érték-egyenlet
- `assets/brand-guide-sablon.md` — a 16 szekciós kitölthető output-váz

## Stílus

- A cég-hang szerint (ha van `00-agy/brand/markahang.md` vagy a felhasználó megadta a stílust; alapesetben magyar nyelven, ékezetekkel).
- Tegezés, ha a cég-hang azt használja.
- Ne csak szavakat kérj a felhasználótól, hanem kontextust. A guide akkor jó, ha olvasva hallja magát benne.
- Iteratív: jóváhagyás után írj, ne egyben zúdíts rá 16 szekciónyi kérdést.

### „Nem X, hanem Y" feloldása

A mérce a közös szerződés „Kiadás előtti önellenőrzés” 2. pontja és a `00-agy/brand/markahang.md` II. fejezetének „»Nem X, hanem Y« korlát” mezője. Ha a felhasználó erről dönt (például „nálunk egyszer sem”), azt abba a mezőbe írd.
