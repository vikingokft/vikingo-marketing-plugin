# Workflow-részletek — fázisok, szekció-szabályok, output

> A sales & landing oldal szövegírás részletes protokollja. Márkahang-szabályok, fázisonkénti lépések, szekció-specifikus szabályok, output-sablon, minőségi checklist.

## Tartalom

1. Márkahang és formázás
2. Fázis 0 — oldaltípus és kontextus
3. Fázis 1 — struktúra-tervezés
4. Fázis 2 — szekciónkénti szövegírás
5. Összesítés + output
6. Minőségi checklist

---

## 1. Márkahang és formázás

Minden generált szövegben (output, sablon-kitöltés, javaslat) a `00-agy/brand/markahang.md` az irányadó: az I. Alapelvek, a II. Mit ne és a III. Sales-oldal fejezet felülírja az alábbi alapértelmezést. Ha ezek még `KITÖLTENDŐ`-k, az alábbi alapértelmezett szabályok érvényesek.

- **Gondolatjel (– vagy —) mondat közben:** SOHA. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Tegezés:** ha a cég-hang tegező, mindig, kivétel nélkül.
- **Szókincs:** a `markahang.md` I. Alapelvek bekezdéseit kövesd, és kerüld a II. Mit ne anti-mintáit.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor / bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan túlcsiszolt mondatokat.
- **„Nem X, hanem Y" szerkezet:** Az AI leggyakoribb, legfárasztóbb mintája. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi retorikai funkciója van. Helyettesítés:
  - **Töröld az első felet.** Ha a „hanem" utáni rész önmagában megáll, a tagadó fél felesleges.
  - **Kezdd a lényeggel.** ❌ „Nem több funkció kell, hanem egy rendszer." → ✅ „Egy működő rendszer kell."
  - **Két külön mondat.** ❌ „Nem a technológia a fontos, hanem a folyamat." → ✅ „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** ❌ „Nem az a kérdés, melyik jobb. Hanem hogy használod-e." → ✅ „A kérdés: használod-e egyáltalán?"
- **Szövegírási szabályok minden outputra:** kerüld a fontoskodást, kitöltő mondatokat, szinonima-kergetést, hármasság-kényszert, és a szolgálatkész AI-hangot.

---

## 2. Fázis 0 — oldaltípus és kontextus

### Cél
Eldönteni, milyen oldalt írunk és milyen kontextusban.

### Lépések

1. **Ha elérhetők, töltsd be a kontextus-fájlokat:** `00-agy/brand/markahang.md` (I. Alapelvek + II. Mit ne + III. Sales-oldal) + `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md` + `00-agy/brand/ajanlatok/<ajanlat>/kontextus-elemek.md` (oldal-szintű változók — alap) + `celcsoport.md` (tartalomjegyzék) + `uzenetek.md` + `testimonialok.md` (top idézetek). Ha nincsenek, ezt a lépést kihagyod, és a hiányzó infót a 3. lépésben kérded be.
2. Jelezd: „Oldal-szöveget írunk." (Ha betöltöttél kontextust: „Betöltöttem a kontextust.")
3. Kérdezd: „Milyen oldalt írunk és melyik termék / kampány?" Ha nem volt kontextus-fájl, kérd be a konkrétumokat is (ár, ügyfélszám, garancia, terméknév, célcsoport), vagy dolgozz a beillesztett anyagból. Soha ne állj le egy hiányzó fájl miatt.

### Oldaltípusok (hossz-irányelv)

| Típus | Hossz | Szekciók |
|-------|-------|----------|
| Termék sales oldal | 6.000–9.000 karakter | standard 11+ szekció + opcionálisak |
| Fő-ajánlat sales oldal | 8.000–12.000 karakter | platform-szintű struktúra |
| Webinár regisztrációs | 2.000–4.000 karakter | 4 kötelező + erősítők |
| Landing oldal (lead magnet) | 1.500–3.000 karakter | 3 kötelező + erősítők |
| Köszönöm oldal | 800–2.000 karakter | 3 alap + opcionális tripwire |

### Ha termék sales oldal:
- Töltsd be a termék-szintű kontextus-elemeket: `00-agy/brand/ajanlatok/<ajanlat>/kontextus-elemek.md` — terméknév, ár, csomag tartalma, oktató, eredmény / fájdalom / célcsoport / CTA. Ezek adják a konkrétumokat. Ami ott `KITÖLTENDŐ`, azt egyetlen üzenetben kérdezd meg, és írd be a fájlba.
- Ha elérhető, töltsd be a teljes termék-narratívát: `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md` — modulok, célcsoportok, értékpiramis, sales-szöveg-szekció.
- Ha van meglévő sales-oldal → töltsd be referenciának (a SKILL.md Mentés helyén, `sales-oldal/<ajanlat>/`).
- Ha van sales-szöveg-szekció a kontextusban, az a kiindulópont a szöveghez; ha nincs, a felhasználó leírásából és a célcsoport-fájdalmakból építkezz.

