# Csali mód — referencia

Ez a fájl **csak azt tartalmazza, ami a csalinál más**, mint a terméknél. Minden egyéb (a
`_sablon` fájljainak kitöltése, az értékpiramis 30 eleme, a kifogás-kategóriák és a
hook-típusok) a [`sablonok.md`](sablonok.md)-ban és a [`modszertan.md`](modszertan.md)-ban él,
és a csalinál ugyanúgy érvényes. **Ne duplikáld őket.**

A csali (lead magnet, webinár, kihívás) ugyanúgy egy ajánlat-mappát kap
(`00-agy/brand/ajanlatok/<csali>/`), ugyanazokkal a `_sablon` fájlokkal. Három dolog más:

1. **A szülő-termék kontextusa bemenet — ha létezik.** Ahova a csali vezet. Ha annak a
   terméknek még nincs `kontextus.md`-je, **ez nem blokkoló**: a hiányzó fájl és a
   `KITÖLTENDŐ` mező ugyanaz, nincs adat ([`marketing-kontextus.md`](../../_kozos/marketing-kontextus.md)).
   Ilyenkor a cég-szintű anyagból dolgozz, a csali fájljában hagyd `KITÖLTENDŐ`-n, ami a
   szülő-termékből jönne, és a záró
   összefoglalóban mondd ki egy sorban, hogy a `termek-specialista` **termék módban** még
   lefuttatható arra a termékre. **Ne találd ki a szülő-termék adatait.**
2. **A `kontextus.md` szakaszaiba részben más kerül**, lásd lent.
3. **Más kérdések kellenek** a hiánypótláskor: tölcsér-típus, upsell, deadline, kézbesítés.

Az univerzális hirdetési változók (ár, garancia, kuponkód, ügyfélszám, díj, termékkategória)
**nem** a csali fájljába kerülnek: azok a cég-szintű `00-agy/brand/kontextus-elemek.md`-ben és a
szülő-termék `kontextus-elemek.md`-jében élnek, és öröklődnek. Ide csak a csali-specifikus
felülírás és az új változó megy.

---


## 1. A `kontextus.md` csalinál

Ugyanaz a `_sablon/kontextus.md`, ugyanazokkal a szakaszokkal. Ami csalinál más:

| `_sablon` szakasz | Csalinál ide kerül |
|---|---|
| Mit ad el, és kinek | Mi ez (típus a lenti 24-ből, formátum), mire jó, és hogy e-mail-címért cserébe ingyenes |
| Az ajánlat mechanikája | A csali **tartalma** (pontok, fejezetek, napok, terjedelem) és a kampány útja: hirdetés → feliratkozó oldal → köszönőoldal → átadás → e-mail-sorozat → a szülő-termék oldala. Ha a tartalom még nincs kész, `KITÖLTENDŐ`: ne találd ki |
| Átalakulási útvonal | Kicsi, gyors eredmény: mit tud vagy lát másképp a csali után |
| Miért működik | Miért éri meg ezt elkérni, és hogyan vezet a szülő-termékhez |
| Értékpiramis | Mint a terméknél, általában 1-2 elem szintenként |
| Pozicionálás az ajánlat szintjén | Kapcsolat a szülő-termékkel és a céggel; a **Szülő-termék** sorba a szülő-termék mappaneve (ha még nincs, `KITÖLTENDŐ`) |
| Kiszállítás és teljesítési korlátok | Kézbesítés (e-mail, átadó oldal, automatizmus), időzítés, deadline, ha van |
| Kizáró tényezők | Mire nem jó, kinek nem való (elvárás-kezelés) |

A `kontextus-elemek.md`-ben csalinál az `ingyenes ajánlat / lead magnet` mező a csali neve, a `csomag tartalma` a tartalma. Az ár, a garancia és a kuponkód ide nem kerül: a szülő-termékről és a cég-szintről öröklődik. Ha a csalinak nincs saját garanciája vagy kuponja, az nem `nincs`, hanem `KITÖLTENDŐ`, hogy az öröklés éljen.

A kész anyagok (e-mail-sorozat, feliratkozó oldal, hirdetések, videók) a kimeneti helyen élnek (közös szerződés: „Hova kerül a kész anyag”, az `<ajanlat>` itt a csali mappaneve). A csali `_attekintes.md`-jének „Kanonikus sales-anyagok” részébe csak a hivatkozásuk kerül.

---

## 2. Csali-specifikus CTA-variánsok

A csali kontextusban két CTA szint van:

**Opt-in CTA-k (csali letöltés):**
- „Töltsd le ingyen"
- „Kérd el a [csali neve]-t"
- „Add meg az e-mail címed és küldöm"

**Upsell CTA-k (fő ajánlat):**
- „Nézd meg a [terméket]"
- „Próbáld ki [X] napig ingyen" (csak ha a szülő-terméknek van valódi próbaidőszaka)
- „Ha érdekel, itt tudsz belépni"

---

## 3. A 24 csali típus

