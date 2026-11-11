# Hirdetés Szövegíró: Hirdetés Formulák

> 7 címsor típus, 10 elsődleges szöveg formula, platform formátumok, CTA rendszer, awareness szintek, tiltott minták.
> Részletes sablonok: `assets/sablonok/cimsor/` (7 fájl, 87 sablon) + `assets/sablonok/elsodleges-szoveg/` (10 fájl, 89 sablon)
>
> A táblázatokban szereplő példák illusztrációk — cseréld a saját termék/ajánlat adataidra (`[termek]`, `[ár]`, `[ügyfélszám]` stb.).

---

## 1. Platform formátumok

### Facebook / Meta Ads

| Elem | Limit | Megjegyzés |
|------|-------|-----------|
| **Címsor (Headline)** | 40 kar ajánlott | 25 felett mobilon 1 sorban, 40 felett csonkul |
| **Elsődleges szöveg (Primary text)** | 125 kar hajtás felett, max 1000 | Az első 125 kar a legfontosabb |
| **Leírás (Description)** | 30 kar ajánlott | Nem minden elhelyezésen látszik |
| **CTA gomb** | Előre definiált | Tudj meg többet / Regisztrálj / Vásárolj / Letöltés / Feliratkozás |

**Formázás:** Emoji mérsékelt (1-2 db), sortörések bekezdések között, link a végén VAGY CTA gombbal. Képen max 20% szöveg.

### Google Ads (Responsive Search Ads)

| Elem | Limit | Db |
|------|-------|----|
| **Címsor** | Max 30 kar | 3 kötelező (max 15) |
| **Leírás** | Max 90 kar | 2 kötelező (max 4) |
| **Display URL útvonal** | 2 × 15 kar | pl. [ceg-domain]/[termek]/[útvonal] |

**Szabályok:** Minden címsor önállóan értelmes (rendszer variálja). Felkiáltójel tilos címsorban. Max 1 felkiáltójel leírásban. Pontos ár feltüntetés kötelező.

### TikTok Ads

| Elem | Limit | Megjegyzés |
|------|-------|-----------|
| **Hirdetés szöveg** | Max 100 kar ajánlott | Rövid, natív hangvétel |
| **CTA gomb** | Előre definiált | Tudj meg többet / Regisztrálj / Letöltés |

**Stílus:** Natív, nem „reklám" jellegű. Informális, beszélgetős hang.