### Ha Notion kampány-URL:
- `notion-fetch`-csel betöltöd.
- Keresd a kampány-tervező tölcsér-tervet (javasolt oldalak, főcím-irány).
- Keresd az ajánlat-workshop outputot (terméknév, ár, bónuszok, garancia).
- „Ezt találtam: [...]. Ebből dolgozom."

---

## 3. Fázis 1 — struktúra-tervezés

### Cél
A szekciók kiválasztása és sorrendezése, az oldal vázlata.

A szekció-sablonokat oldaltípusonként lásd: [oldaltipus-sablonok.md](oldaltipus-sablonok.md). Válaszd ki a megfelelő oldaltípus sablonját, állítsd össze a struktúra-táblázatot, majd kérdezd: „Stimmel a struktúra?" Várd meg a választ.

---

## 4. Fázis 2 — szekciónkénti szövegírás

### Cél
Minden szekció szövegének megírása a `markahang.md` III. Sales-oldal szabályai szerint.

### Szekció-formátum

```
### [N]. [Szekció neve]
**Layout:** [képszöveg / kártya / egyoszlopos / osztott]

**Főcím-opciók:**
A) [szöveg]
B) [szöveg]
C) [szöveg]

**Alcím-opciók:**
A) [szöveg]
B) [szöveg]
C) [szöveg]

[Törzsszöveg, rövid bekezdések, scannable]

**[CTA-gomb szöveg]** [ha van]

---
```

### Címsor / alcím szabály

Minden szekciónál **legalább 3 opciót** adj a főcímre és az alcímre. Az olvasó választ, te nem döntesz helyette. A törzsszöveg 1 verziót kap, ami az A) opcióhoz illeszkedik, de a címsorok cseréjével is működjön.

### Szekció-specifikus szabályok

**Hero:**
- Főcím = felszólítás / imperatívusz (leggyakoribb forma).
- Alcím = 1 mondat, max 10-12 szó.
- Leíró bekezdés = 1-2 mondat, a termék eredményét fogalmazza meg.
- 3 adat: idő + tartalom-egység + melléklet (igazítsd a termékhez).
- 5 másodperces szabály: azonnal értse, miről szól.

**Social proof:**
- Termék-specifikus testimonial → hero alá (ha van).
- Ügyfélszám, ha van adat (a `kontextus-elemek.md`-ből, vagy a felhasználótól / beillesztett anyagból).
- Ha nincs termék-specifikus, jöhet később.

**Probléma / miért kell (5 variáns):**
- Az oldal elején, a „Kinek való" szekció ELŐTT adj **5 különálló probléma / vágy / eredmény szekciót**.
- Minden variáns: alcím (kontextusadó, kis szöveg) + főcím (meggyőző, nagy) + 3-4 mondat törzsszöveg + opcionális CTA gomb.
- A főcímre és alcímre **3-3 opciót** adj (A/B/C), a törzsszöveg 1 verzió.
- 5 tartalmi irány: (1) iparági helyzet / trend, (2) fájdalompont / kontraszt, (3) vágyott eredmény, (4) mit kap a vevő, (5) miért most / sürgősség.
- Tényeken alapul, nem manipulál. Mindig pozitív irányba fordul.

**Kinek való:**
- 3-4 persona, H3 szinten.
- Mindegyik 2-3 mondat kifejtés.
- Sorrend: pályakezdő → szabadúszó → vállalkozó → (hobbista / egyéb).
- Az érték van középen, nem a termék tartalma.

**Termék szerkezete (modulcsoportok):**
- NE sorolj fel minden egységet külön. Csoportosítsd **max 3-4 modulcsoportba** (tematikus blokkok). Nagyon eltérő tartalomnál max 5-6, de ne több.
- Minden csoport: `### [Csoportnév]` + **2-3 mondat** leírás, ami több egységet fed le.
- A cél: nagy csomópontokat mutass be, ne egyedi alegységeket. Az összes részlet felsorolása később, külön szekcióban.
- NEM száraz felsorolás: személyes ígéret, motiváció, kontextus.
- Összefoglaló fejléc: **X szekció | X tartalom-egység | X óra X perc** (igazítsd a termékhez).

**Mire leszel képes (bővebb kifejtés):**
- 3 félkövér pont, mindegyikhez **3-4 mondat kifejtés** (nem 1-2). Az olvasó érezze a súlyát.
- Képesség / eredmény / rendszer-központú.
- Olvasmányos, mini bekezdések, nem egymondatos sorok.
- Nem „tanulsz", hanem „képes leszel".

**Oktató / készítő:**
- Harmadik személyben indul → idézettel személyessé.
- 2-3 releváns hitelességi pont.
- A tanítási / munka-filozófia mindig benne van.

**Testimonialok:**
- 3-5 idézet, eredmény-fókuszú.
- Név + opcionális csillagos értékelés.
- Eredeti szöveg, nem szerkesztett.

