# DESIGN.md sablon

A Google nyílt `DESIGN.md` formátuma ([leírás](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md)), egy kiegészítéssel: a **Signature Elements** szakasszal. A szakaszcímek angolul maradnak, és ebben a sorrendben jönnek. A szöveg magyar. Ami nem releváns, az kimaradhat, de akkor kerüljön az `omitted` listába.

A YAML-ban csak egyszerű értékek legyenek: szín hexkóddal, idézőjelben (`"#1F2A24"`); minden érték idézőjelbe kerül, amiben `#` van (`border: "3px solid #8A1C47"`), mert a YAML a szóköz utáni `#`-tól megjegyzésnek veszi; méret `px` vagy `rem` egységgel, időtartam `ms`-mal. Másik értékre `{colors.primary}` alakban lehet hivatkozni.

**A színnevek szabálya** (ebből tudja az ellenőrző szkript, mit mivel mérjen):

- a szövegszínek neve `ink`-kel kezdődik (`ink`, `ink-muted`), a világos hátterek neve `neutral` vagy `surface` (`surface-alt`),
- minden színnek, amin szöveg áll, és ami nem világos háttér (fő szín, sötét szakasz), legyen `on-` párja: `primary` és `on-primary`, `night` és `on-night`. Sötét felületet ne nevezz `surface`-nek.
- A tokenek nevei angolok maradnak (az eszközök ezt értik); a beszédes magyar név a szövegbe kerül.

A YAML-ban nincs helye a nagybetűsítésnek, a mobil méreteknek és a szignó részleteinek: ezeket a szakaszok szövegébe írd. A mobil betűméreteket külön tokenként is megadhatod (`h1-mobile`).

````markdown
---
version: alpha
name: <A vállalkozás neve> design rendszer
description: <Egy mondat: milyen hatású, milyen referenciából.>
colors:
  primary: "#..."        # a fő kiemelés: gomb, link, fontos jel
  on-primary: "#..."     # szöveg a fő színen
  secondary: "#..."      # második kiemelés, mértékkel
  neutral: "#..."        # alap háttér
  surface-alt: "#..."    # váltó szakasz háttere
  night: "#..."          # sötét szakasz (ha van)
  on-night: "#..."       # szöveg a sötét szakaszon
  ink: "#..."            # szöveg
  ink-muted: "#..."      # halványabb szöveg (még olvasható)
  line: "#..."           # vonalak, szegélyek
typography:
  display:
    fontFamily: "<Google-betű>, Georgia, serif"   # a tartalékbetű a vessző után (talpatlannál: system-ui, sans-serif)
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.02em
  h1: { fontFamily: ..., fontSize: 56px, fontWeight: 400, lineHeight: 1.1 }
  h1-mobile: { fontFamily: ..., fontSize: 36px, fontWeight: 400, lineHeight: 1.1 }
  h2: { fontFamily: ..., fontSize: 40px, fontWeight: 400, lineHeight: 1.15 }
  h3: { fontFamily: ..., fontSize: 26px, fontWeight: 500, lineHeight: 1.25 }
  eyebrow: { fontFamily: ..., fontSize: 13px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.12em }
  body-lg: { fontFamily: ..., fontSize: 20px, fontWeight: 400, lineHeight: 1.6 }
  body: { fontFamily: ..., fontSize: 17px, fontWeight: 400, lineHeight: 1.65 }
  button: { fontFamily: ..., fontSize: 16px, fontWeight: 500, lineHeight: 1.3 }   # 1.3, hogy a két sorba törő gombfelirat se csússzon egymásra
rounded:
  none: 0px
  sm: 4px
  md: 12px
  full: 999px
spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 96px
  section: 128px
  content-width: 1200px
motion:
  hover: { duration: 200ms, timingFunction: ease-out }
  reveal: { duration: 700ms, timingFunction: "cubic-bezier(0.2, 0.7, 0.2, 1)" }
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 16px 32px
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  card:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 32px
  input:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
---

# <Név> design rendszer

## Overview

Két-három mondat a hatásról: milyen érzést keltsen, kinek, mennyire levegős vagy sűrű, mennyire visszafogott vagy merész.

**Referenciák:** <irányadó oldal> (az irány), <második oldal> (csak: …).

**Tárgyi világ:** <8-15 tárgy, anyag, szó, vesszővel>.

**Kerüljük:** <a szakma elcsépelt képi világa, amit a felhasználó nem szeret>.

## Colors

Színenként egy sor: beszédes név (a tárgyi világból), szerep, hol használd, és mennyit. Például: **Mohazöld (`primary`):** gombok és a kiemelt szó, oldalanként néhány helyen.

## Typography

Melyik betű mire, miért (egy mondat a karakteréről), és a kiemelés szabálya. Ha a címsor és a szöveg betűje más, írd le, hol nem keverhetők.

## Layout

Tartalomszélesség, szakaszok közötti tér, a levegős és a sűrű szakaszok váltakozása. Mobilon mi változik.

### Kompozíciós minták

