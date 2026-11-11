# Webinár Script Író: workflow-részletek

> Részletes lépések, kérdéssor, kirakósdarab-választó listák, output-sablon, mély mód. A SKILL.md „Hogyan dolgozz" szekciójának kibontása.
>
> 🟡 SABLON: a path-ok és példák placeholdert tartalmaznak — cseréld a saját vault-od adataira.

## Tartalom

1. [Márkahang és formázás](#márkahang-és-formázás)
2. [1. lépés: Kontextus + webinár-azonosítás](#1-lépés-kontextus--webinár-azonosítás)
3. [2. lépés: Struktúra / vázlat](#2-lépés-struktúra--vázlat)
4. [3. lépés: Script-írás + output](#3-lépés-script-írás--output)
5. [Mély mód](#mély-mód)

---

## Márkahang és formázás

Minden generált szövegben (output, sablon-kitöltés, javaslat) kövesd a `00-agy/brand/markahang.md` szabályait (I. Alapelvek + II. Mit ne). Tipikus minták (a konkrét szabályokat a cég `markahang.md`-je adja):

- **Mondatközi gondolatjel:** SOHA. Használj vesszőt, kettőspontot, zárójelet, vagy bontsd két mondatra.
- **Megszólítás:** a cég-hang szerint (pl. tegezés végig, ha a hang tegező), keveredés nélkül.
- **Mondatszerkezet:** rövid, pattogós mondatok + közepes magyarázók. Max 3 sor / bekezdés.
- **Redundancia:** ne ismételd meg ugyanazt a gondolatot más szavakkal.
- **AI-minták kerülése:** ne írj retorikusan túlcsiszolt mondatokat.
- **„Nem X, hanem Y" tiltás:** az AI leggyakoribb és legfárasztóbb szerkezete. Max 1× per teljes szöveg, és csak ha a kontrasztnak valódi retorikai funkciója van. Helyettesítési stratégiák:
  - **Töröld az első felet.** Ha a „hanem" utáni rész önmagában megáll, a tagadó fél felesleges.
  - **Kezdd a lényeggel.** ❌ „Nem több funkció kell, hanem egy rendszer." → ✅ „Egy működő rendszer kell."
  - **Két külön mondat.** ❌ „Nem a technológia a fontos, hanem a folyamat." → ✅ „A folyamat számít. A technológia másodlagos."
  - **Kérdéssel oldd fel.** ❌ „Nem az a kérdés, melyik jobb. Hanem az, hogy használod-e." → ✅ „A kérdés: használod-e egyáltalán?"

---

## 1. lépés: Kontextus + webinár-azonosítás

### Cél
Termék-kontextus betöltése, webinár-téma és paraméterek meghatározása.

### Lépések

1. Töltsd be az elérhető kontextust (lásd SKILL.md → Kontextus). Ha léteznek, használd: `00-agy/brand/markahang.md` (I. Alapelvek + II. Mit ne + III. Hirdetés / videoszkript fókusz) + `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md` + `00-agy/brand/ajanlatok/<ajanlat>/kontextus-elemek.md` (webinár-változók) + `celcsoport.md` + `uzenetek.md` + `00-agy/brand/ajanlatok/<ajanlat>/testimonialok.md`. **Ha valamelyik nem létezik, ne állj le** — a hiányzó infót a felhasználótól vagy a beillesztett anyagból pótold.
2. Jelezd: ha volt kontextus-fájl → „Webinár scriptet írunk. Betöltöttem a kontextust." Ha nem volt → „Webinár scriptet írunk. Nem találtam kontextus-fájlt, párat rákérdezek."
3. Kérdezd: „Melyik termékhez vagy ajánlathoz készül a webinár?" A többit (célcsoport, pitch-elt ajánlat, hang) az ajánlat mappája adja; csak azt kérdezd, ami ott `KITÖLTENDŐ`.

### Kérdések (max 5)

1. **Melyik termék / ajánlat?** Ha van Notion kampány-oldal: „Add meg az URL-t, betöltöm onnan."
2. **Mi a webinár témája vagy címe?** Mi a fő ígéret?
3. **Ki az előadó?** A fő-előadó egyedül, vagy van vendég / társelőadó? (Ha vendég: milyen stílusban beszél, mit tudunk róla?)
4. **Mennyi idő?** (alapértelmezés: ~60 perc)
5. **Egyből vásárlásra** vezeted, vagy **konzultációs hívásra** irányítod?

### Ha Notion kampány-oldalt kap
`notion-fetch`-csel betöltöd, kiemeled:
- Tölcsér terv (kampány-tervező): webinár-struktúra, kiválasztott kirakósdarabok
- Ajánlat-összefoglaló (ajánlat workshop): ajánlat, ár, bónuszok, garancia
- Célcsoport, fő ígéret
- Ne kérdezz olyat, ami már benne van.

### Ha nincs webinár-témája
Segíts:
- Milyen szisztéma szerint dolgozol?
- Milyen égető problémák vannak a célcsoportodnál?
- Milyen tévhitek vannak a piacodon?
- Mutass 2-3 példa-témát az adott termékhez.

### Összefoglalás

| Elem | Tartalom |
|------|----------|
| Termék / ajánlat | [...] |
| Téma / cím | [...] |
| Fő ígéret | [...] |
| Előadó | [...] (fő-előadó egyedül / vendég / társelőadó) |
| Célcsoport | [...] |
| Fő ajánlat | [...] |
| Ajánlat típus | Közvetlen vásárlás / Konzultáció |
| Időtartam | [...] |

→ „Stimmel? Menjünk tovább a struktúrára."

---

## 2. lépés: Struktúra / vázlat

### 2A: Kirakósdarabok kiválasztása

**Ha VAN kampány-tervező output:** Mutasd az elemeket, kérdezd: „Ez így stimmel, vagy változtatnál?"

**Ha NINCS:** Mutasd a lehetőségeket.

**Alapozás, válassz ezekből:**
- ☐ Üdvözlés (~3 perc small talk)
- ☐ Nagy ígéret
- ☐ Mi NEM kell hozzá
- ☐ Fájdalom és probléma
- ☐ Rövid tematika
- ☐ Nincs visszaút
- ☐ Bemutatkozás
- ☐ Ügyfélsztorik
- ☐ Vágyott állapot
- ☐ Maradj velem
- ☐ Kinek való / Kinek nem való

**Tartalom, melyik megközelítés?**
- ☐ A) Módszertan-bemutatás: saját keretrendszer lépései
- ☐ B) Titok/tévhit-alapú tanítás: 3-5 pont, mindegyik egy tévhitre épül

**CTA, válassz ezekből:**
- ☐ Tartalom összefoglalása
- ☐ Válaszút / Döntés helyzete
- ☐ Ajánlat felvezetése
- ☐ Ügyfélsztorik
- ☐ Árprezentáció (érték-halmozás)
- ☐ Bónuszok bemutatása
- ☐ Limitációk (sürgetés)
- ☐ Garancia
- ☐ Hogyan tovább (link/CTA)
- ☐ Kérdezz-felelek (Q&A)

### 2B: Tartalom-blokk kidolgozása

**Ha A) Módszertan:**
- Mi a keretrendszered neve?
- Milyen lépésekből áll? (3-5)
- Melyik lépésnél van a legtöbb tévhit?

**Ha B) Titok/tévhit-alapú:**
- Hány pontot tanítasz? (ajánlott: 3-5)
- Minden pontnál:
  1. Mi a tévhit / hiba?
  2. Mi a valóság / jobb megoldás?
  3. Van hozzá sztori, szám, vagy példa?

**Ha elakad:** Segíts a `sablonok-katalogus.md` 4. szekciójának formuláival, mutass 3-5 releváns tévhitet a termék niche-éhez.

### 2C: Nagyvonalú vázlat generálása

| # | Szakasz | Elem | Tartalom röviden | ~Idő |
|---|---------|------|------------------|------|
| 1 | Alapozás | Üdvözlés | Small talk, honnan jöttek | 3 perc |
| 2 | Alapozás | Nagy ígéret | [...] | 1 perc |
| ... | ... | ... | ... | ... |
| X | Tartalom | 1. tanítási pont: [...] | [...] | 10 perc |
| ... | ... | ... | ... | ... |
| Y | CTA | Válaszút | Döntés helyzete | 2 perc |

→ „Ez a vázlat stimmel? Ha igen, elkezdem megírni a scriptet."

---

## 3. lépés: Script-írás + output

### 3A: Alapozás script

Elemről elemre haladj:
1. Írd meg az elem scriptjét (read-aloud formátum)
2. Adj **[DIA]** blokkot
3. Ha releváns: ajánlj sztorit, metaforát
4. Mutasd meg

**Formátum:**
```
#### [Elem neve]
**[DIA: (szöveg/vizuál)]**

[Script szöveg, természetes, beszélt nyelven]
```

Minden 2-3 elem után: „Eddig stimmel?"

### 3B: Tartalom script

Tanítási pontonként haladj:

**Ha módszertan:** Minden lépéshez: felvezetés → bemutatás → szemléltetés → összegzés + átvezetés

**Ha titok/tévhit:** Minden ponthoz:
1. Tévhit bemutatása: „Sokan azt hiszik, hogy..."
2. Miért rossz ez
3. A jobb megoldás
4. Sztori / bizonyíték / szám
5. Összegzés + átvezetés

Minden tanítási pontnál:
- **[DIA]** blokkok a kulcspillanatokhoz
- **Interakció-javaslat:** hol vonj be (szavazás, kérdés)
- Ajánlj szemléltetést: sztori típus, metafora, szám

Minden pont után: „Ez így stimmel?"

### 3C: CTA script

**Ha van ajánlat workshop output:** Használd az elemeit (ár, bónuszok, garancia, limitáció, értékösszesítő).

**Ha nincs:** Kérdezd meg: termék neve és ára, bónuszok, garancia, korlátok.

Elemről elemre írd (válaszút, ajánlat, árprezentáció, bónuszok, limitációk, garancia, hogyan tovább, Q&A).

→ „Stimmel a CTA rész?"

### 3D: Összefűzés + output

„Összefűzöm a teljes scriptet. Utolsó módosítás?"

Generáld a Webinár Scriptet (kódblokkban, másolható):

```
## [Webinár címe]: Webinár Script

### Összefoglaló
- **Termék / ajánlat:** [...]
- **Téma:** [...]
- **Fő ígéret:** [...]
- **Előadó:** [...] (fő-előadó egyedül / vendég / társelőadó)
- **Célcsoport:** [...]
- **Időtartam:** ~[X] perc
- **Ajánlat:** [terméknév, ár]
- **Ajánlat típus:** [Közvetlen vásárlás / Konzultáció]

---

### I. ALAPOZÁS (~[X] perc)

#### [1. elem neve]
**[DIA: (szöveg/vizuál)]**

[Script szöveg]

---

[... minden kiválasztott alapozás-elem ...]

---

### II. TARTALOM (~[X] perc)

#### [1. tanítási pont címe]

**[DIA: (cím)]**

[Felvezetés script]

**[DIA: (tévhit/módszertan-lépés)]**

[Kifejtés script]

**[DIA: (megoldás/példa)]**

[Megoldás + sztori script]

**Interakció:** [kérdés/szavazás]

**[DIA: (összegzés)]**

[Összegzés + átvezetés]

---

[... minden tanítási pont ...]

---

### III. CTA (~[X] perc)

#### Tartalom összefoglalás
**[DIA: (főbb tanulságok)]**

[Összefoglaló script]

#### Válaszút
**[DIA: (Két lehetőség)]**

[Döntés helyzete script]

#### Ajánlat bemutatása
**[DIA: (terméknév)]**

[Ajánlat felvezetés script]

#### Árprezentáció
**[DIA: Értékösszesítő]**

[Érték-halmozás script]

**[DIA: Ár: [összeg]]**

[Ár bemutatás script]

#### Bónuszok
**[DIA: Bónusz 1]**

[Bónusz bemutatás script]

#### Limitációk
**[DIA: (határidő/korlát)]**

[Sürgetés script]

#### Garancia
**[DIA: (garancia neve)]**

[Garancia bemutatás script]

#### Hogyan tovább?
**[DIA: (link/QR kód/CTA)]**

[Záró instrukció script]

#### Kérdezz-felelek
**[DIA: Kérdések?]**

[Q&A bevezetés + előre elkészített kifogások]

---

### Dia lista

| # | Szekció | Dia típus | Szöveg/tartalom |
|---|---------|-----------|-----------------|
| 1 | Alapozás: Üdvözlés | Cím dia | [webinár cím] |
| 2 | Alapozás: Nagy ígéret | Pont dia | [...] |
| ... | ... | ... | ... |
```

### Notion-mentés

Ha van kampány-oldal → „Mentsem a scriptet a Notion kampány-oldalra?"
Ha igen: `notion-update-page` vagy `notion-create-pages` (aloldalként).

---

## Mély mód

Ha bármelyik elemnél „Részletesebben":
- Térj át lépésenkénti kérdezésre
- Használd a `sablonok-katalogus.md` teljes anyagát (kirakósdarabok, tévhit-formula, script-írási elvek)
- Minden kérdés után összefoglalás + „Stimmel?"
- Ha végzett: visszatérsz a gyors módhoz
