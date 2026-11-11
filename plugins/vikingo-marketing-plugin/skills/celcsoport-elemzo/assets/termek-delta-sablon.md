# Termék mód — delta-sablon

Ezt illeszd be az ajánlat **saját** `00-agy/brand/ajanlatok/[ajanlat]/celcsoport.md` fájljába — onnan olvasnak az író-skillek. A `kontextus.md` Célcsoportok szekciója csak **hivatkozzon** rá, ne másolja: két példányból az egyik mindig elavul.

## Ha még nincs kitöltve az ajánlat `celcsoport.md`-je

Először hozd létre a fejlécet:

```markdown
## Célcsoportok

> Alap avatarok: lásd a `celcsoport.md`-t (ha van ilyen fájl a projektben)
> Itt csak az szerepel, ami **erre a termékre specifikus**. Az általános avatar-adatok (demográfia, pszichográfia, jelenlét, életmód) az alap profilokban vannak.
```

## Minden célcsoporthoz ezt a sablont töltsd

```markdown
### Célcsoport {{N}}: {{Rövid leíró név}}

**Alap avatar:** {{A cég-avatarok közül a legközelebb álló}}
**Termék-specifikus szerep:** {{1 mondat: mi az avatar motivációja erre a termékre}}

**Rövid leírás:** {{2-3 mondat a termék szemszögéből}}

#### Termék-specifikus célok
- {{Amit ezzel a termékkel akar elérni — NEM általános életcélok}}
- ...

#### Termék-specifikus problémák
- {{Ami ebben a témában akadályozza — NEM általános frusztrációk}}
- ...

#### Termék-specifikus vásárlási trigger
- {{Milyen pillanat / helyzet véteti meg vele ezt a terméket}}
- ...

#### Termék-specifikus kifogások
- „{{kifogás szó szerint}}": {{rövid kontextus, miért mondja}}
- ...

#### Deal-killers
- {{Amitől garantáltan NEM veszi meg}}
- ...
```

## Fontos szabályok

- Célcsoportok közé `---` elválasztó kerül.
- **Egy termékhez jellemzően 3-4 célcsoport** tartozik.
- A „Rövid leíró név" **a termék kontextusán belül** legyen értelmes (pl. „Kezdő felhasználó", „Kreatív szakember"), NEM az alap avatar neve.
- Ha az alap avatar még nincs kitöltve (❌ / 🟡), akkor is használható — a termék-specifikus delta **független** az alap avatartól.
- Az általános demográfia (kor, helyszín, bevétel) **NEM** kerül a deltába. Az az alap profilban van.

## Példa (illusztráció — cseréld a saját termékedre)

```markdown
### Célcsoport 1: Saját vállalkozást építő szakember

**Alap avatar:** [Szabadúszó avatar-típus]
**Termék-specifikus szerep:** Szolgáltatást akar saját vállalkozásként kínálni, de nincs még rendszere és portfolioja.

**Rövid leírás:** Otthonról dolgozó szakember, aki a szakmát megtanulta vagy önállóan elsajátította, és most ügyfeleket akar szerezni. A terméktől a teljes folyamatot (intake → terv → kivitelezés → átadás) tanulja.

#### Termék-specifikus célok
- Saját portfolio felépítése
- Szolgáltatás-csomag strukturálása
- Első 3 ügyfél megszerzése

#### Termék-specifikus problémák
- „Tudok szakmát, de nem tudom hogyan adjam el"
- „Nem tudom mennyi időbe telik egy projekt"
- „Félek az ügyféllel való kommunikációtól"

#### Termék-specifikus vásárlási trigger
- Munkahelyén feszültté vált, és szabadúszást fontolgat
- Barátja kérte hogy csináljon neki valamit, és rájött hogy nem tudja árazni

#### Termék-specifikus kifogások
- „Már tudom a technikát, minek tanuljak újat?": A termék nem technika — folyamat
- „Nem ismerek senkit aki kérné ezt": A termék része hogyan kerülj kapcsolatba

#### Deal-killers
- Ha a termék csak technikai
- Ha nincs ügyfél-kommunikációs rész
```

## Kapcsolódás

A delta-output a termék-specifikus marketing-skillekhez ad inputot:
- Sales-oldal-író: a termék-specifikus célok / problémák / kifogások a sales-szöveg alapja
- Email-szövegíró: a termék-specifikus vásárlási trigger az email-sorozat hook-ja
- Hirdetés-szövegíró: a termék-specifikus problémák a hirdetés-angle
