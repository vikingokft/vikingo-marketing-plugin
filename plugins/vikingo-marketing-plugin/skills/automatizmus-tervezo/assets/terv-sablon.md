# [Flow neve] · automatizmus-terv

> Készült: [dátum] · Termék / ajánlat: [X] · Cél: [mit érjen el a flow]
> Készítette: automatizmus-tervezo skill · Megírás: az író-skill sorozat módja (`/email-iro` vagy `/email-iro`)

## Beállítás (ESP-független)

| Elem | Érték |
|---|---|
| **Trigger (mi indítja)** | [pl. feliratkozás a(z) [csali] űrlapon] |
| **Kilépési feltétel** | [pl. vásárlás bármikor → kilép a flow-ból] |
| **Párhuzamos flow-k kezelése** | [pl. a gondozó sorozat és a hírlevél csendes napokra vált a futás alatt / nincs párhuzamos flow / kizárás beállítva] |
| **Címke-javaslat** | [pl. `csali-X-feliratkozo`, belépéskor] |
| **Teljes hossz** | [X email, ~Y nap] |
| **Küldési idősáv** | [pl. reggel 8-10 között, a felhasználó időzónájában] |

## A flow lépésről lépésre

Minden sor egy elem, amit a szoftverben egymás után létrehozol. Négy elem-típus van: 📧 email, ⏱️ várakozás, 🔀 feltétel (elágazás), 🚪 kilépés.

| Lépés | Elem | Részletek |
|---|---|---|
| 1 | 📧 Email 1 | [név] · tárgy-irány: [3-5 szó] |
| 2 | ⏱️ Várakozás | [pl. 2 nap] |
| 3 | 🔀 Feltétel | [pl. kattintott az Email 1 linkjére?] |
| 3/IGEN | 📧 Email 2A | [név] |
| 3/NEM | 📧 Email 2B | [név] |
| … | … | … |

> Ha a lista kicsi (pár száz fő): [itt jelezd, ha az elágazás elhagyható, és mi a lineáris változat].

## Email-slotok részletesen

### Email 1 · [munkanév]

- **Időzítés:** [trigger + X]
- **Típus:** [a 13 kanonikus típusból]
- **A levél célja:** [1 mondat]
- **Üzenetmag / téma:** [a kontextusból]
- **Kulcs-elemek:** [mi kerüljön bele feltétlenül: link, határidő, bizonyíték…]
- **CTA:** [hova visz, mit kérünk]
- **Variáns-opciók:** [pl. rövid emlékeztető vs sztoris verzió, a felhasználó választ]

### Email 2 · [munkanév]

[ugyanez a szerkezet minden slotra]

## Mire figyelj ennél a flow-nál

- [a flow-kártya figyelmeztetései, a kontextusra vonatkoztatva]

## Eltérések a kártyától

- [KÖTELEZŐ szekció, mindig döntés születik: vagy TÉTELESEN felsorolod, mi tér el az eredeti flow-kártyától (trigger, slot, időzítés, elágazás, CTA-mechanizmus) és miért, vagy ha semmi, egyetlen sor: „Nincs eltérés a kártyától." A CTA-típus cseréje (pl. vásárlás helyett időpontfoglalás) is eltérés!]

## Nyitott pontok

- [minden `[KITÖLTENDŐ]` mező listája, hogy egy helyen látszódjon, mi hiányzik]

## Következő lépés

1. Terv jóváhagyása.
2. Levelek megírása: az író-skill sorozat módja (`/email-iro`). Input: ez a terv + a kontextusfájl + (ha van) az email-hang profil.
3. Beállítás a saját email-szoftveredben a „lépésről lépésre" tábla alapján.
