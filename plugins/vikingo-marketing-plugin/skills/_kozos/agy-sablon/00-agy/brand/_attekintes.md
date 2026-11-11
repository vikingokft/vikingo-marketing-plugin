# Brand — áttekintés

last_updated: 2026-11-02

A cég „ki vagyok én" rétege. Minden vevő felé menő szöveg innen dolgozik: márkahang, vizuális arculat, csapat, történetek, versenytársak — és az ajánlatok.

## Kanonikus fájlok

- [`markahang.md`](markahang.md): hogyan beszél a cég. **Ez a legfontosabb** — nélküle Claude generikus hangon ír.
- [`arculat.md`](arculat.md): vizuális arculat, színek, tipográfia, design-tokenek.
- [`csapat.md`](csapat.md): kulcsemberek, és ha valakinek eltér a hangneme.
- [`sztoribank.md`](sztoribank.md): újrahasznosítható történetek, anekdoták, eredetmítosz.
- [`versenytarsak.md`](versenytarsak.md): cég-szintű versenytárs-térkép három osztályban.
- [`kontextus-elemek.md`](kontextus-elemek.md): a **cég-szintű univerzális hirdetési változók** (ár-keret, garancia, ügyfélszám…).
- `ajanlatok/_attekintes.md`: a termékportfólió indexe. Ajánlatonként egy almappa.

## A három szabály, ami megakadályozza a duplikációt

Ez a réteg két szinten él (cég és ajánlat), ezért kellenek szigorú szabályok. Ha ezeket
betartod, ugyanaz a tény soha nem lesz két helyen.

**1. Egy változó egy szinten él.**
Cég-szinten az, ami **minden** ajánlatra igaz. Ajánlat-szinten **csak a delta** — ami ennél
az ajánlatnál más. Amit az ajánlat-fájl nem tartalmaz, azt a cég-szintről örökli.

**2. A `kontextus-elemek.md` a változó-értékek kanonikus otthona.**
Az ár, a garancia, a kuponkód, a fő fájdalom, az identitás **ott** él és csak ott. A narratív
fájlok (`kontextus.md`, `celcsoport.md`, `uzenetek.md`) nem ismétlik meg őket — hivatkoznak rájuk.

**3. A narratív fájlok a „miért" otthona.**
Az érvelés, a mélységi profil, az elemzés ott él. A változólistába **nem** kerül érvelés —
oda érték kerül.

## Miért éppen ilyen a `kontextus-elemek.md`

Nem szabadon választott formátum: a szövegírás sablonjai nevesített változókra épülnek
(`ár`, `garancia`, `fő fájdalom`, `identitás`…). A mezőnevek tehát rögzítettek: ha átnevezed
őket, a sablonok nem találják meg az értéket.

## Hogyan töltődik ki

Az építő-skillek (`brand-specialista`, `termek-specialista`) beírják, amit a feltöltött anyagaidból egyértelműen tudnak, az ajánlatokat és a
`kontextus-elemek.md` értékeit is. Ami nem derül ki, `KITÖLTENDŐ` marad, és munka közben gyűlik:
ha az AI-jal ajánlatot, célcsoportot vagy versenytársat elemzel, kérd meg, hogy írja ide.

Kézzel csak a **kemény értékeket** frissítsd: ár, kuponkód, ügyfélszám, ezek avulnak el.

## Új ajánlat felvétele

```bash
cp -r 00-agy/brand/ajanlatok/_sablon 00-agy/brand/ajanlatok/<ajanlat-slug>
```

Aztán vedd fel egy sorral az `ajanlatok/_attekintes.md` portfólió-táblájába.

## A kész szövegek helye

A kész szöveg **nem ide kerül**, mert az időhöz kötött eredmény. AI-oprendszerben a `03-projektek/` vagy
a `02-allando-teruletek/` alá megy, önálló marketing-mappában a `kimenetek/` alá (a pontos szabály: `_kozos/marketing-kontextus.md`, Hova kerül a kész anyag). Ez a mappa a tartós igazság, nem a legyártott anyag.

## Karbantartás

- Az `arculat.md` és a `sztoribank.md` lassan változik — évente elég átnézni.
- A `kontextus-elemek.md` kemény értékeit **negyedévente** vagy árváltozáskor.
- A `versenytarsak.md`-t akkor, ha új szereplő jelenik meg vagy egy régi kilép.