| # | Típus | Jellemző |
|---|-------|----------|
| 1 | Útmutató / beszámoló | Részletes leírás egy témáról |
| 2 | Puska | Gyors, tömör segédlet |
| 3 | Checklist / folyamatábra | Lépésről lépésre útmutató |
| 4 | Lista / gyűjtés | Erőforrások, eszközök, tippek |
| 5 | E-book | Hosszabb, könyvszerű tartalom |
| 6 | Oktatóvideó | Egy konkrét technika bemutatása |
| 7 | Több napos videós kurzus | 3-7 napos mini tanfolyam |
| 8 | Webinár | Élő online előadás |
| 9 | Esemény videók | Korábbi előadások felvételei |
| 10 | Sablonok | Azonnal használható eszközök |
| 11 | Ingyenes szoftver / próba | Szoftver kipróbálás |
| 12 | Kalkulátor | Számokkal mutatja az értéket |
| 13 | Audit | Ingyenes elemzés/értékelés |
| 14 | Akció / kupon | Kedvezmény csali |
| 15 | Sorsolás | Nyereményjáték belépőért |
| 16 | Fizikai termék (próbacsomag) | Kézzelfogható minta |
| 17 | Teszt / kvíz | Interaktív, személyre szabott eredmény |
| 18 | Kihívás | Napokig tartó program |
| 19 | Közösségi csoport hozzáférés | Zárt csoport tagság |
| 20 | Ingyenes konzultáció | Első alkalom ingyen |
| 21 | Workshoprészvétel | Élő workshop |
| 22 | Podcast sorozat | Több részes audio |
| 23 | Poszter / infografika | Vizuális segédlet |
| 24 | AI eszköz / prompt csomag | AI-alapú megoldás |

---

## 4. Tölcsér-típusok

| Szempont | Csali tölcsér | Webinár tölcsér | Kihívás tölcsér |
|----------|--------------|-----------------|-----------------|
| **Komplexitás** | Közepes (~40-60 óra) | Magas (~80-100 óra) | Nagyon magas (~150-200 óra) |
| **Értékesítési ciklus** | Pár nap | 5-14 nap | 2+ hét |
| **Elköteleződés** | Alacsony (letöltés) | Közepes (élő részvétel) | Magas (napi feladatok) |
| **Konverzió potenciál** | Alacsonyabb | Magasabb | Legmagasabb |
| **Örökzöldíthető?** | Igen, teljesen | Részben | Nehezen |

---

## 5. Hiánypótló kérdések csali módban

### Kérdések (csak ami tényleg hiányzik!)

1. **A csali tartalma:** „Mi van a csaliban (pontok, fejezetek, napok)?” Ha még nincs kész, a mechanika tartalom-része `KITÖLTENDŐ` marad. Ne találd ki, mert a feliratkozó oldal és az e-mailek erre ígérnek.

2. **Tölcsér-típus:** „Milyen tölcsér mögött lesz ez a csali?” (csali/webinár/kihívás). Ha a Szakasz 0 javaslata jó, csak erősítsd meg.

3. **Szülő-termék (upsell):** „Mi a fő ajánlat mögötte?” (pl. kurzus, coaching). Ha a kontextusból kiderül, ne kérdezd.

4. **Deadline/sürgősség:** „Van időkorlátozás?” (pl. 3 napos ajánlat, launch-időszak)

5. **Kézbesítés:** „Hogyan kapja meg?” (e-mail, átadó oldal, automatizmus)

Bizonyítékra (vélemény, szám) csak akkor kérdezz, ha belefér az öt kérdésbe; ha az `ajanlat-workshop` már rögzítette, onnan vedd.

### Fontos szabályok

- **Egy menet, nem több ciklus.** Minden kérdést egyszerre tedd fel.
- Amit nem kapsz meg: `KITÖLTENDŐ`.
- Ha a felhasználó módosítja a Szakasz 0 javaslatokat → adaptáld.
- A célcsoport-javaslatot erősítsd meg: „A javasolt avatarok jók, vagy cserélnél?"

Tovább: Szakasz 2.

---

## 6. Deriválási stratégia csali módban

A változókat a csali többi fájljából deriváld:
- **Mechanika (tartalom)** → `feature / jellemző`, `csomag tartalma`
- **`celcsoport.md`, `kifogasok.md`** → `megszólítás`, `szint / tapasztalat`, `vágy / aspiráció`, `identitás`, `fő fájdalom`, `félelem`, `akadály`, `rossz alternatíva`, `érzelmi benefit`
- **Átalakulási útvonal** → `átalakulás: előtte → utána`
- **Értékpiramis** → `érzelmi benefit`, `advantage / előny a versenytárssal szemben`, `fő eredmény / ígéret`
- **Oktató** → `szakértő / tekintély`
- **`testimonialok.md`** → `eredménytörténet / testimonial`
- **Pozicionálás, Kiszállítás (deadline)** → `sürgősség`, `lökés / záró érv`

A levezetett, de el nem hangzott ígéret (például „bármikor leiratkozhatsz”) `(következtetés, erősítsd meg)` jelölést kap.

A bullet-eket úgy fogalmazd, mintha a referencia-mintát követnéd: élő mondatok, konkrétumok, célcsoport-hangok, sok variáns ugyanarra a magvalóságra.

---
