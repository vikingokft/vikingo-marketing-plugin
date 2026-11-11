# Ajánlatok — portfólió

last_updated: 2026-11-02

A termékportfólió indexe. **Csak index** — minden ajánlat részletei a saját almappájában élnek.

## Portfólió

KITÖLTENDŐ. Ajánlatonként egy sor. Az „Egy mondatban" tényleg egy mondat legyen — a részletek a mappában vannak.

| Ajánlat | Egy mondatban | Státusz | Mappa |
|---|---|---|---|
| KITÖLTENDŐ | | aktív / szünetel / kivonva | `<ajanlat-slug>/` |

## Új ajánlat felvétele

```bash
cp -r 00-agy/brand/ajanlatok/_sablon 00-agy/brand/ajanlatok/<ajanlat-slug>
```

Aztán:
1. Vedd fel egy sorral a fenti táblába.
2. Töltsd ki az új mappa `_attekintes.md`-jét (státusz, felelős).
3. Töltsd ki, amit tudsz, a többi maradjon `KITÖLTENDŐ`. Meg is kérheted az AI-t, hogy a
   forrásanyagaidból töltse ki.

A slug ékezet nélküli, kisbetűs, kötőjelezett — mint a területeknél.

## Mi kerül ajánlat-szintre és mi cég-szintre

Ez a rendszer legfontosabb szabálya. Részletesen: [`../_attekintes.md`](../_attekintes.md).

**Röviden:** cég-szinten az, ami minden ajánlatra igaz. Ajánlat-szinten **csak a delta**.
Amit az ajánlat-fájl nem tartalmaz, azt a cég-szintről örökli.

## Csomag-térkép (létra)

Ha többszintű árazás van, itt látszik, hogyan viszonyulnak egymáshoz — mi a belépő, mi a fő
ajánlat, mi a felső szint, és mi a tipikus útvonal közöttük. Ez **portfólió-szintű** információ:
egyetlen ajánlat fájljából nem derül ki.

Az ár ide nem kerül értékként: a kanonikus otthona az ajánlat saját `kontextus-elemek.md`-jének
`### ár / árképzés` mezője. Az „Ár” oszlopba csak a hivatkozás kerül, hogy egy árváltozást egy
helyen kelljen átírni.

| Szint | Ajánlat | Ár | Kinek | Mi a következő lépés |
|---|---|---|---|---|
| Csali | KITÖLTENDŐ | ingyenes | | |
| Belépő | | lásd `<ajanlat-slug>/kontextus-elemek.md` | | |
| Fő | | lásd `<ajanlat-slug>/kontextus-elemek.md` | | |
| Felső | | lásd `<ajanlat-slug>/kontextus-elemek.md` | | |

## Csomag-akciók és bundle-ök

Két vagy több ajánlat együtt, saját áron. Nem tartozik egyik ajánlat mappájába sem — itt a helye.

KITÖLTENDŐ. Bundle-önként egy sor: mely ajánlatok, milyen áron, mikor élő, mi az indoklás.

## Kivont ajánlatok

KITÖLTENDŐ. Ha egy ajánlatot kivonunk, a mappája egy archív mappába (AI-oprendszerben a `99-archivum/00-agy/brand/ajanlatok/<slug>/`, önállóan a `00-agy/brand/ajanlatok/_archiv/<slug>/`)
kerül, és ide egy sor a dátummal meg az indokkal. Ne töröld — a régi szövegek még hivatkozhatnak rá.

## Karbantartás

- Új ajánlat bevezetésekor és kivonásakor a fenti tábla frissítendő.
- Ha egy változó **minden** ajánlat-fájlban ugyanaz, húzd fel a cég-szintű
  [`../kontextus-elemek.md`](../kontextus-elemek.md)-be, és töröld az ajánlat-fájlokból.
