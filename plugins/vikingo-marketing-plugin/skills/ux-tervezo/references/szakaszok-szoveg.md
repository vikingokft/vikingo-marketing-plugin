# Szakaszok + webszöveg — tartalomstruktúra és vázlatok

> A `ux-terv.md` 3. és 4. szekciójához. Szakasz-katalógus, oldal-receptek, webszöveg-elvek, Typeframing-formátum, iterációs irányok, anti-patternek.

## Tartalom

1. Szakasz-katalógus
2. Oldal-receptek (kiindulási pontok)
3. Webszöveg-elvek
4. Typeframing-formátum (szakaszonként)
5. Iterációs irányok (skill-javaslat)
6. Anti-patternek

---

## 1. Szakasz-katalógus

A tartalomstruktúrában ezekből rakosgatsz.

| Szakasz | Cél | Mikor használd |
|---|---|---|
| **Hero** | 5 mp magyarázat: mit, kinek, fő előny | Szinte minden oldalon első |
| **Előny-szakasz (3-4 pont)** | Miért válassza a céget | Főoldal, szolg-oldal, sales |
| **Probléma-szakasz** | A látogató felismerje a saját problémáját | Top-of-funnel oldalakon |
| **Megoldás-szakasz** | Mit kínál válaszként | Probléma után, vagy önállóan |
| **Funkciók / előnyök (ikon-doboz)** | Mit tud + mit nyer a felhasználó | Szolg-oldal, termék-oldal, főoldal |
| **Visszajelzések (testimonial)** | Social proof, bizalom | Majdnem mindenhol |
| **Csapat-bemutatás** | Humanizálás, bizalom | Rólunk, főoldal, szolg-oldal ha kulcsfontos |
| **GYIK (FAQ)** | Kifogás / félelem kezelése | Sales, termék, főoldal záró |
| **Garancia** | Vásárlási félelem csökkentés | Sales, termék (ha van garancia) |
| **Ár-szakasz (csomagok)** | Ár + csomag-választás | Sales, szolg-oldal, kurzus |
| **CTA-szakasz (záró)** | Konverziós akció | Szinte minden oldal végén |
| **Kapcsolat-űrlap** | Lead-gyűjtés | Kapcsolat-oldalon központi |
| **Galéria** | Vizuális termék / projekt | Portfolio, termék, fotózás |
| **Blog-feed** | Friss tartalom + SEO | Főoldal alsó, blog-aloldal |
| **Kép-szöveg vegyes** | Részletes magyarázat / „Hogyan működik" | Szolg-oldal, „Hogyan dolgozunk" |
| **Számláló** | Social proof számokban | Főoldal, Rólunk |
| **Partner / integráció logók** | Trust (ismert márkák) | Főoldal, sales |
| **Hírlevél-feliratkozás** | Lead-gyűjtés tartalom-felhasználókból | Blog vége, főoldal alsó |

**Tipp:** ne keverd a „funkciókat" (mit csinál) és „előnyöket" (mit nyer a felhasználó).

## 2. Oldal-receptek (kiindulási pontok)

| Oldal-típus | Szakaszok sorrendben |
|---|---|
| **1-oldalas landing** | Hero → Mit kapsz → Mire jó → Bizonyíték → CTA-záró → Footer |
| **Vállalkozói főoldal (egyszerű)** | Hero → Mit kínálunk (3 szolg) → Miért minket (3-4 előny) → Visszajelzések → CTA + kapcsolat |
| **Vállalkozói főoldal (kibővített)** | Hero → Probléma → Megoldás → Szolgáltatások → Hogyan dolgozunk → Csapat-előview → Visszajelzések → Számláló → GYIK → CTA |
| **Szolgáltatás-aloldal** | Hero → Kinek szól → Mit tartalmaz → Folyamat → Ár → Visszajelzések → GYIK → CTA |
| **Kapcsolat-oldal** | Mini-hero → Űrlap → Email + telefon + cím → Térkép → Nyitvatartás → Social |
| **Rólunk-oldal** | Hero (küldetés) → Történet → Csapat → Értékek → Visszajelzések → CTA |
| **Webshop főoldal** | Hero → Kategóriák → Kiemelt termékek → Előnyök → Visszajelzések → Hírlevél → Footer |

Termék-sales-oldalra: a részletes szöveget a `sales-oldal-iro` skill írja. A `ux-tervezo` csak az IA-szintet adja.

## 3. Webszöveg-elvek

A `00-agy/brand/markahang.md` szabályai érvényesek. Kötelező (alapesetben — a konkrét megszólítást a cég-hang dönti el):

