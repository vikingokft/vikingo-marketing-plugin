# Kampány Tervező — Workflow

> Orchestrátor, NEM ír szöveget. 3 fázis + mély mód. 3 tölcsér típus, dispatch a kivitelező skillekhez.

## Tartalomjegyzék

- [Márkahang és formázás](#márkahang-és-formázás)
- [Fázis 0 — Kontextus + kampány](#fázis-0--kontextus--kampány)
- [Fázis 1 — Tölcsér tervezés](#fázis-1--tölcsér-tervezés)
  - [Csali tölcsér elemek](#csali-tölcsér-elemek)
  - [Webinár tölcsér elemek](#webinár-tölcsér-elemek)
  - [Kihívás tölcsér elemek](#kihívás-tölcsér-elemek)
- [Fázis 2 — Output + Notion + Dispatch](#fázis-2--output--notion--dispatch)
- [Mély mód](#mély-mód)

---

## Márkahang és formázás

Minden generált szövegben (output, sablon-kitöltés, javaslat) a `00-agy/brand/markahang.md` az irányadó: ott a részletes anti-minta lista. Ha az még `KITÖLTENDŐ`, dolgozz az alábbi általános elvekből, amelyek a kampány-orchestrátor szempontjából a leggyakoribb buktatók:

- **Gondolatjel (– vagy —) mondat közben:** SOHA. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Tegezés vagy magázás:** ahogy a `00-agy/brand/markahang.md` előírja, következetesen.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor/bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan csiszolt mondatokat, kerüld a fontoskodást, a kitöltő mondatokat, a szinonima-kergetést és a hármasság-kényszert.
- **„Nem X, hanem Y" szerkezet:** az AI egyik leggyakoribb, fárasztó mintája. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi retorikai funkciója van. Tipikus feloldás: töröld a tagadó felet, kezdd a lényeggel, vagy bontsd két mondatra.

Orchestrátorként ritkán írsz hosszú szöveget, de a terv-output és a kérdéseid is a márkahangon szóljanak.

---

## Fázis 0 — Kontextus + kampány

### Cél
Kontextus felmérése (ha elérhető), kampány típus azonosítása.

### Lépések

1. Töltsd be a kontextust: `00-agy/brand/ajanlatok/_attekintes.md` (a portfólió) és a kampány termékének `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md`-je. Ami ott `KITÖLTENDŐ`, azt a Fázis 0 kérdéseivel pótolod, és a válasz a fájlba kerül.
2. Jelezd: „Kampányt tervezünk." Ha betöltöttél kontextust, tedd hozzá: „Betöltöttem a kontextust." Ha nem volt fájl, ne állíts ilyet.
3. Kérdezd: „Melyik termékhez/szolgáltatáshoz, és milyen kampányt tervezel?"

### Kérdések (max 5)

1. **Melyik termék/szolgáltatás?** — Ha van Notion kampány oldal: „Add meg az URL-t, betöltöm onnan."
2. **Milyen tölcsér típus?** (csali / webinár / kihívás, ha nem tudja, segíts)
3. **Mik a kulcs dátumok?** — Kampány indulás, webinár/kihívás napja, utókövetés vége. Ha nincs még: „Mikor szeretnéd indítani?"
4. **Ki az előadó / szereplő?** (webinár/kihívás esetén) — Ki prezentál? Van-e vendégelőadó?
5. **Ki a kampány felelős?** — Ki koordinálja az egészet? Kik dolgoznak rajta? (PPC-s, designer, site builder, stb.)

### Tölcsér típus ajánlás

- Gyors + hideg közönség + automatizálás → **Csali tölcsér**
- Bizalomépítés + kamera előtt jó → **Webinár tölcsér**
- Magas bevonódás + van idő napi tartalomra → **Kihívás tölcsér**

→ „Rendben, [X] tölcsért tervezünk a [termék]-hez."

---

## Fázis 1 — Tölcsér tervezés

Gyors módban: minden elemhez 1-2 kérdés, összefoglaló, tovább. Ha a felhasználó „Részletesebben"-t kér → mély mód (lásd lent).

---

### Csali tölcsér elemek

**C1 — A csali**
- Mi a fő probléma, amire választ ad? Milyen formátum?
- Ha nincs ötlet: 3-4 releváns típus a 24-ből (lásd modszertan.md, 3. szekció)
- Határozd meg: csali neve, formátum, tartalom, kapcsolat a fő ajánlathoz

**C2 — Feliratkozó oldal**
Javasold a struktúrát:
- ✅ Főcím + Alcím + CTA + Űrlap (kötelező)
- ☐ Mockup, bullet pontok, kinek szól, social proof, bio, FOMO, záró CTA (opcionális)

**C3 — Köszönöm oldal + tripwire**
- Lesz-e azonnali ajánlat? Ha igen: mi, milyen áron?

**C4 — E-mail stratégia**
6-8 email, 5-10 nap (NEM szöveg, csak terv):

| # | Típus | Cél | Nap |
|---|-------|-----|-----|

- Ha van meglévő lista: külön bejelentő email a csaliról (1-2 email)
- Új feliratkozóknak: csali átadó → bemutatkozás → értékadás → ajánlat → sürgető
- Trigger szabályok: mikor lép be a sorozatba, mikor kap ajánlatot

**C5 — Fő ajánlat**
- Ajánlat neve, ára, garanciája. Melyik emailtől jelenik meg?

**C6 — Hirdetési stratégia + matek**
- Platform(ok), büdzsé. Számolj a benchmark-okkal (modszertan.md, 9. szekció).
- Platform elosztás: Meta / TikTok / Google, melyiken, milyen arányban?

**C7 — Felelősségek**
- Ki koordinálja? Ki csinál kreatívokat? Ki építi az oldalakat? Ki állítja be az automatizmusokat?

**C8 — Technikai checklist + menetrend**
- Mikorra, milyen eszközök. Hetes bontású menetrend.

---

### Webinár tölcsér elemek

**W1 — Cím, ígéret, elérendő eredmény**
- Webinár végleges címe + alcím
- Mi az egy mondatos fő ígéret?
- Mit tudjon / érezzen / tegyen a résztvevő a végén?
- Mi az a konkrét probléma, amire a webinár választ ad?
- Webinár koncepciója kibontva (2-3 mondat)
- Milyen főbb pontokat tanítasz?
- Hogyan kapcsolódik az ajánlathoz?

**W2 — Tartalmi felépítés (NEM script)**
Kirakósdarabok:
- **Alapozás (~10p):** üdvözlés, nagy ígéret, mi NEM kell, fájdalom, tematika, bemutatkozás, kinek való
- **Tartalom (~30-40p):** módszertan VAGY 3-5 tanítási pont
- **CTA (~15-20p):** összefoglalás, válaszút, ajánlat, ár, bónuszok, garancia, hogyan tovább, Q&A
- Lesz-e gyakorlati elem? Story / esettanulmány?
- Kell-e prezentáció / letölthető melléklet / interaktív elem (pl. mentimeter)?

**W3 — Ajánlat**
- Fő termék / szolgáltatás neve
- Ár / kedvezmény
- Bónuszok
- Limitációk (idő / darabszám / hozzáférés)
- Garancia

**W4 — Webinár szoftver & technika**
- Webinár szoftver (Zoom / YouTube Live / Facebook Live / egyéb)
- Regisztráció a szoftverben szükséges? (igen/nem)
- Replay lesz? (igen/nem). Ha igen: meddig elérhető? (48 óra / 7 nap / korlátlan)
- Lesz support webinár közben?

**W5 — Oldalak + URL slugok**
- Feliratkozó oldal struktúra: főcím + alcím + CTA + űrlap (kötelező), opcionálisan: mockup, bullet pontok, kinek szól, social proof, bio, FOMO
- URL slugok: landing / köszönöm oldal / ajánlat oldal
- Köszönöm oldal: lesz-e azonnali ajánlat (tripwire)?

**W6 — Oldalak webinár UTÁN**
- Feliratkozó oldal sorsa: vázlat / átirányítás más oldalra?
- Ajánlat oldal sorsa: vázlat / átirányítás más oldalra?
- Ki kezeli az átállítást? Mikor? Kell-e időzített váltás?

**W7 — Feliratkozás & lista kezelés**
- Feliratkozási mód (oldalépítő form / külön form-eszköz / egyéb)
- Lista / cimke azonosító

**W8 — Email stratégia: meglévő lista vs. új feliratkozók**
Két külön email szál:

| Szál | Célcsoport | Emailek |
|------|-----------|---------|
| A — Meglévő lista | Akik már ismerik [a céged hangját / az oktatót] | Meghívó (1-2) + emlékeztetők |
| B — Új feliratkozók | Hirdetésből jönnek, regisztrálnak | Visszaigazolás + előmelegítők + emlékeztetők |

- A meglévő listának kevesebb előmelegítés kell, de erősebb „miért érdemes eljönni"
- Új feliratkozóknál: bemutatkozás + értékadás + bizalomépítés a webinárig
- **Emlékeztető ütemezés:** -3 nap, webinár napján reggel, 1 órával előtte
- Utókampány: hány email, mi a célja?
- Konkrét email automatizmus felépítés (sikeres reg → +1 nap → dátumhoz kötött → stb.)

**W9 — Hirdetések: stratégiai döntések**
- Hirdetési platformok: Meta / TikTok / Google, melyiken, milyen arányban?
- Hirdetés felépítés: kampányköltségkeret vagy hirdetéssorozat költségkeret?
- Több hirdetéssorozat vagy 1 nagy széles?
- Szöveg/cím változatok: egy hirdetéshez berakva, vagy külön hirdetés variációnként?
- Hány szöveg és cím legyen 1 hirdetéshez?
- Napi büdzsé platformonként
- Mi a célszám?
	- Elvárt minimum feliratkozó
	- Milyen feliratkozói költséggel
- Webinár konverziós lánc: feliratkozás → megjelenés (25%) → vásárlás (10%)

**W10 — Felelősségek**
| Szerep | Feladat |
|--------|---------|
| Kampány felelős | Koordináció, határidők |
| Operatív menedzser | Napi végrehajtás |
| Jóváhagyó | Szövegek, kreatívok jóváhagyása |
| Előadó | Webinár tartalom, script jóváhagyás |
| Videós/vágó | Hirdetés videók |
| Szövegíró | Email, hirdetés, oldal szövegek |
| Site builder | Oldalak felépítése |
| Designer | Kreatívok, oldal design |
| PPC-s | Hirdetés setup + optimalizáció |

**W11 — Menetrend**
- Relatív hetes bontás a webinár napjához képest: W-10...W-1, Webinár napja, W+1...W+3
- Minden hétnél: fő feladatok + felelősök

---

### Kihívás tölcsér elemek

**K1 — Kihívás koncepció**
- Konkrét eredmény X nap alatt? Hány napos? Mennyi napi elköteleződés?

**K2 — Regisztrációs oldal**
- Plusz: időtartam, kezdési dátum, napi elköteleződés, közösségi elem

**K3 — Napi tartalom**
- Napról napra terv: téma + feladat + eredmény

**K4 — Közösség**
- Platform, moderálás, napi aktivizálás

**K5 — Záró webinár**
- W4 alapján, de kihívás eredményeire építve

**K6 — Email stratégia**
- Előmelegítés: visszaigazolás + közösségi meghívó + felkészülés
- Kihívás alatt: napi feladat + motiváció (meglévő lista is kap update-eket?)
- Záró fázis: webinár meghívó + utókövetés + ajánlat sorozat
- Meglévő lista vs. új feliratkozó: eltérő előmelegítés

**K7 — Hirdetési stratégia + matek**
- Platform elosztás és büdzsé struktúra

**K8 — Felelősségek**
- Ki a kihívás moderátor? Ki kezeli a közösséget? Ki koordinál?

**K9 — Technikai setup + menetrend**
- 5-6 hetes menetrend

---

## Fázis 2 — Output + Notion + Dispatch

„Végigmentünk mindenen. Módosítanál valamit?"

### Output sablon

A teljes másolható terv-sablon (webinár kampány strategizálás, 15 szekció) itt van: [assets/webinar-kampany-terv-sablon.md](../assets/webinar-kampany-terv-sablon.md). Töltsd ki a beszélgetés alapján, és add vissza kódblokkban (másolható).

### Csali / kihívás tölcsér output

Ha csali vagy kihívás tölcsér → használd ugyanezt a sablont alapként, de igazítsd a tölcsér típushoz:
- **Csali:** a 4. (tartalmi felépítés) szekció helyett csali leírás (név, formátum, tartalom), webinár-specifikus szekciók kihagyása
- **Kihívás:** a 4. szekció kibővítve napi tervvel, közösségi elem hozzáadása

### Notion mentés

Ha van kampány oldal → „Mentsem a tervet a Notion kampány oldalra?"

### Dispatch — Következő lépések

A tölcsér terv végén **mindig** javasold a következő skilleket:

**Csali tölcsér:**
1. `/ajanlat-workshop` → Lead magnet kialakítás (ha nincs még)
2. `/email-iro` → Csali email sorozat megírása
3. `/sales-oldal-iro` → Feliratkozó oldal + köszönöm oldal szöveg
4. `/hirdetes-szovegiro` → Hirdetés szövegek
5. `/hirdetes-video-script-iro` → Videó hirdetés scriptek (ha kell)

**Webinár tölcsér:**
1. `/ajanlat-workshop` → Ajánlat kidolgozása (ha nincs)
2. `/webinar-script-iro` → Webinár script
3. `/email-iro` → Előmelegítő + utókövető email sorozat
4. `/sales-oldal-iro` → Regisztrációs + ajánlat + köszönöm oldal
5. `/hirdetes-szovegiro` → Hirdetés szövegek
6. `/hirdetes-video-script-iro` → Videó scriptek

**Kihívás tölcsér:**
1. `/ajanlat-workshop` → Ajánlat kidolgozása (ha nincs)
2. `/email-iro` → Teljes email sorozat (regisztráció → napi → utókövetés)
3. `/webinar-script-iro` → Záró webinár script
4. `/sales-oldal-iro` → Regisztrációs + ajánlat oldal
5. `/hirdetes-szovegiro` → Hirdetés szövegek

**Új termék launch (nem tölcsér, hanem kampány típus):**
1. `/ajanlat-workshop` → termék-ajánlat kontextus (ha nincs még)
2. `/sales-oldal-iro` → termék sales oldal
3. `/email-iro` → Bejelentő email(ek)
4. `/hirdetes-szovegiro` + `/hirdetes-video-script-iro` → PPC

→ „Melyikkel kezdjük?"

---

## Mély mód

Ha bármelyik elemnél a felhasználó „Részletesebben"-t kér:
- Használd a módszertan teljes anyagát (modszertan.md: 24 csali típus, oldal szakaszok, email típusok, hirdetési matek)
- Lépésenkénti kérdezés, összefoglalás, „Stimmel?"
- Ha végzett: visszatérsz gyors módba