**Fő-ajánlat bemutató (ha része egy előfizetésnek):**
- Standard 5 érv (mindig ugyanaz, lásd sablonok-katalogus.md 10. szekció).
- Csak a terméknevet cseréld.
- „A [terméknév] a [fő-ajánlat] része."

**Árképzés:**
- Havi / éves / próba / garancia (a `kontextus-elemek.md` szerint, ha elérhető; egyébként a felhasználótól / beillesztett anyagból).
- Bruttó ár félkövéren, nettó zárójelben.
- Nincs nyomás (nincs „csak ma!", nincs visszaszámláló).

**GYIK:**
- 4-5 kérdés-válasz.
- Standard: „Mikor indul?" + „Szükséges előképzettség?" + „Hogyan kérhetek segítséget?".
- 1-2 termék-specifikus kérdés.
- Rövid, közvetlen, megnyugtató válaszok.

### Layout-típusok

| Layout | Mikor |
|--------|-------|
| **Képszöveg** | Hero, oktató, megoldás, bemutatkozás |
| **Kártya** | Funkciók, testimonialok, ár / csomag, lépések |
| **Egyoszlopos** | Probléma, sztori, GYIK, garancia, CTA |
| **Osztott** | Előtte-utána, kinek szól / kinek nem |

### Szövegírási szabályok

- **Mondathossz:** 47%+ rövid (≤8 szó), max 12% hosszú (>18 szó).
- **Bekezdések:** 1-2 mondat, max 3.
- **Félkövér:** strukturális elemekre (nevek, számok), ~20 per oldal.
- **„Te" perspektíva:** „Te éred el", nem „A felhasználó megkapja".
- **Alcímek:** előny-orientált, nem leíró.
- **Nincs agresszív CTA:** az ár és a próba / garancia a CTA.
- **Zsargon:** ha technikai, akkor „Az úgynevezett *X*, vagyis...".
- **Motívum-változatosság:** egy hook / metafora / kép (pl. anti-sztereotípia kép) max 2× szerepelhet a teljes oldalon. Ha ugyanaz a fordulat több szekcióban ismétlődik, vágd ki, és fogalmazd újra: minden szekciónak a saját szögéből kell újramondania az ígéretet. Egy sales-oldalon a 14 szekció így nem fárasztja az olvasót ugyanazzal a képpel.

**Minden 2-3 szekció után:** „Eddig stimmel?"

---

## 5. Összesítés + output

**Mielőtt generálod:** „Összefűzöm a teljes oldal-szöveget. Utolsó módosítás?"

**Sablon:**

```
## [Oldal neve] — [Oldaltípus] szöveg

### Összefoglaló
- **Oldaltípus:** [Termék sales / Fő-ajánlat sales / Regisztrációs / Landing / Köszönöm]
- **Cél:** [vásárlás / regisztráció / feliratkozás / megerősítés]
- **Termék:** [...]
- **Célcsoport:** [...]
- **Ajánlat:** [ha van — terméknév, ár]

### Oldalstruktúra

| # | Szekció | Layout |
|---|---------|--------|
| 1 | Hero | Képszöveg |
| 2 | [...] | [...] |
| ... | ... | ... |

---

### 1. Hero
**Layout:** Képszöveg

**Főcím:** [szöveg]
**Alcím:** [szöveg]

[Leíró bekezdés]

- [X] óra tananyag
- [X] tartalom-egység
- [X] melléklet

---

### 2. [Szekció neve]
**Layout:** [...]

**Főcím:** [...]

[Szöveg]

---

[... minden szekció ...]
```

**Notion-mentés:** „Mentsem a Notion kampány-oldalra?" Ha igen: `notion-update-page` vagy `notion-create-pages` (aloldalként).

---

## 6. Minőségi checklist

Minden oldal írásakor ellenőrizd:

- [ ] Van hero a 3 adat-ponttal? (idő, tartalom-egység, melléklet)
- [ ] Az alcím felszólítás vagy kontraszt? (nem leírás!)
- [ ] Van social proof az első 2 szekcióban?
- [ ] Van 5 probléma / vágy / eredmény variáns, mindegyikhez 3 címsor + 3 alcím-opció?
- [ ] A „Kinek való" 3-4 personát tartalmaz?
- [ ] A „Mire leszel képes" pontosan 3 félkövér pontot tartalmaz, 3-4 mondat kifejtéssel?
- [ ] A termék szerkezete max 3-4 modulcsoportot mutat (nem egyedi egységeket)?
- [ ] Ha előfizetés része: az 5 standard fő-ajánlat-előny benne van?
- [ ] Az ár bruttóban félkövér, nettó zárójelben?
- [ ] A GYIK tartalmaz standard kérdéseket?
- [ ] Nincs agresszív CTA?
- [ ] A szöveg a célzónában van? (6.000–9.000 kar termék sales-nél)
- [ ] A mondatok 47%+ rövid (≤8 szó)?
- [ ] Nincs 3 mondatnál hosszabb bekezdés?
- [ ] Layout-javaslat minden szekcióhoz?
