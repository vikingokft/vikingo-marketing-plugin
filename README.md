# Marketing skill-csomag (v1.3.0)

22 magyar nyelvű marketing-skill Claude Code-hoz és Codexhez. A céged saját márkahangján
és termékein dolgoznak: először felépítik a márka-alapodat, aztán abból írnak e-mailt,
hirdetést, sales-oldalt, landing oldalt és a többit.

## Mi új a 1.3.0-ban

- **Minden landing-recept:** a `landing-szovegiro` már nem csak az alapoldalt írja, hanem mind a
  25 receptet ismeri (letölthető csali, webinár és esemény, kihívás, értékesítési oldal,
  szolgáltatás). Az elején ajánl egyet az ajánlatod szerint, és rákérdez.
- **Új: `landing-design`.** A kész szövegből és 1-3 tetsző oldalból (inspirációból) tervezi meg
  és építi fel az oldalt, böngészőben ellenőrizve.
- **Új: `landing-elesites`.** A kész oldalt FTP-re feltölthető mappává, Elementorba és
  WordPress HTML blokkba illeszthető kóddá, és médiatárba tölthető képmappává csomagolja.

## Mi volt új a 1.2.0-ban

- **Landing oldal az elejétől a végéig:** a `landing-szovegiro` megírja az oldal szövegét,
  a `szoveg-emberiesito` kiszedi belőle az AI-ízt, a `landing-epito` pedig kész HTML oldalt
  épít belőle (WordPress-be illeszthető változattal együtt).
- **Egy közös márka-alap:** minden skill ugyanabból a `00-agy/brand/` mappából dolgozik. Ha még
  nincs ilyened, a `brand-specialista` az első futáskor létrehozza (megkérdez előtte). Ha
  AI-oprendszert használsz, a meglévő agyadból dolgozik.
- **A kész anyagok helye:** önálló mappában a `kimenetek/<típus>/<ajánlat>/` (például `kimenetek/landing/<ajánlat>/`), AI-oprendszerben a birtokló projekt mappája (`03-projektek/<projekt>/<típus>/<ajánlat>/`).
- **Kikerült:** a `csali-kontextus-epito` (a csali kontextusát mostantól a `termek-specialista`
  csali módja építi) és a `session-zaras`.

## Telepítés: Claude Code

Írd be a Claude Code-ba ezt a két parancsot, egymás után:

```
/plugin marketplace add vikingokft/vikingo-marketing-plugin
```

```
/plugin install vikingo-marketing-plugin@vikingo
```

Utána indítsd újra a Claude Code-ot.

Ha korábban zipből töltötted fel a csomagot (1.0, 1.1, 1.2 vagy 1.3), előbb távolítsd el azt a
**Customize → Personal plugins** alatt, hogy a skillek ne látsszanak kétszer.

## Telepítés: Codex

Terminálban:

```bash
codex plugin marketplace add vikingokft/vikingo-marketing-plugin
```

```bash
codex plugin add vikingo-marketing-plugin@vikingo
```

## Hol dolgozz

Nyiss meg egy külön mappát a marketingednek (például `Dokumentumok/marketing`), és onnan
indítsd a Claude-ot. A skillek ide építik fel a márka-alapodat (`00-agy/brand/`), és ide teszik
a kész anyagokat (`kimenetek/`). Ne egy weboldal forráskódjában vagy más projektben indítsd.

A landing oldalhoz a fotóidat és a logódat a `kimenetek/landing/<ajánlat>/forrasok/` alá tedd
(a fotókat a `forrasok/kepek/` alá), a tetsző oldalak képernyőképeit pedig az `inspiracio/` alá; a `landing-design` és a `landing-epito` ott keresi őket.

**Ha AI-oprendszert használsz:** a skillek a meglévő `00-agy/brand/`-edből dolgoznak, a kész anyag
pedig a birtokló projektbe kerül (ha nincs, a skill javasolja az `uj-projekt`-et). A munkaterületednek
lehet saját `szoveg-emberiesito` skillje; a landing oldalhoz ennek a csomagnak a változata kell
(`/vikingo-marketing-plugin:szoveg-emberiesito`), mert csak az ismeri a landing módot.

## Milyen sorrendben

1. **`brand-specialista`**: a márka-alap. Az első futáskor létrehozza a `00-agy/brand/` mappát.
2. **`markahang-elemzo`**: a márkahangod 3-5 meglévő szövegedből.
3. **`termek-specialista`**: egy termék vagy csali (lead magnet, webinár, kihívás) kontextusa.
4. **`celcsoport-elemzo`, `versenytars-elemzo`, `testimonial-elemzo`**: mélyítés, ha kell.
5. **`ajanlat-workshop`**: az ajánlat összerakása.
6. **`kampany-tervezo`**, **`automatizmus-tervezo`**: kampány-, tölcsér- és e-mail-automatizmus terv.
7. **Írók**: `email-iro`, `hirdetes-szovegiro`, `hirdetes-video-script-iro`, `sales-oldal-iro`,
   `webinar-script-iro`, `social-tartalom-tervezo`, `landing-szovegiro`, és az oldalakhoz a `ux-tervezo`.
8. **Befejezés**: `szoveg-emberiesito` bármilyen kész szövegre, `feladat-iro`, ha valamit át kell
   adnod egy segítőnek.

**A landing oldal sorrendje:** `landing-szovegiro` (szöveg, recept szerint) → `szoveg-emberiesito`
(ezt a szövegíró magától lefuttatja) → `landing-design` (az oldal HTML-ben; a régebbi
`landing-epito` is jó, ha nincs inspirációd) → `landing-elesites` (FTP és WordPress).

## Hogyan hívd meg

- **Természetesen:** „írj egy üdvözlő e-mailt a termékemhez”, és a megfelelő skill elindul.
- **Név szerint:** `/vikingo-marketing-plugin:email-iro`.
- Ha valami hiányzik, a skill egy üzenetben rákérdez, a válaszodat pedig beírja a márka-alapba,
  hogy legközelebb ne kelljen újra megadnod.

## Frissítés

Új változatnál a Claude Code-ban:

```
/plugin marketplace update vikingo
```

Ha a **/plugin → Marketplaces** alatt bekapcsolod az automatikus frissítést, ez magától megy.
A saját `00-agy/` és `kimenetek/` mappádhoz a frissítés nem nyúl.
