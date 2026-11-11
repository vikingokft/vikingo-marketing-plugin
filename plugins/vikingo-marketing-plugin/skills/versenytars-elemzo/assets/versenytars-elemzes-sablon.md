# Versenytárs-elemzés sablon

Ezt a formátumot illeszd be az `00-agy/brand/versenytarsak.md` megfelelő szekciójába a Fázis 4-ben. Meglévő versenytársnál bővítsd, új versenytársnál hozz létre új szekciót.

```markdown
#### {{Versenytárs neve}}

- **Téma:** {{téma}}
- **Kategória:** {{kategória — lásd references/pozicionalas.md}}
- **Weboldal:** {{URL}}
- **Nyelv:** {{nyelv}}

**Mélyelemzés ({{dátum}}):**

- **Pozicionálás:** {{1-2 mondat}}
- **Fő üzenetek:**
  - {{headline 1}}
  - {{headline 2}}
- **Trigger-ek (legerősebbek):** {{felsorolás 3-5 legmarkánsabbról a 29-ből}}
- **Tölcsér:** {{típus — csali / webinár / kihívás / mini / kevert}}
- **Erős oldal:**
  - {{1-2 bullet}}
- **Gyenge oldal / fehér folt:**
  - {{1-2 bullet}}
- **Adaptálható hozzánk:**
  - {{2-3 bullet — a legértékesebb rész!}}
- **Tanulság-prioritás:** {{azonnali / közepes / hosszú táv}}

**Források (az elemzéshez használt anyagok):**
- {{URL-ek, screenshot-leírások, social-poszt-számok}}
```

## Output-formátum elve

- **Tömör** — a `versenytarsak.md` sok versenytársat tart, nem férnek bele hosszú elemzések.
- **Bullet-fókuszú** — az „Adaptálható" rész a leg-fontosabb, ott legyen 2-3 konkrét, cselekvésre fordítható tanulság.
- **Dátum-pecsételve** — ha 6 hónap múlva visszanézed, lásd mi mikor készült.

## Mikor használj batch módú formátumot

Ha a felhasználó egyszerre 5+ versenytársat akar (Batch mód), akkor ne ezt a részletes formátumot használd. Helyette egy táblázat:

```markdown
## Batch-elemzés ({{dátum}}): {{X}} versenytárs

| Versenytárs | Pozicionálás | Fő üzenet | Top trigger | Tölcsér | Adaptálható |
|---|---|---|---|---|---|
| {{név 1}} | ... | „..." | ... | ... | ... |
| {{név 2}} | ... | „..." | ... | ... | ... |
```

Részletes elemzéshez később egyenként visszatérni.
