# Termék Specialista: a fájlok kitöltése

> **A szerkezetet az ajánlat-mappa `_sablon/` fájljai adják** (`00-agy/brand/ajanlatok/_sablon/`). Ez a fájl csak azt írja le, mit írj az egyes szakaszokba, és honnan. Új, párhuzamos szerkezetet ne hozz létre, a szakaszokat ne nevezd át: az író-skillek név szerint keresik őket.
>
> **Üres-jel:** ami hiányzik, `KITÖLTENDŐ` (szakasz elején, vagy mezőértékként). Ami tudatosan nem használt, `nincs`. Más jelet (`—`, „nincs kitöltve”) ne használj, mert az öröklés és a hiány-protokoll csak ezt a kettőt ismeri ([`marketing-kontextus.md`](../../_kozos/marketing-kontextus.md)).
>
> A konkrét ár, garancia és kuponkód mindig ajánlat-szintű: két különböző árú ajánlatnál a cég-szintre visszaesés rossz árat adna. A cég-szintű `kontextus-elemek.md` csak a keretet tartja.

## Tartalom

1. [kontextus.md](#1-kontextusmd)
2. [Felelős, oktató](#2-felelős-oktató)
3. [celcsoport.md, kifogasok.md, uzenetek.md](#3-celcsoportmd-kifogasokmd-uzenetekmd)
4. [kontextus-elemek.md](#4-kontextus-elemekmd)
5. [A többi fájl](#5-a-többi-fájl)

---

## 1. kontextus.md

A `_sablon/kontextus.md` a narratíva: mechanika, érték, pozicionálás. Értéket (ár, garancia, terméknév) nem tartalmaz, arra hivatkozik.

| `_sablon` szakasz | Mit írj bele | Honnan |
|---|---|---|
| Mit ad el, és kinek | 2-3 mondat: a fő ígéret és a célcsoport | Szakasz 0 elemzés |
| Az ajánlat mechanikája | A folyamat, amin a vevő végigmegy, és hol érti meg az értéket. Alatta a terjedelem és a formátum (hány óra vagy nap, self-paced, kísért, 1:1), és `### Tartalmi egységek` alpontként egységenként egy sor (név, egy mondat, fő témák, mellékletek) | Szakasz 0 struktúra-parszolás, Szakasz 1 |
| Átalakulási útvonal | Az előtte → utána története: milyen lépéseken megy át. A két végpont értéke a `kontextus-elemek.md` „átalakulás” mezőjébe kerül | Szakasz 0 before-after |
| Miért működik | A mögöttes logika, amit a sales-szöveg érvelésként használ, és a landing Mechanizmus blokkja keres | Input-anyag, sales-narratíva |
| Értékpiramis | A négy szint (Funkcionális, Érzelmi, Életet megváltoztató, Társadalmi), szintenként 1-3 elem a [`modszertan.md`](modszertan.md) 30 eleméből. Elemenként: hogyan jelenik meg használat közben, és a termék után a mindennapokban. Üres szint maradhat `KITÖLTENDŐ` | Szakasz 0 javaslat, Szakasz 2 |
| Pozicionálás az ajánlat szintjén | Hol áll a vevő útján, mi előtte és utána ajánlott, melyik programhoz, kampányhoz kapcsolódik, ki tanítja (§2). Csalinál a **Szülő-termék** sor kitöltése kötelező | Szakasz 1 javaslat + jóváhagyás |
| Kiszállítás és teljesítési korlátok | Hogyan jut hozzá, hozzáférés, kohorsz, kapacitás | Input-anyag |
| Kizáró tényezők | Kinek nem jó, és az előfeltételek (tudás, eszköz, másik termék) | Szakasz 0, Szakasz 2 deal-killerek |

Ami nem ide tartozik, és hova kerül:

- vélemények, eredmények → `testimonialok.md`;
- célcsoport-profil → `celcsoport.md` (a `kontextus.md`-be ne másold, mert két példányból az egyik elavul);
- kész sales-oldal, sales-videó → a kimeneti helyen él (lásd a közös szerződés „Hova kerül a kész anyag” részét), az ajánlat `_attekintes.md`-jének „Kanonikus sales-anyagok” részébe csak a hivatkozás kerül;
- kulcskifejezések (top 20) → `uzenetek.md` „Üzenetmag-index” alá, vagy a célcsoport-nyelvhez, ha a vevő szavai.

## 2. Felelős, oktató

A profil kanonikus helye a `00-agy/brand/csapat.md`. Ha ott még nincs, oda írd (név, szerep, háttér, hitelességi elemek). Ebben az ajánlatban:

- a `kontextus.md` „Pozicionálás az ajánlat szintjén” részébe egy sor: ki tanítja, hivatkozással a `csapat.md`-re;
- a `kontextus-elemek.md` IV. `szakértő / tekintély` mezőjébe az ajánlat-specifikus hitelesség, 3-5 rövid sorban (amit ez a termék megmutat belőle).

## 3. celcsoport.md, kifogasok.md, uzenetek.md

A Szakasz 2 célcsoport-deltája három fájlba oszlik szét. Csak ami erre a termékre sajátos: amit a cég-szintű `00-agy/brand/celcsoport.md` már tartalmaz, ne ismételd.

**`celcsoport.md`:** a „Melyik szegmensnek szól” részbe a cég-szintű szegmens neve. Avatarra egy blokk a `_sablon` mezőivel:

| `_sablon` mező | Mit írj bele |
|---|---|
| `### [Avatar neve] — „[egy mondat a fejéből]”` | termék-specifikus név, az alap avatar neve zárójelben |
| Élethelyzet | 2-3 mondat, és a termék-specifikus problémák (3-5 pont) |
| Amit akar | termék-specifikus célok (3-5 pont): amit ez a termék ad neki |
| Amitől fél | a kifogások mögötti félelem |
| Deal-killer | mikor ne ezt ajánljuk neki (1-3 pont) |
| Messaging insight | belső monológ egy bekezdésben, a saját szavaival, utána egy mondatban a belátás |
| Vásárlási trigger | 2-4 esemény, amitől most keresni kezd |
| Hol érjük el | csatorna; ha nem tudod, `[becsült, megerősítendő]` |

**`kifogasok.md`:** a kifogás-cáfolat ide megy, az I. Belépési kifogások blokkjaiba, kifogásonként egy blokk (Mi van mögötte, Cáfolat, Bizonyíték hozzá, Hol kezeljük). 4-6 kifogás elég, a kategóriákból válogatva: ár, idő, bizalom, szükséglet, halogatás, technikai. Ami jogos, és nem cáfoljuk, az „Amit nem próbálunk megcáfolni” részbe kerül.

**`uzenetek.md`:** 3-5 üzenetmag a `_sablon` blokkjával. A termék-specifikus hookok a mag **Hookok** sorába kerülnek (3-5), váltogatva a négy típust:

1. **Érzelem-alapú:** a belső érzésre céloz.
2. **Probléma-alapú:** a konkrét akadályra mutat.
3. **Eredmény-alapú:** az elérhető kimenetre fókuszál.
4. **Kíváncsiság-alapú:** meglepetést ígér, és a következő mondat beváltja.

A mag **Melyik avatarnak** sora köti össze a célcsoporttal. Ha az `uzenetek.md` már ki van töltve, csak a hiányzó kapcsolatot írd be.

## 4. kontextus-elemek.md

A `_sablon/kontextus-elemek.md` I–VII. fejezetét töltöd, a rögzített mezőnevekkel (`### fő fájdalom` és társai). Szabályok:

- **Csak érték, nulla érvelés.** Magyarázó blokk, „mit jelent” sor nem kell: a változók definíciója a `hirdetes-szovegiro` skill `references/placeholder-registry.md` fájljában van.
- **Csak a delta.** Ami a cég-szintű `00-agy/brand/kontextus-elemek.md`-ben van és itt is ugyanaz, az maradjon `KITÖLTENDŐ`: onnan öröklődik. Az árat, a garanciát és a kuponkódot mindig itt add meg (vagy `nincs`).
- **Variánsok: 3-5 mezőnként**, ha van hozzá anyag. Több csak bőséges forrásnál, mert a sok variáns kitalálásra nyom. Ahol nincs anyag, a mező `KITÖLTENDŐ`.
- **Konkrét, termék-specifikus mondatok** a célcsoport saját szavaival, a `00-agy/brand/markahang.md` szerint. Az idézőjel `„…”` vagy `"…"`, egy fájlon belül egyformán; az angol `“…”` nem.
- **Következtetés jelölése:** amit nem az input-anyag vagy a felhasználó mondott, hanem te vezettél le (például „bármikor leiratkozhatsz”), az kapjon `(következtetés, erősítsd meg)` jelölést. A landing-szövegíró ellenőrzője ezt felismeri, és nem engedi ki tényként.

Minta egy mezőre:

```markdown
### fő fájdalom
- Este fáj a derekam, és nem tudom, mit csináltam rosszul.
- A gyógytorna-videókat mindig abbahagyom a harmadik napon.
- Félek, hogy rosszul csinálom, és csak rontok rajta.
```

### Deriválás

A változókat a többi fájlból vezesd le, ne kérdezd újra a felhasználót:

- Mechanika, tartalmi egységek → `csomag tartalma`, `feature / jellemző`, `konkrét tudás / készség`
- Célcsoport-delta → `megszólítás`, `szint / tapasztalat`, `vágy / aspiráció`, `identitás`, `fő fájdalom`, `félelem`, `akadály`, `rossz alternatíva`, `érzelmi benefit`
- Átalakulási útvonal → `átalakulás: előtte → utána`
- Értékpiramis → `érzelmi benefit`, `advantage / előny a versenytárssal szemben`, `fő eredmény / ígéret`
- Felelős, oktató → `szakértő / tekintély`
- Testimonialok → `eredménytörténet / testimonial`, `értékelés / review`
- Mit ad el, és kinek → `fő eredmény / ígéret`, `számszerű eredmény`, `időkeret`
- Pozicionálás → `sürgősség`, `lökés / záró érv`

A részletes heurisztikák: [modszertan.md](modszertan.md) „Kontextus-elemek deriválás”.

## 5. A többi fájl

- **`testimonialok.md`:** ha a felhasználó adott véleményt, az I. Idézhető visszajelzések blokkjába, szó szerint, az **Engedély** sorral. Engedély nélkül `KITÖLTENDŐ` marad az Engedély sor.
- **`_attekintes.md` (az ajánlaté):** Cél, Státusz, Következő lépés.
- **`00-agy/brand/ajanlatok/_attekintes.md`:** egy sor a portfólióba.
- **`versenytarsak.md`, `gyengesegek.md`:** csak ha az anyagból kiderül valami; különben maradnak `KITÖLTENDŐ`-n.