**Karakterszám-annotáció szabály:** Ha az outputban karakterszámot tüntetsz fel egy konkrét címsor / szöveg mellé (pl. „38 kar — Meta-limit alatt"), azt TÉNYLEGESEN számold meg a leadott szövegen. Becsült vagy találgatott szám rosszabb, mint a hiánya — ha nem számoltad meg, ne írd ki. A fenti limitek a tervezés iránymutatói, nem azt jelentik, hogy a kész szöveg automatikusan annyi karakter.

---

## 2. 7 címsor típus

87 sablon 7 típusban. Részletes sablonok: `assets/sablonok/cimsor/[típus].md`

| # | Típus | Sablonok | Mikor használd | Példa (cseréld saját adatra) |
|---|-------|----------|----------------|------------------|
| 1 | **Ajánlat / Akció** | 19 | Konkrét ajánlat, kedvezmény, garancia, próba | „7 nap ingyen. Ha nem tetszik, törlöd." |
| 2 | **Előny-ígéret** | 18 | Eredmény ígéret, átalakulás, jobb alternatíva | „5,5 óra [termek], utána magabiztosan dolgozol" |
| 3 | **Probléma-megoldás** | 9 | Fájdalompont kiemelés + megoldás | „Unom, hogy a szolgáltatóra várok" |
| 4 | **Meglepő állítás** | 9 | Váratlan, erős kijelentés, attention grabber | „2 millió forintot kerestem tavaly [készség]gel" |
| 5 | **Társadalmi bizonyíték** | 10 | Számok, vélemények, social proof | „[ügyfélszám] tag, [termék-szám] termék, 1 előfizetés" |
| 6 | **Termékleírás** | 15 | Termék tulajdonságok, feature kiemelés | „[termék-szám] termék. 200+ óra. [ár]." |
| 7 | **Kíváncsiság-keltés** | 7 | Kérdés, nyitott hurok, curiosity gap | „Van egy bökkenő a [termek]kel." |

### Címsor írási szabályok

- A címsor az első dolog amit az ember lát a képen kívül
- Max 40 karakter (Meta), max 30 karakter (Google)
- Egy címsor = egy gondolat, egy ígéret
- Ha kérdés: ne legyen eldöntendő (igen/nem), hanem gondolkodtató
- Számokkal indítani erős (specifikusság trigger)
- Variáld a típusokat: ne legyen 5 „ajánlat" egymás után

---

## 3. 10 elsődleges szöveg formula

89 sablon 10 formulában. Részletes sablonok: `assets/sablonok/elsodleges-szoveg/[formula].md`

| # | Formula | Sablonok | Struktúra | Legjobb erre |
|---|---------|----------|-----------|-------------|
| 1 | **FAB** | 18 | Feature→Advantage→Benefit | Termék tulajdonságok bemutatása, összetevő listák |
| 2 | **4P** | 14 | Promise→Picture→Proof→Push | Termék-tudatos célcsoport, közvetlen ajánlat |
| 3 | **Storyselling** | 12 | Jelenet→Probléma→Fordulópont→Megoldás→CTA | Személyes sztorik, érzelmi kapcsolat |
| 4 | **PAS** | 11 | Problem→Agitate→Solution | Probléma-tudatos célcsoport |
| 5 | **AIDA** | 9 | Attention→Interest→Desire→Action | Általános célú, széles célcsoport |
| 6 | **QUEST** | 7 | Qualify→Understand→Educate→Stimulate→Transition | Drágább termékek, oktatást igénylő ajánlat |
| 7 | **BAB** | 6 | Before→After→Bridge | Átalakulás bemutatása |
| 8 | **Feel-Felt-Found** | 4 | Érezd→Érezték→Tapasztalták | Kifogáskezelés, ellenállás oldása |
| 9 | **ACCA** | 4 | Awareness→Comprehension→Conviction→Action | Tudattalan/probléma-tudatos célcsoport |
| 10 | **StoryBrand** | 4 | Hős(vásárló)→Probléma→Mentor(te)→Terv→CTA→Tét→Siker | Hosszabb szöveg, brand építés |

### FAB altípusok (a leggyakoribb formula)

| Altípus | Minta |
|---------|-------|
| Összetevő lista | ✅ Feature1→Benefit1, ✅ Feature2→Benefit2... |
| Összetevő reflektorfény | 1 sztár feature mély kifejtése |
| Probléma→Feature híd | Fájdalom → Feature mint megoldás |
| Előny-halmozás | Rövid, ütős benefit sorozat |
| Social proof szendvics | Social proof → FAB → Social proof |
| Összehasonlító | Mi vs. alternatívák |
| Kérdés→Feature→Benefit | Kérdéssel nyit, feature-rel válaszol |

### Elsődleges szöveg írási szabályok

- Az első 125 karakter a legfontosabb (hajtás felett látszik)
- Hook-kal indít, SOHA nem köszönéssel
- Max 1000 karakter (de nem kell kihasználni)
- Rövid bekezdések, üres sorok között
- Egy szöveg = egy üzenet = egy CTA
- A formula meghatározza a struktúrát, de a hang mindig a márkahang

---

## 4. 5 tudatossági szint (Schwartz)

A célcsoport tudatossági szintje meghatározza melyik címsor típust és formulát válaszd.

| Szint | Jellemző | Legjobb címsor típus | Legjobb formula |
|-------|----------|---------------------|-----------------|
| **1. Tudattalan** | Nem tudja, hogy van problémája | Meglepő állítás, Kíváncsiság | Storyselling, ACCA |
| **2. Probléma-tudatos** | Érzi a problémát, nem ismeri a megoldást | Probléma-megoldás, Kíváncsiság | PAS, QUEST |
| **3. Megoldás-tudatos** | Tudja hogy van megoldás, nem ismeri a terméket | Előny-ígéret, Termékleírás | AIDA, BAB, FAB |
| **4. Termék-tudatos** | Ismeri a terméket, nincs meggyőzve | Társadalmi bizonyíték, Ajánlat | 4P, FAB (Social proof szendvics) |
| **5. Legtudatosabb** | Készen áll, utolsó lökés kell | Ajánlat / Akció | Feel-Felt-Found, közvetlen ajánlat |

---

## 5. CTA rendszer

### Erős CTA jellemzők
1. **Konkrét:** pontosan mit tegyen
2. **Előnyfókuszú:** mit nyer vele
3. **Cselekvésorientált:** igével indul
4. **Alacsony küszöb:** kis elköteleződés
5. **Természetes:** a szövegből következik
6. **Eredményfókuszú:** az eredményre mutat

### CTA típusok

**Közvetlen (elsődleges):**
- „Nézd meg a [termek]et"
- „Próbáld ki a [termek]et"
- „Regisztrálj a webinárra"

**Átmeneti (lágy, bizalomépítő):**
- „Töltsd le ingyen"
- „Nézd meg a videót"
- „Kérd el a sablont"

### CTA szabályok
- Termék-specifikus hirdetésnél a termék neve legyen a CTA-ban
- Felelősség-átadás: „Ha érdekel, nézd meg", nem „KATTINTS MOST!"
- Egy hirdetés = egy CTA
- Variáld: „Próbáld ki" / „Nézd meg" / „Vágj bele" / „Csatlakozz"

### Gyenge CTA-k (kerülendő)
- „Bővebben" / „Tudj meg többet" / „Kattints ide" / „Elküldés"
- Bármilyen felszólító módú nyomulás: „Ne habozz!", „Csapj le rá!"

---

## 6. Tulajdonság → Funkció → Előny fordítás

Ez a kulcs mechanizmus: a termék száraz tényeit vásárlói értékké fordítani. (A példák illusztrációk — töltsd ki saját termék-adatokkal.)

| Tulajdonság | Funkció | Előny |
|---|---|---|
| [termék-szám] termék | Egy előfizetéssel mind elérhető | Nem kell külön-külön fizetni, mindenhez hozzáférsz |
| [ár] | Korlátlan hozzáférés alacsony havidíjért | Olcsóbb, mint bármely hasonló megoldás |
| 7 napos próba | Ingyen kipróbálhatod mielőtt fizetnél | Kockázatmentes, nincs mit veszíteni |
| [termek] 5,5 óra | Nulláról profi szintre, lépésről lépésre | 5,5 óra alatt magabiztosan dolgozol |
| Zárt közösség | [ügyfélszám] tag, kérdezz bármit | Nem vagy egyedül, segítenek |

**Szabály:** Hirdetésben SOHA ne a tulajdonságot írd, mindig a funkciót vagy az előnyt.

---

## 7. Tiltott szavak és minták

> Ha van `00-agy/brand/markahang.md`, annak II. Mit ne szekciója bővíti ezt a listát a cég saját anti-mintáival. Az alábbi alaplista fájl nélkül is érvényes — minden generált hirdetésnél futtasd le.

### Tiltott szavak (tipikus AI / reklám-klisé)
„egyedülálló", „kihagyhatatlan", „forradalmi", „garantált" (kivéve valódi garancia), „exkluzív", „csapatunk büszke", „örömmel jelentjük", „fantasztikus hír", „szenzációs", „hihetetlen", „páratlan", „tökéletes"

### Tiltott minták
- „Kattints most!" — soha
- „Ne hagyd ki!" — soha
- „Csak ma!" — csak ha tényleg
- „Nem X. Hanem Y." többször egy szövegben
- Redundancia (ne mondd kétszer más szavakkal)
- Csupa nagybetűs szavak (kivéve brand)
- Felkiáltójelek halmozása (max 1)
- Hamis sürgősség / szűkösség
- Túl retorikus mondatok — szóljon mint élő beszéd

### Google Ads specifikus
- Felkiáltójel címsorban tilos
- Csupa nagybetű címsorban tilos
- Félrevezető állítás tilos
- Pontatlan ár feltüntetés tilos

---

## 8. Kreatív brief sablon

```
### Kreatív brief: [Hirdetés neve]

**Típus:** Kép / Videó / Carousel / UGC
**Platform:** Meta / Google / TikTok

**Vizuál irány:**
[Mi legyen a képen/videóban]

**Szöveg overlay:**
[Max 20% felület. A kulcsüzenet.]

**Hangulat:**
[professzionális / barátságos / sürgető / inspiráló]

**Arc / ember:**
[Kell-e? Az oktató? Stock? Nincs?]
```

---

## 9. USP-k hirdetésekhez (sablon)

Töltsd ki a saját ajánlatod USP-ivel. Ha van kontextus-fájl (`00-agy/brand/ajanlatok/<ajanlat>/kontextus-elemek.md`), onnan vedd; ha nincs, a felhasználótól vagy a beillesztett anyagból. Példa-szerkezet:

| USP | Számmal |
|-----|--------|
| Kínálat | [termék-szám] termék, 1 előfizetés |
| Ár | [ár] |
| Ügyfélbázis | [ügyfélszám] tag |
| Nyelvezet | [nyelv] |
| Tempó | Saját tempóban |
| Előfeltétel | Nincs, nulláról |
| Frissítés | Folyamatosan frissül |
| Próba | 7 napos ingyenes próba |

---

## 10. Célcsoport szegmensek hirdetésekhez (sablon)

A konkrét szegmenseket a `celcsoport.md`-ből vedd, ha van; ha nincs, a felhasználótól vagy a beillesztett anyagból. Példa-szerkezet:

| Szegmens | Fájdalom | Vágy | Releváns termék |
|----------|----------|------|-----------------|
| 1. avatar | [fő fájdalom] | [fő vágy] | [termek] |
| 2. avatar | [fő fájdalom] | [fő vágy] | [termek] |
| 3. avatar | [fő fájdalom] | [fő vágy] | [termek] |