(Csak a web rétegnél.) A referencia 4-6 jellemző szakasz-felépítése. Weboldal építésekor ezekből áll össze az oldal, és a képükön látszik, milyen arányokkal, rétegekkel, léptékkel.

| Minta | Hogyan áll össze | Referenciakép | Mire jó |
|---|---|---|---|
| Kettéosztott hero | bal oldalt sötét szövegpanel, jobb oldalt kifutó fotó, alatta futó szalag | `@referenciak/hero.jpg` | nyitás |
| … | … | … | probléma, ajánlat, bemutatkozás, CTA… |

## Elevation & Depth

Van-e árnyék, réteg, átfedés. Ha nincs, mondd ki: „Nincs árnyék: a mélységet a színváltás adja.”

## Shapes

Lekerekítés-szabály: mi kerek, mi szögletes, és miért.

## Motion

Egy-két mozdulat: mi mozog, mikor, mennyire. A tartalom animáció nélkül is látszódjon, és a csökkentett mozgás beállítását tartsd tiszteletben.

## Voice & Content Strategy

Egy-két sor. Ha van márkahang-fájl, csak hivatkozz rá.

## Components

Gomb (elsődleges, másodlagos), kártya, felső címke, űrlapmező, navigáció, lábléc. Komponensenként egy-két sor.

**Állapotok:** hover, fókusz (látható körvonal), letiltott, hiba; a gombra és a mezőre egy-egy sor.

**Logó:** a fájlok (`logo/logo.svg`, `logo-sotet.svg`, `logo-feher.svg`, `favicon.svg`), melyik hova, és mekkora szabad tér kell körülötte. Ha szöveges és ideiglenes, írd ki.

**Ikonok:** a család (például Lucide), vonalvastagság, alapméret, szín; ha vannak illusztratív ikonok, azok stílusa. Vagy: „nincs ikon, a rendszer nélküle működik”.

**Kis felület (eszköz, bővítmény-ablak):** betűskála, térköz, melyik díszítés marad.

## Signature Elements

A rendszer legfontosabb része: a díszítő eszköztár. **Csak azt töltsd ki, ami a referenciában megvan**, ugyanakkora léptékben és gyakorisággal; ami nincs, annál „nincs” áll, és nem pótolod. Elemenként: **mi ez**, **honnan jön** (a referencia melyik része; a tárgyi világ csak a tartalmat adja), **hol és oldalanként hányszor** használd, és ha kell, **hogyan készül** (CSS-ötlet, SVG-forma).

**Vizuális intenzitás: <1-5>.** Egy mondat arról, mitől ennyi (rétegzettség, tipográfiai lépték, kontraszt, részletgazdagság). A felhasználó ezt szóval állíthatja („legyen vagányabb”: egy fokkal feljebb).

| Eszköz | Mi ez | Honnan | Hol, hányszor |
|---|---|---|---|
| Szignó | … | … | legfeljebb 3-4 helyen |
| Címsorkezelés | … | … | … |
| Felső címke | … | … | … |
| Szekcióhatár 1 | … | … | … |
| Szekcióhatár 2 / elválasztó | csak ha a referenciában kétféle van | … | … |
| Háttérváltások | melyik szakasz milyen hátteret kap, milyen sorrendben | … | … |
| Dekor-réteg | … | … | … |
| Képkompozíció 1 | … | … | … |
| Képkompozíció 2 | csak ha a referenciában kétféle van | … | … |
| Kártyatípusok | … | … | … |
| Mozgó elem | szalag, kirajzolódás; vagy „nincs” | … | … |
| Vonalak | rácsvonal, keret, elválasztó: vastagság, szín, hol fut végig; vagy „nincs” | … | … |
| Illusztráció | stílus, szín, téma; vagy „nincs” | … | … |

**Képkezelés:** fotóstílus (tónus, fény, téma), kivágás, keret. Mi legyen a képeken, és mi ne.

**Ritmus:** egy példasor arra, hogyan követik egymást a szakaszok (például „sötét hero, szalag, világos szöveges, kártyás váltó háttéren, nagy kép, sötét CTA”). Két egymás utáni szakasz ne kapja ugyanazt a határt és képkompozíciót.

## Do's and Don'ts

- **Igen:** 4-6 pont.
- **Ne:** 4-6 pont, a referencia szándékos hiányaiból és a kerülendőkből.

## Agent Prompts

Kész utasítások a felhasználónak, bemásolásra:

- „Olvasd be a `design-rendszer/DESIGN.md`-t, nézd meg a `design-rendszer/referenciak/` képeit, és a kompozíciós mintákból építs egy landing oldalt ehhez a szöveghez: … A referenciaképek karakterét és intenzitását tartsd, a tartalmat és a fotókat a sajátunkból vedd.”
- „A `DESIGN.md` alapján készíts egy 1080×1350-es Instagram-posztot erről: …”
- „A `DESIGN.md` alapján készíts egy 16:9-es diát erről: …”
- „A `DESIGN.md` jellegzetességeivel tervezz egy ikont erről: …”
````
