# Feladat Író — Workflow részletek

Gyors, nem fázisos workflow — a user diktál, te kiadsz egy strukturált feladatot.

## Tartalomjegyzék

1. [Diktálás fogadása + elem-azonosítás](#1-diktalas-fogadasa--elem-azonositas)
2. [Link-feloldás (Notion + Web)](#2-link-feloldas-notion--web)
3. [Hiány-check + visszakérdezés](#3-hiany-check--visszakerdezes)
4. [Output megírása](#4-output-megirasa)
5. [Szövegírás-check](#5-szovegiras-check)
6. [Példák](#peldak)
7. [Általános szabályok](#altalanos-szabalyok)

---

## 1. Diktálás fogadása + elem-azonosítás

A user feldiktál egy szöveget. Olvasd végig egyben, és jegyezd le mit fed:

| Elem | Példa a diktálásból |
|------|---------------------|
| **Mi a deliverable** | „kéne csinálni egy oldalt", „egy email szöveg", „átnézni a kampányt" |
| **Cél / kontextus** | „mert utána indul a hirdetés", „a kuncsaftnak kell" |
| **Forrás-anyag** | „a szöveg már megírtam Notionban", „az X-féle a referencia" |
| **Határidő** | „jövő péntekre", „mielőbb", „nem sürgős" |
| **Érintettek** | „[kolléga] csinálta a referenciát", „kérdezd [kolléga]-t" |
| **Bizonytalanság** | „nem tudom pontosan mennyi", „valami olyasmi", „majd kiderül" |

Ami nem hangzott el, az nincs. Ne találd ki.

---

## 2. Link-feloldás (Notion + Web)

### Notion oldalak

Ha a diktálás említ egy Notion oldalt / dokumentumot **név szerint** (pl. „a [projekt] v2 oldal", „a [kampány] doksi"), futtass egy `notion-search` MCP hívást a névvel és vedd ki a URL-t.

**Példa:**
- User: „a szöveget már megírtam Notionban, az oldal címe [Projekt] v2 vagy mi"
- Te: `notion-search` → query: „[Projekt] v2"
- Eredmény: első találat URL-je → ezt belinkeld

### Külső platform / weboldal / cégnév

Ha a diktálás link-szerű külső entitást említ **név szerint** (platform, cég, weboldal — pl. egy versenytárs neve, egy szoftver, egy publikus oldal), futtass egy `WebSearch` hívást a hivatalos főoldal URL-jére.

**Példa:**
- User: „meg kellene nézni [Versenytárs 1]-et, [Versenytárs 2]-t és [Versenytárs 3]-at"
- Te: `WebSearch` mindegyikre (egyszerre vagy batch-elve)
- Eredmény: hivatalos URL-ek → ezeket linkeld a megfelelő helyen a törzsben vagy a Linkek mezőben

### Közös szabályok

**Ha több találat van** és nem egyértelmű melyik a jó:
- Vagy listázd ki a top 2-3 találatot az output előtt és kérdezd meg melyik
- Vagy ha nyilvánvaló a kontextusból (pl. dátum, ügyfél neve, nyelv), válaszd ki

**Ha nincs egyértelmű találat:**
- Ne találj ki linket. Csak a nevet írd, és jelezd: „(URL bizonytalan, keresd elő)" — indoklás nélkül.
- **Ne állíts olyan keresési eredményt, amit a WebSearch/Notion nem adott vissza.** Ha nincs találat, ne fűzz hozzá kitalált magyarázatot („több hasonló nevű oldal van") — csak akkor írj „több találat van" típusú indoklást, ha a keresés ténylegesen több találatot adott.

**Ne** próbálj feltölteni Notionra. A skill csak olvas / keres.

---

## 3. Hiány-check + visszakérdezés

Mielőtt megírod az outputot, nézd meg mi kritikus de hiányzik. Csak ezekre kérdezz vissza:

- **Deliverable formátuma** ha nem egyértelmű (Notion oldal? PDF? HTML? Mockup?)
- **Határidő** ha úgy tűnik sürgős a diktálásból, de nem mondott dátumot
- **Felelős/átvevő** ha „a kollegáknak" homályos és tényleg kell tudnod hogy kinek (általában NEM kell — alapból a user majd átadja akinek akarja)

**Max 2-3 kérdést tegyél fel egyszerre.** Egyetlen üzenetben, listázva. NE menj 5-ös kihallgatásba.

**Példa visszakérdezés:**

> Mielőtt megírom, két dolog:
>
> 1. **Határidő:** mondtad hogy „mielőbb" — van konkrét dátum amit a kollégának látnia kell?
> 2. **Deliverable:** Notion oldal jó formátumnak, vagy inkább egy mockup / kész HTML?

**Ha nincs ilyen kritikus hiány**, ugorj át erre a lépésre — egyből írd meg az outputot. Ne kérdezz csak hogy kérdezz.

---

## 4. Output megírása

A SKILL.md-ben lévő sablont töltsd ki. Pár kulcs-szabály:

**Cím:**
- Főnévi forma („X elkészítése", „Y átnézése")
- Konkrét deliverable benne (ne „valami a kampánnyal", hanem „Sales oldal v2 elkészítése")

**Nyitó bekezdés (1-2 mondat):**
- Mi a cél + mi a deliverable
- A user szóhasználatával — ne fogalmazz át
- ❌ „Egy értékesítési oldal létrehozására irányuló feladat" — slop
- ✅ „Saját brand alatt is kéne a [termék] sales oldal — a szöveg már Notionban kész"

**Törzs:**
- 1-2 bekezdés folyó szövegben **vagy** 3-6 bullet, attól függően mit diktáltál
- Ha a diktálás 5 mondat volt, az output törzs is 2-4 mondat
- A user megfogalmazásai maradnak — csak töltelék („izé", „hú", „akkor figyelj", „mint amilyen") + ismétlés ki

**Vastagított mezőnevek (csak ha van mit írni mögé):**
- `**Határidő:**`
- `**Linkek / csatolmányok:**`
- `**Akin múlik / kérdés vissza:**`

**Üres mező = töröld a sort.** Nem írunk „Határidő: nincs megadva".

---

## 5. Szövegírás-check

Mielőtt átadod, gyors szövegírás-check. Ha van `00-agy/brand/markahang.md`, annak „Mit ne" szekciója a mérce; ha nincs, az alábbi beépített lista elég. Speciálisan figyelj:

- **Gondolatjel (— / –) mondat KÖZBEN** — tilos. Csak listajelölőként vagy párban (zárójel-szerűen) megengedett. Mondat közben cseréld vesszőre, kettőspontra, zárójelre, vagy bontsd két mondatra. (Ez a leggyakoribb, ismétlődő hiba — keress rá a karakterre az outputban.)
- **Igétlen tőmondatok** — „Két ujj." „Konkrét." → fűzd a következő mondathoz, vagy egészítsd ki
- **Hamis cselekvő / passzív** — „A feladat létrehozása megtörténik" → „Csináld meg X-et"
- **Meta-kommentár** — „Az alábbi feladat..." → töröld
- **Üres töltelék** — „fontos megjegyezni, hogy", „érdemes kiemelni", „a megfelelő"
- **Heading-túltagolás** — ha több mint 1 `#` címed van, túl sok

Ha bukik valamelyiken → javíts mielőtt átadod.

---

## Példák

### Példa 1 — Sales oldal

**Diktálás:**
> Hú, akkor figyelj, kéne csinálni egy oldalt, izé landing oldalt a [termék]-re, mint amilyen [referencia]-nak van, csak ezt most a saját brandünk alatt. A szöveget már megírtam Notionban, az oldal címe [Termék] v2 vagy mi, megtalálod. Jövő péntekre kéne hogy meglegyen, mert utána indul a hirdetés. Ja és [kolléga] csinálta a [referencia] oldalt szóval ha elakadsz nézd meg azt.

**Lépések:**
- Notion search: „[Termék] v2" → URL megvan
- Hiány-check: minden megvan (deliverable, határidő, forrás, referencia) → nincs visszakérdezés
- Output:

```
# [Termék] sales oldal elkészítése (saját brand)

A [referencia]-féle landing mintájára építsd meg a saját brandünk alatti változatot.

A szöveg már Notionban kész, neked az oldal-építés van.

---

A Notion oldalon van a teljes szöveg — abból dolgozz.

A [referencia]-féle verzió a referencia felépítésre, nem 1:1 másolat, brandünkre szabva.

**Határidő:** jövő péntek (utána indul a hirdetés)
**Linkek / csatolmányok:** [[Termék] v2 Notion oldal](https://www.notion.so/...)
**Akin múlik / kérdés:** [kolléga] csinálta a referencia oldalt — ha elakadsz, nézd meg azét vagy kérdezd.
```

### Példa 2 — Rövid task, semmi extra

**Diktálás:**
> Át kéne nézni a múlt heti hirdetés statot, csinálni belőle egy 3 bullet pontos összefoglalót nekem. Holnapra jó.

**Output:**

```
# Múlt heti hirdetés stat összefoglalása

Nézd át a múlt heti hirdetés-számokat és csinálj 3 bulletet a lényegről.

**Határidő:** holnap
```

Ennyi. Nincs szükség `---` választóvonalra vagy törzsre — a nyitó mondat elmondta amit kellett.

### Példa 3 — Bullet-listás tördelés + WebSearch

**Diktálás:**
> Azon gondolkodtunk, hogy milyen olyan kurzusok vannak, amiket be tudnánk hozni, amiket vagy mi tudnánk elkészíteni, vagy tudnánk szakértőket csinálni hozzá. Ennek az lenne a célja, hogy kicsit jobban tudjuk kommunikálni azt, hogy tartsa frissen az ember a tudását a [termék]-ben. Ehhez meg kellene nézni [Versenytárs 1]-et, [Versenytárs 2]-t, [Versenytárs 3]-at és [Versenytárs 4]-et. Kellene egy adatbázist csinálnia különböző címekről, linkekről; ezekben is tud az AI segíteni. Szóval, ha ráküldjük az oldalra, akkor a linkeket elég jól be tudja szedni, meg tudja nézni a sales oldalakat. Aztán lehetne értékelni őket, hogy mondjuk mi az, ami egyáltalán nem illik be, közepesen illik be, vagy teljesen beillik hozzánk. Lehet olyan, hogy ki az, aki tőlünk meg tudná csinálni. Lehet, hogyha tudunk valakire konkrét szakértőt, az meg tudná csinálni. Szóval erre kellene egy ilyen kis kutatást és egy ilyen összefoglalót, hogy ennek vajon hogy lenne értelme hozzánk.

**Lépések:**
- WebSearch a 4 platformra → URL-ek megvannak
- Hiány-check: nincs határidő, nincs név megadva ki a végrehajtó — de ezek nem kritikusak (kutatási feladat, a user dönti ki kapja)
- Tördelés: 4 platform → bullet. 3 értékelési szint → bullet. „Ki tudja megcsinálni" 2 alesete → bullet vagy mondat.

**Output:**

```
# Kurzusok átnézése — behozható témák feltérképezése

Nézzük meg milyen kurzusok vannak amiket be tudnánk hozni, amiket mi tudnánk elkészíteni, esetleg külsős szakértőkkel.

A cél hogy jobban tudjuk kommunikálni: a [termék]-ben tartsd frissen a tudásod.

---

Ehhez nézd át a következő platformokat:

- [[Versenytárs 1]](https://...)
- [[Versenytárs 2]](https://...)
- [[Versenytárs 3]](https://...)
- [[Versenytárs 4]](https://...)

Csinálj egy adatbázist a kurzusokról: cím + link.

Ebben az AI is tud segíteni — ha ráküldöd egy oldalra, a linkeket elég jól beszedi, és a sales oldalakat is meg tudja nézni hogy miről szól egy kurzus.

Aztán értékeld a kurzusokat több szempont szerint:

- Mennyire illik hozzánk — egyáltalán nem, közepesen, vagy teljesen
- Van-e valaki tőlünk aki meg tudná csinálni
- Vagy ismerünk-e konkrét szakértőt akit be lehetne hozni

Az egészből kell egy kis kutatás és egy összefoglaló: vajon hogy lenne értelme ennek nálunk.
```

**Miért így:**
- **Nincs „Összefoglaló:" címke** — a nyitó bekezdés közvetlenül a feladat
- **A cél külön bekezdésben** — két különálló gondolat, két bekezdés
- **`---` választóvonal** a nyitó és a részletek között
- **Bekezdés-tördelés agresszívebb** — „Csinálj egy adatbázist" és „Ebben az AI segíthet" KÜLÖN bekezdés, nem ugyanazon belül
- **4 platform → bullet** (nem zsúfolva egy mondatba)
- **Értékelési szempontok egy listában** — nem külön „értékelés" és „ki csinálná" szekció, hanem egy szempont-lista több ponttal. A 3 szint árnyalásként az első bulletben („egyáltalán nem, közepesen, vagy teljesen") — információ megmarad, struktúra letisztul.
- **Záró deliverable mondat** („kutatás + összefoglaló") megmarad — ez volt a végső eredmény amit kértek
- **A „be is linkelheti, ha tudja" meta-utasítás kihagyva** — a linkek megjelennek a WebSearch eredményeként, nem kell róla beszélni
- **A hossz a diktálás kb. 70-80%-a**, levegős

### Példa 4 — Bizonytalanság benne

**Diktálás:**
> Kéne egy email a feliratkozóknak a kihíváshoz, valami olyasmi mint múltkor volt csak az új kuponkóddal, és a kuponkód az most már nem tudom pontosan, kérdezd meg [kolléga]-t.

**Output:**

```
# Email a feliratkozóknak — kihívás (új kuponkód)

A múltkori kihívás-email mintájára egy új verzió, az új kuponkóddal.

A struktúra és hangvétel ugyanaz mint a múltkori — csak a kuponkód cserélődik az aktuálisra.

**Akin múlik / kérdés:** [kolléga] tudja az új kuponkódot — kérdezd el tőle indulás előtt.
```

---

## Általános szabályok

- A cég-hang nyelvén és megszólításában (alapesetben a diktálás nyelvén; ha van `00-agy/brand/markahang.md`, az dönti el a megszólítást/tegezést)
- Diktálás voice marad — csak strukturálsz, nem újraírsz
- Az kerülendő minták szabályok minden outputon érvényesülnek (ha van `00-agy/brand/markahang.md` „Mit ne", az a forrás; ha nincs, a fenti beépített check)
- Max 1 db `#` cím / output
- Üres mezőket törlünk, nem üresen hagyunk
- Notion-keresést használunk linkfeloldásra, de NEM töltünk fel oda
- Ha bizonytalan vagy hogy egy infó kellene-e még, max 2-3 visszakérdezés egyszerre
