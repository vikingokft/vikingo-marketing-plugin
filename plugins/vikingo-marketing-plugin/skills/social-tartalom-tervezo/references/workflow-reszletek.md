# Social Tartalom Tervező: Workflow részletek

> 3 fázis + mély mód. Termék-tartalomból (kurzus, lecke, edukációs anyag) rövid videó scriptek, képes posztok, carousel tartalmak. 6 hook típus, platform-specifikus formátumok.
>
> 🟡 PÉLDÁK ILLUSZTRÁCIÓK: a fájl konkrét példákat tartalmaz (termék-/kurzus-nevek, avatar-nevek) — ezek csak illusztrációk. A struktúra, a formulák és a módszertan általános, a konkrét hivatkozásokat cseréld a saját adataidra.

---

## Márkahang és formázás

A `00-agy/brand/markahang.md` szabályai (I. Alapelvek + II. Mit ne + III. Social) az irányadók minden generált szövegben (output, sablon-kitöltés, javaslat). Ha ezek még `KITÖLTENDŐ`-k, tartsd az alábbi általános minimumot:

- **Gondolatjel (– vagy —) mondat közben:** kerüld. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Megszólítás:** a cég-hang szerint (alapesetben tegezés, ha a `00-agy/brand/markahang.md` így rendeli).
- **Szókincs:** a `00-agy/brand/markahang.md` I. Alapelvek bekezdéseit (Hang, Tartalom-elvek) kövesd, és kerüld a II. Mit ne szekció anti-mintáit.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor/bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan túlcsiszolt mondatokat.
- **„Nem X, hanem Y" szerkezet:** Az AI leggyakoribb és legfárasztóbb szerkezete. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi retorikai funkciója van. Helyettesítési stratégiák:
  - **Töröld az első felet.** Ha a „hanem" utáni rész önmagában megáll, a tagadó fél felesleges. ❌ „Nem az appokkal volt a baj. Hanem azzal, hogy nem rendszert építettél." → ✅ „Nem rendszert építettél, csak egy újabb helyet csináltál."
  - **Kezdd a lényeggel.** ❌ „Nem több funkció kell, hanem egy rendszer." → ✅ „Egy működő rendszer kell."
  - **Két külön mondat.** ❌ „Nem a technológia a fontos, hanem a folyamat." → ✅ „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** ❌ „Nem az a kérdés, melyik app jobb. Hanem az, hogy használod-e." → ✅ „A kérdés: használod-e egyáltalán?"
  - **Detektálás — a két mondatra bontott változat IS tiltott.** A szabály nem csak az egy mondaton belüli „nem… hanem…"-ra vonatkozik, hanem a kettévágott formára is: „Nem azért X. Hanem Y.", „Nem azzal van baj, hogy X. Y.", „Nem X. Y." A modell hajlamos pont így kikerülni a szabályt (két mondatra vágja, és a saját QA-ja „nincs"-nek könyveli). Az önellenőrzéskor a tagadó-nyitány + rákövetkező állítás párost is számold bele a max 1× keretbe. ❌ „Nem azért nézel meg száz videót, hogy okosabb légy. Hanem hogy ne kelljen csinálnod." → ✅ „Száz videót nézel meg, csak hogy ne kelljen csinálnod."
- **Szövegírási szabályok:** Minden outputra (válasz, generált szöveg, javaslat) alkalmazd a `00-agy/brand/markahang.md` (II. Mit ne) szabályait. Kerüld a fontoskodást, kitöltő mondatokat, szinonima-kergetést, hármasság-kényszert és a szolgálatkész AI-hangot.

---

## Fázis 0: Kontextus + forrás-tartalom tisztázása

### Cél
Megérteni miből (melyik termék anyagából vagy beillesztett szövegből) kell tartalmat generálni, milyen platformokra, és betölteni a releváns kontextust — amennyi elérhető.

### Lépések

1. **Töltsd be a Bemenet-tábla fájljait:** `00-agy/brand/markahang.md` (figyelj a kifejtő / edukációs szöveg szekcióra), a termék `00-agy/brand/ajanlatok/<ajanlat>/` mappája, és a forrás-tartalom, amiből vágunk.
2. **Ha a termék mappája még üres**, ne állj le: a forrás-anyag és a platform elég az induláshoz. A hangot a `markahang.md` adja; ami kötelezőként hiányzik, azt egyetlen üzenetben kérdezd meg.
3. Jelezd: „Rövid tartalmakat generálunk a forrás-anyagból."

### Kérdések (max 4 — annyit kérdezz, amennyi a fájlokból nem derül ki)

1. **Miből vágjunk?** Egy termék / kurzus az `00-agy/brand/ajanlatok/` mappából, egy konkrét fájl, vagy beillesztett szöveg.
2. **Melyik tartalom-blokk?** mind / specifikus rész megnevezése (pl. egy konkrét lecke vagy modul).
3. **Milyen platformokra?** Reel / TikTok / YouTube Short / Carousel / Poszt / Mix (mindegyik).
4. **Van-e Notion kampány oldal?** Ha van, másold be az URL-t.

### Kontextus betöltés

- Ha van termék kontextus fájl, olvasd be (teljes).
- Olvasd be a forrás-tartalmat — fájlból (kis fájl: teljes; nagy fájl: első 200 sor + fejléc grep) vagy a beillesztett szövegből.
- Elemezd ki a tanítási pontokat, tippeket, meglepő tényeket, gyakori hibákat, példákat.

### Összefoglalás

| Elem | Tartalom |
|------|----------|
| Forrás (termék / kurzus / beillesztett anyag) | [...] |
| Feldolgozott tartalom-blokkok | [...] |
| Platformok | [...] |
| Tanítási pontok száma | [X db a forrás-anyagból kinyerve] |
| Kontextus forrás | Kontextus fájl / beillesztett anyag / felhasználó input |

→ „Stimmel? Ha igen, generálom a koncepciókat."

---

## Fázis 1: Koncepció generálás (10-15 koncepció)

### Cél
A termék-tartalomból kinyert tanítási pontokból 10-15 tartalom-koncepció generálása elosztott hook-típusokkal és platformokkal.

Gyors módban: koncepciókat generálsz, a felhasználó kiválaszt, megírod. Ha „Részletesebben" → mély mód.

### Hogyan dolgozz

1. Keresd a termék-tartalomban:
   - Fő tanítási pontok (mit tanít az anyag?)
   - Meglepő tények, számok, statisztikák
   - Gyakorlati tippek, trükkök
   - Gyakori hibák, tévhitek
   - Személyes történetek, anekdoták
   - Eredmények, amit a tanulók / ügyfelek elérhetnek
2. Alkalmazd az „1 tartalom-egység = 5+ social tartalom" szorzó logikát (lásd `sablonok-katalogus.md` 3. szekció).
3. Oszd el a hook típusokat és platformokat.

### Kötelező elosztás: hook típusok

| Hook típus | Db (15 koncepcióból) |
|---|---|
| Tudtad, hogy...? | 3–4 |
| Rosszul tudod | 2–3 |
| Így csináld | 2–3 |
| Legnagyobb hiba | 2 |
| Személyes tapasztalat | 1–2 |
| Eredmény bemutatás | 1–2 |

### Platform elosztás (ha „Mix")

| Platform | Db |
|---|---|
| Instagram Reel | 3–4 |
| TikTok | 2–3 |
| YouTube Short | 2 |
| Carousel | 2–3 |
| Képes poszt | 2–3 |

### Szabályok

- Minden koncepció **más tanítási pontot** dolgozzon fel, ne ismételd.
- A hook legyen **konkrét szöveg** (amit az oktató ténylegesen elmondana), ne leírás.
- Carousel-nál a cover slide szövegét írd a hook-ba.
- Képes posztnál az első sor legyen a hook.

### Output formátum

Koncepció táblázat:

| # | Tartalom-blokk | Hook típus | Tanítási pont | Platform | CTA előnézet |
|---|----------------|------------|---------------|----------|--------------|
| 1 | [...] | Tudtad, hogy...? | [...] | Reel | [...] |
| 2 | [...] | Rosszul tudod | [...] | TikTok | [...] |

Hook előnézet lista (🟡 a példák illusztrációk):

```
**1.** „Tudtad, hogy a [eszköz] teljesen ingyenes?" → Reel, 30 mp
**2.** „3 [eszköz] funkció, amit rosszul használsz" → TikTok, 45 mp
**3.** „5 lépés a [eredmény]-hez" → Carousel, 7 slide
```

→ „Ezek a koncepciók. Melyikeket írjam meg? Add meg a sorszámokat."

> **Számozás Fázis 2-ben:** ha csak a koncepciók egy részhalmazát írod meg, a megírt darabokat számozd újra folyamatosan (1..N), VAGY a koncepció-táblázatban jelöld egyértelműen, melyik nem készül el. Ne hagyj ugráló számozást (pl. hiányzó 5-ös), mert az befejezetlennek tünteti fel a kész outputot.

---

## Fázis 2: Tartalom írás + output

### Cél
A kiválasztott koncepciókhoz teljes, platform-specifikus tartalom megírása.

### Input kezelés

- Sorszámok: „1, 3, 7, 12"
- Szöveges: „az első hármat", „mind ami carousel"
- Módosítás: „A 3-asnál változtasd meg a hookot erre: ..."

### Tartalom formátumok

#### Rövid videó script (Reel / TikTok / YouTube Short)

```
### [N]. [Cím]
**Platform:** [Reel / TikTok / YouTube Short]
**Hossz:** [X mp]
**Hook típus:** [...]
**Tartalom-forrás:** [termék, tartalom-egység neve]

**HOOK (0-5 mp):**
[1-2 mondat, scroll-stopper]

**TARTALOM (5-X mp):**
[Tanítási pont, rövid, tömör, hétköznapi nyelven]
[Minden gondolat új bekezdés.]
[Konkrét példák, számok, eszközök.]

**CTA (utolsó 5 mp):**
[Platform-specifikus CTA, 1 mondat]

**FELIRAT MEGJEGYZÉS:**
[Felirat stílus javaslat: kulcsszavak kiemelése, színek]
```

#### Képes poszt (Instagram / Facebook / LinkedIn)

```
### [N]. [Cím]
**Platform:** [Instagram / Facebook / LinkedIn]
**Hook típus:** [...]
**Tartalom-forrás:** [termék, tartalom-egység neve]

[Hook az első sorban]

[Értékadó szöveg, 2-4 mondat]

[CTA, 1 mondat, platform-specifikus]

**Kép szöveg javaslat:** [max 10 szó]
```

#### Carousel (Instagram)

```
### [N]. [Cím]
**Platform:** Instagram Carousel
**Slide-ok száma:** [X]
**Hook típus:** [...]
**Tartalom-forrás:** [termék, tartalom-egység neve]

| Slide | Szöveg |
|-------|--------|
| 1 (cover) | [Hook, max 10 szó] |
| 2 | [Pont 1, max 30 szó] |
| 3 | [Pont 2, max 30 szó] |
| ... | ... |
| [utolsó] | [CTA slide] |

**Cover design javaslat:** [szín, stílus, betűméret]
```

### Minden tartalom után

→ „Ez stimmel? Módosítanál rajta?"

### Teljes csomag output sablon

```
## [Termék neve]: Rövid tartalom csomag

### Összefoglaló
- **Termék / kurzus:** [...]
- **Feldolgozott tartalom-blokkok:** [...]
- **Tartalmak száma:** [X]
- **Platformok:** [...]

### Tartalom terv
| # | Típus | Platform | Hook | Tanítási pont | Tartalom-forrás |
|---|-------|----------|------|---------------|-----------------|
| 1 | Reel | Instagram | [...] | [...] | [...] |
| 2 | Poszt | Facebook | [...] | [...] | [...] |

---

[... minden tartalom a fenti formátumok szerint ...]
```

### Minőség-ellenőrzés (BELSŐ, NEM a kimenetbe)

Mielőtt átadod a csomagot, futtasd le a `sablonok-katalogus.md` 8. ellenőrzőlistáját minden darabra. Ezt a beszélgetésben végezd, NE írd bele a végtermék-fájlba / a Notion-oldalba — oda csak a javított tartalom kerül.

### Notion mentés

→ „Mentsem a Notion kampány oldalra is?"

Ha igen: `notion-create-pages` aloldalként, teljes output formátummal.

---

## Mély mód

Ha bármelyik fázisnál „Részletesebben":

**Fázis 1-ben:**
- Minden koncepcióhoz mutasd meg a forrás tartalom-szöveg releváns részletét (idézet).
- Magyarázd el, miért pont ez a hook típus illik ehhez a tanítási ponthoz.
- Add meg az alternatív hook opciókat is (2-3 variáció koncepciónként).

**Fázis 2-ben:**
- Rövid videó scriptnél: adj másodpercre bontott időtervet (0-3 mp: hook, 3-7 mp: pont 1, stb.).
- Carousel-nál: adj design javaslatokat slide-onként (háttér szín, betűtípus, vizuális elem).
- Posztnál: adj 3 tárgysor/hook variációt és hashtag javaslatokat.
- Mutasd meg a forrás tartalom-szöveget, amiből dolgoztál.

Ha végzett: visszatérsz gyors módba.