- **Tegezés mindenhol** (vagy a cég-hang szerinti megszólítás).
- **Gondolatjel mondat közben SOHA.**
- **„Nem X, hanem Y" max 1×** az egész terven.
- **Rövid mondatok.** Max 3 sor / bekezdés.
- **CTA-szöveg konkrét akció**, igével: „Letöltöm", „Ajánlatot kérek", „Időpontot foglalok". **Nem** „Tovább" / „Több info".
- **Eredmény-ígéret a hero-ban**, nem folyamat-leírás.
- **Bizonyíték a marketing-állításra** — ne mondj „a legjobb"-at szám / visszajelzés nélkül.
- **Számmal kezdődő CTA / címsor:** a határozott névelőt a **kiejtés** szerint ellenőrizd, nem a leírt számjegy első betűje alapján (5 = „öt" → **az** 5 nap; 1 = „egy" → **az** 1 lépés; 100 = „száz" → **a** 100 nap). A „*a* 5 napos" tipikus hiba.

## 4. Typeframing-formátum (szakaszonként)

```markdown
### Hero — Főoldal
**Címsor (H1) — A opció:** [konkrét cím]
**Címsor (H1) — B opció:** [másik megközelítés]
**Alcím:** [1-2 mondat]
**CTA gomb:** [konkrét akció]
**Másodlagos CTA (opc):** [enyhébb opció]
**Vizuális utalás:** [pl. „háttérben cég-fotó" — CSAK utalás, NEM design]

### Előnyök — Főoldal
**Címsor:** [pl. „Miért válassz minket?"]
**3 pont:**
1. **[Rövid cím]** — [1-2 mondat]
2. **[Rövid cím]** — [1-2 mondat]
3. **[Rövid cím]** — [1-2 mondat]

### GYIK — Sales-oldal
**Címsor:** „Gyakori kérdések"
1. **Kérdés:** [valódi vásárló-kérdés]
   **Válasz:** [konkrét, 2-3 mondat]
```

Hero-címsoroknál mindig adj **2 opciót (A/B)**, hogy a felhasználó válasszon.

## 5. Iterációs irányok (skill-javaslat)

Iterációkor 2-3 irányt ajánlasz, mindig a brand-kontextushoz kötve.

| Irány | Mit jelent | Mikor érdemes |
|---|---|---|
| **Konverzió-fókusz** | Több CTA, sticky CTA, exit-intent popup | Fő cél vásárlás/lead, kevés CTA |
| **Információ-gazdagság** | Részletes szolg-oldal, esettanulmányok, mély GYIK | B2B-szerű kutatós döntés |
| **Marketing-tartalom** | Blog-szakasz, lead-magnet, hírlevél | Tartalom-marketing-stratégia |
| **Trust-fókusz** | Visszajelzés-szakasz, számláló, sajtó, partner-logók, garancia | Új cég, bizalmi kihívás |
| **Egyszerűsítés** | Kevesebb oldal / szakasz, 1 fő cél | Túl komplex lett |
| **Mobil-first** | Mobil-szempontból átszervezés, sticky CTA | Többségében mobil látogató |
| **SEO-fókusz** | Több oldal témára, schema.org, blog-stratégia | Organikus növekedés fő csatorna |
| **Niche-irány** | Brand-anyagokból egyedi irány | Konkrét niche-fókusz |

**Mindig kontextushoz kötve javasolj:**
> „A brand-kontextusban azt láttam, hogy új a cég és kevés visszajelzésed van. Trust-fókusz: berakhatnánk egy szám-szakaszt + garancia-elemet."

## 6. Anti-patternek (mit NE csinálj)

**Tartalom-szintű:**
- Túl sok szakasz egy oldalon (8-12 felett a látogató elveszik)
- Hero nélkül kezdődő oldal
- CTA hiánya — minden oldalnak legyen domináns akciója
- Több cél egy oldalon — legyen EGY domináns
- Ismétlődő szakaszok minden oldalon (variálj)

**Skill-szintű (kerüld):**
- Wireframe / drótváz készítése
- Konkrét design-elem (szín, font, képhely, layout-arány)
- Kitalálni a cégről olyat, ami nincs az inputban
- Hosszú kérdőív a kérdezős fázisban — max 7 kérdés
- HTML / CSS / JS-kód írása
- Vizuális moodboard

**Marketing-szintű:**
- „Modern", „letisztult", „professzionális" — üres jelzők
- „Tovább" / „Több info" CTA — konkrét akciót kérj
- „Mi vagyunk a legjobbak" bizonyíték nélkül
- GYIK ami csak marketing-üzenet
