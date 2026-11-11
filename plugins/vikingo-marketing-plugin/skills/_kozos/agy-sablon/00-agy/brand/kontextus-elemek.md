# Kontextus-elemek — cég-szint (univerzális változók)

last_updated: 2026-11-02

> **Mi ez:** azok a szövegíró-változók, amelyek **minden ajánlatnál ugyanazok**. Innen örökli
> mindegyik ajánlat, tehát itt egyszer kell megírni.
>
> **Ide csak az kerül, ami ajánlattól független.** Ha egy érték ajánlatonként más (ár, csomag,
> fő eredmény, fő fájdalom), az az ajánlat mappájába tartozik:
> `ajanlatok/<ajanlat>/kontextus-elemek.md`.
>
> **A mezőnevek szerződés** — ugyanaz a névtér, mint ajánlat-szinten, hogy az öröklés működjön.
>
> **Csak érték, nulla érvelés.** A „miért" a [`uzleti-profil.md`](uzleti-profil.md)-ban,
> [`celcsoport.md`](celcsoport.md)-ban és [`versenytarsak.md`](versenytarsak.md)-ban él.

Ami még nincs meg, maradjon `KITÖLTENDŐ`. Amit tudatosan nem használtok (például nincs egységes garancia), oda `nincs` kerül. A hiányzó mező jobb, mint a kitalált érték.

---

## I. Ajánlat változók

### termékkategória
KITÖLTENDŐ — mit adunk el általában („online kurzusok", „tanácsadás").

### ár / árképzés
KITÖLTENDŐ — az általános ár-keret, ha van („49–297e Ft"). Konkrét ár az ajánlatnál.

### kedvezmény mértéke
KITÖLTENDŐ — csak ha a cégnek egységes akció-politikája van.

### kuponkód
KITÖLTENDŐ — cég-szintű, minden ajánlatra érvényes kód.

### garancia
KITÖLTENDŐ — az **egységes** garancia. Ha ajánlatonként más, ide `nincs` kerül, és az érték az ajánlatnál él.

---

## II. Bizonyíték változók

### ügyfélszám / közösség méret
KITÖLTENDŐ — a cég összes ügyfele/tagja.

### értékelés / review
KITÖLTENDŐ — cég-szintű átlag és darabszám.

### szakértő / tekintély
KITÖLTENDŐ — az alapító/csapat hitelessége. Részletek: [`csapat.md`](csapat.md).

### adat / kutatás
KITÖLTENDŐ — saját mérés vagy hivatkozható kutatás, amit rendszeresen idézünk.

### díj / elismerés
KITÖLTENDŐ — sajtó, díj, tanúsítvány.

---

## III. Célcsoport változók

### megszólítás
KITÖLTENDŐ — ahogy a célcsoportot hívjuk. Szegmensek: [`celcsoport.md`](celcsoport.md).

### identitás
KITÖLTENDŐ — a cég által kínált önkép, ajánlattól függetlenül.

---

## IV. CTA változók

### cselekvés ige
KITÖLTENDŐ — az alap-ige („Csatlakozz", „Nézd meg").

---

## V. Operatív elemek

Nem sablon-változók, de cég-szinten állandók.

### alap-CTA
KITÖLTENDŐ — a default cselekvésre hívás, ha az ajánlat nem ad sajátot.

### megrendelés-folyamat
KITÖLTENDŐ — hogyan vásárol valaki (kosár, számlázás, hozzáférés).

### jogi háttér
KITÖLTENDŐ — cégnév, adószám, ÁSZF-link, amit hirdetésnél kérnek.

### csapat-méret
KITÖLTENDŐ — hányan vagyunk (hitelesség és kapacitás-állításokhoz).

### szállítási díj
KITÖLTENDŐ — fizikai terméknél a díj („690 Ft-tól"). Szolgáltatásnál `nincs`.

### ingyenes szállítás küszöbe
KITÖLTENDŐ — az az összeg, ami felett nincs szállítási díj („14 000 Ft felett").

### szállítási idő
KITÖLTENDŐ — mennyi idő a kézbesítés („akár 24 órán belül").

### visszaküldés / elállás
KITÖLTENDŐ — hány nap, milyen feltétellel. A pénzvisszafizetési garanciát a `### garancia` mező viszi; ide a visszaküldés gyakorlata jön.
## Karbantartás

- Ha egy érték itt **és** egy ajánlat-fájlban is ugyanaz, töröld az ajánlat-fájlból.
- Ha itt kitöltesz valamit, ami mégis ajánlatonként változik, vidd le ajánlat-szintre.
- A `last_updated`-et minden érdemi változtatásnál frissítsd.
