# Testimonial elosztási workflow (Batch mód)

> A nyers `testimonialok.md`-ből hogyan kerül a rendszer többi pontjára. Negyedéves vagy ad hoc futás.

## A testimonialok útja (áttekintés)

```
testimonialok.md (nyers adatbázis)
        │
        ├──→ Termék-kontextus fájlok (Visszajelzések, eredmények szekció)
        │       → Sales-oldalak, hirdetések, email-sorozatok
        │
        ├──→ Célcsoport-avatarok (celcsoport-avatarok.md)
        │       → Problémák, vágyak, kifejezések validálása/bővítése
        │
        ├──→ Marketing-üzenetek (marketing-uzenetek.md)
        │       → Üzenetmagok társadalmi bizonyítékkal feltöltése
        │
        └──→ Testimonial-következtetések (testimonial-kovetkeztetesek.md)
                → Minták, insightok, felhasználható narratívák
```

---

## 1. Termék-kontextus fájlok feltöltése

### Mi kerül ide

A `Visszajelzések, eredmények` szekcióba **termékenként a 3-5 legerősebb idézet** — ami specifikus eredményt, transzformációt vagy meggyőző ajánlást tartalmaz.

### Válogatási szempontok

1. **Specifikus eredmény > általános dicséret** („Már lett is belőle munkám" > „Szuper vagytok")
2. **Azonosulható háttér** — ha van foglalkozás/kontextus, az erősebb
3. **Egyedi szempont** — ne 5 ugyanolyan, hanem különböző szögből
4. **Arc = igen** preferált (ha van, sales-oldalon használható)

### Formátum

```markdown
> „Idézet szövege"
> — **Név**, foglalkozás/kontextus (exit/onboarding)
```

Ha van konkrét eredmény: `**Eredmény:** ...` kiemelve.

---

## 2. Célcsoport-avatarok validálása

### Mi a cél

A testimonialokból kiderülő **valós problémák, vágyak, kifejezésmódok** visszavezetése az avatarokba. Ez validálja a `[h]` hipotézis-jelölésű pontokat.

### Folyamat

1. A `celcsoport.md` minden avatarjánál átnézni a `[h]` jelölésű hipotéziseket
2. Ahol testimonial ERŐSÍT → `[h]` → `[v]` (validált) + testimonial-szám-hivatkozás
3. Ahol testimonial ELLENTMOND → jelölni és felülvizsgálni
4. Új problémákat / vágyakat is felvenni, ha a testimonialokból kiderül

### Tipikus validációs pontok (sablon)

| Avatar | Testimonialból validálható | Jellemző entry-szám |
|---|---|---|
| 1. avatar | „[a probléma saját szavaival]", „[a vágy saját szavaival]" | #X, #Y |
| 2. avatar | „[jellemző fájdalom]" | #X |
| 3. avatar | [karrierváltás-sztori / élethelyzet] | #X, #Y |
| 4. avatar | „[jellemző kifejezés]" | #X, #Y |

---

## 3. Marketing-üzenetek bővítése

### Mi a cél

A `uzenetek.md` üzenetmagjaihoz **társadalmi bizonyíték** (social proof) hozzárendelése — konkrét idézetek, amik az üzenetet alátámasztják.

### Üzenetmag ↔ testimonial mapping (sablon)

| Üzenetmag | Testimonial-példák |
|---|---|
| „Egyedül vagyok ezzel" | #X, #Y |
| „Nem vagyok elég jó" | #X, #Y |
| „Lemaradok" | #X, #Y |
| „Nem tudom hol kezdjem" | #X, #Y |
| „Nincs időm" | #X (saját tempó-idézet) |
| „Nem engedhetem meg" | #X (ár-relativizáló idézet), #Y |
| „[X] nem elég" (összehasonlító) | #X, #Y |
| „Nem értem [a témát]" | #X, #Y |
| „Nem egyedül tanulsz" | #X, #Y |
| „Van rendszer, nem káosz" | #X, #Y |

### Folyamat

Minden üzenetmag leírásához adj egy `### Társadalmi bizonyíték` alszekcót 2-3 idézettel.

---

## 4. Testimonial-következtetések dokumentum

> Fájl: `00-agy/brand/ajanlatok/<ajanlat>/testimonialok.md`

### Tartalom

1. **Visszatérő minták** — mit mondanak legtöbben, ismétlődő szavak/témák
2. **Legerősebb idézetek top 10** — bármilyen sales-anyagban azonnal használhatók
3. **Karrierváltás-sztorik** — legmélyebb transzformációk
4. **Termék-specifikus insightok** — mit emelnek ki az egyes termékeknél
5. **Hiányok és lehetőségek** — melyik avatar / termék alulreprezentált
6. **Felhasználási javaslatok csatornánként** — sales-oldal, hirdetés, email, social, webinár

---

## 5. Ismétlődő workflow — „Új testimonial-csokor érkezett"

### Mikor fut

- **Negyedévente** (Q1, Q2, Q3, Q4) amikor új onboarding/exit-elemzések készülnek
- **Ad hoc** amikor visszajelzés-adatbázisba új entry kerül

### 4 lépés

```
1. GYŰJTÉS
   ├── Exit-kérdőív elemzések (termékenként)
   ├── Onboarding-kérdőív elemzések (termékenként)
   ├── Visszajelzés-adatbázis (új entry-k)
   └── Output: testimonialok.md bővítése, következő sorszámtól

2. SZŰRÉS + CÍMKÉZÉS
   ├── Minden új entry-t jelölni: termék, típus (exit/onboarding/általános)
   ├── Van-e konkrét eredmény? → Igen/Nem
   ├── Van-e arc? → Igen/Nem
   └── Erősségi besorolás: A (sales-ready) / B (kontextus) / C (statisztikai)

3. ELOSZTÁS
   ├── A-szintű → termék-kontextus Visszajelzések szekció frissítés
   ├── A+B-szintű → testimonial-kovetkeztetesek.md frissítés
   ├── Problémát/vágyat említő → celcsoport-avatarok.md ellenőrzés
   ├── Üzenetmagot erősítő → marketing-uzenetek.md social proof
   └── Minden → testimonialok.md (nyers adatbázis) — itt marad

4. KONTEXTUS FRISSÍTÉS KÉSZ
   └── A marketing-skillek automatikusan a friss kontextust használják
```

### Checklist sablon (copy-paste)

```markdown
## Testimonial-feldolgozás — [ÉV] [NEGYEDÉV]

- [ ] Exit-elemzések lekérése
- [ ] Onboarding-elemzések lekérése
- [ ] Visszajelzés-adatbázis ellenőrzése
- [ ] Új entry-k hozzáadása testimonialok.md-hez
- [ ] Szűrés: A / B / C besorolás
- [ ] Termék-kontextus fájlok Visszajelzések szekció frissítése (A-szintű)
- [ ] celcsoport-avatarok.md validáció ([h] → [v])
- [ ] marketing-uzenetek.md social proof frissítés
- [ ] testimonial-kovetkeztetesek.md frissítés
- [ ] Statisztikák frissítése (testimonialok.md statisztika-szekció)
```
