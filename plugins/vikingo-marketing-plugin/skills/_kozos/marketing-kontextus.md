# Marketing-kontextus

A marketing-skillek közös szerződése: honnan jön a kontextus, ki tölti fel, és mi történik, ha hiányzik. Ez váltja ki azt, hogy minden skill külön magyarázza el ugyanezt.

## Hol él a márka-agy

Minden skill ugyanabból a márka-agyból olvas: a `00-agy/brand/` mappából. **Minden `00-agy/…` útvonal a megnyitott mappa gyökeréhez képest értendő**, nem a skill mappájához képest. A plugin két helyzetben fut, és a mappa útvonala mindkettőben ugyanaz:

| Helyzet | Honnan ismered fel | Mit csinálsz |
|---|---|---|
| **AI-oprendszer munkaterület** | A gyökérben van `AGENTS.md` és `00-agy/` | A meglévő `00-agy/brand/`-ből dolgozol. A kész anyag a birtokló projektbe vagy területbe kerül (lásd lent: Hova kerül a kész anyag). |
| **Önálló marketing-mappa** | Nincs AI-oprendszer, de van `00-agy/brand/` (ezt egy korábbi futás hozta létre) | Ugyanígy a `00-agy/brand/`-ből dolgozol. A kész anyag a `kimenetek/` alá kerül (lásd lent: Hova kerül a kész anyag). |
| **Még nincs márka-agy** | Nincs `00-agy/brand/` | Az író-skill ne találgasson: mondd meg, hogy előbb a `brand-specialista` építse fel a márka-alapot (egy termékhez a `termek-specialista`), és kérdezd meg, indítsuk-e. Az építő-skill felajánlja, hogy létrehozza. |

**A márka-agyat csak az építő-skill hozza létre, és csak a felhasználó igenje után.** Előtte mondd meg, melyik mappában jön létre (a megnyitott mappa gyökerében), és ha a mappa láthatóan egy másik projekt (például egy weboldal forráskódja, ahol `package.json` vagy `wp-config.php` van), javasold, hogy inkább egy külön marketing-mappát nyisson meg erre. A létrehozott fájlok a lenti Betöltés-tábla szerkezetét követik, így ha a felhasználó később AI-oprendszert telepít, a márka-agya változtatás nélkül átvihető.

**Az AI-oprendszer mappái önálló módban.** Ha egy skill AI-oprendszer-mappát említ, önálló marketing-mappában ezt jelenti: a projekt vagy terület helyett a `kimenetek/` (a lenti kimeneti-hely szabály szerint); a `01-nyers/` helyett az, amit a felhasználó megad vagy beilleszt (ha van `01-nyers/` mappa, azt is megnézheted); a projekt `_attekintes.md`-je helyett nincs külön állapotfájl, a következő lépést a kísérő üzenetben mondd el.

Az elv: egy tény egy helyen él, és minden skill onnan olvassa.

## Hova kerül a kész anyag

Egy szabály minden író-skillre, hogy a két helyzetben ugyanaz a szerkezet legyen:

| Helyzet | Kimeneti hely |
|---|---|
| Önálló marketing-mappa | `kimenetek/<tipus>/<ajanlat>/` |
| AI-oprendszer | `03-projektek/<projekt>/<tipus>/<ajanlat>/`, vagy ha folyamatos munka, a birtokló terület (`02-allando-teruletek/<terulet>/<tipus>/<ajanlat>/`) |

- `<tipus>`: `email`, `hirdetes`, `video-script`, `sales-oldal`, `landing`, `webinar`, `social`, `kampany`, `automatizmus`, `ux`.
- `<ajanlat>`: az ajánlat mappájának neve a `00-agy/brand/ajanlatok/` alatt. Ha a munka nem egy ajánlathoz tartozik (például egy cég-szintű social-terv), egy rövid, ékezet nélküli slug.
- A fájlnevet a skill adja meg a saját Mentés sorában. Ha már van ilyen nevű fájl, ne írd felül: a régit nevezd át `<nev>-elozo-ÉÉÉÉ-HH-NN.md`-re.
- **AI-oprendszerben, ha nincs birtokló projekt vagy terület:** egy mondatban javasold a munkaterület `uj-projekt` skilljét (slug és cél), és igen után hozd létre. A gyökérbe ne írj, mert ott a munkaterület rendje szerint semmi nem él tartósan.
- Ha a projektnek van `_attekintes.md`-je, a kész anyagot vedd fel az eredménytermékei közé.

## Két család

| Család | Mit csinál | Skillek |
|---|---|---|
| **Építő** | Nyers anyagból kanonikus agyfájlt ír. Kérdez, kutat, elemez. | `brand-specialista`, `markahang-elemzo`, `celcsoport-elemzo`, `versenytars-elemzo`, `testimonial-elemzo`, `termek-specialista` (termék és csali módban), `ajanlat-workshop` |
| **Író** | A kész agyból dolgozik, és eredményterméket termel. Nem kérdez ki, nem elemez. | `email-iro`, `hirdetes-szovegiro`, `hirdetes-video-script-iro`, `sales-oldal-iro`, `webinar-script-iro`, `social-tartalom-tervezo`, `kampany-tervezo`, `automatizmus-tervezo`, `ux-tervezo`, `landing-szovegiro`, `landing-design`, `landing-epito`, `landing-elesites` |
| **Eszköz, utómunka** | Kész szövegen vagy a felhasználó saját anyagán dolgozik. Az agyból legfeljebb a márkahangot olvassa. | `szoveg-emberiesito`, `feladat-iro` |

Az író-skillek **nem építenek kontextust**. Ha egy író-skill azon kapja magát, hogy interjút készít a termékről vagy a célcsoportról, rossz családban dolgozik: adja át az építőnek, vagy pótolja a hiányt a lenti protokoll szerint.

## Betöltés

Minden marketing-skill ugyanabból a szerkezetből olvas. A cég-szintű fájlok az alapok, az ajánlat-mappa felülírja őket.

| Amire szükség van | Kanonikus otthon |
|---|---|
| Írás-szabályok, tiltott minták, felület-szabályok | `00-agy/brand/markahang.md` |
| Mit ad el a cég, kinek, mi a pozicionálás | `00-agy/brand/uzleti-profil.md` |
| Cég-szintű célközönség | `00-agy/brand/celcsoport.md` |
| Versenytársak, differenciátorok | `00-agy/brand/versenytarsak.md` |
| Történetek, alapító-sztori, ügyfél-sztorik | `00-agy/brand/sztoribank.md` |
| Cég-szintű hirdetési változók (egységes garancia, ügyfélszám, díj) | `00-agy/brand/kontextus-elemek.md` |
| Színek, logó, tipográfia | `00-agy/brand/arculat.md` |
| Ki ír, kinek más a hangja | `00-agy/brand/csapat.md` |
| A termékek listája és állapota | `00-agy/brand/ajanlatok/_attekintes.md` |
| Egy termék teljes kontextusa | `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md` |
| Termék-specifikus hirdetési változók (ár, garancia, terméknév, CTA) | `.../kontextus-elemek.md` |
| A termék célcsoportja, avatarok | `.../celcsoport.md` |
| Hookok, üzenetmagok, fájdalmak | `.../uzenetek.md` |
| Kifogások és cáfolatuk | `.../kifogasok.md` |
| Vevői idézetek, számok | `.../testimonialok.md` |
| Amiben a termék gyenge | `.../gyengesegek.md` |
| A termék versenytársai | `.../versenytarsak.md` |

**Öröklés és sorrend.** Három fájlnak van cég-szintű és termék-szintű párja is:
`celcsoport.md`, `kontextus-elemek.md`, `versenytarsak.md`. A Bemenet-táblákban ezek így
szerepelnek:

`00-agy/brand/celcsoport.md` → `.../celcsoport.md`

A nyíl a betöltés sorrendje. **Előbb a bal oldalit olvasd, az az alap.** Aztán a jobb
oldalit, és ahol ott kitöltött érték van, az felülírja a cég-szintűt, mezőnként. A
`KITÖLTENDŐ` nem felülírás, hanem hiány: ilyenkor a cég-szintű érték marad érvényben.

Ebből következik, hogy egy üres termék-szintű fájl nem hiány, ha a cég-szintű ki van
töltve. Ne kérdezz rá olyasmire, amit a cég-szinten megtalálsz.

**Csalinál három szint van:** cég → szülő-termék → csali. A szülő-termék az a fizetős
ajánlat, ahova a csali vezet; a csali `kontextus.md`-jének Pozicionálás szakaszában a
**Szülő-termék** sor nevezi meg. Csali-ajánlatnál tehát a szülő-termék `kontextus-elemek.md`-je
a középső szint, és a csali saját értéke nyer.

**Üres és nem használt mező.** Egy jel van a hiányra: `KITÖLTENDŐ`. Ami tudatosan nem
használt (például nincs kuponkód), oda `nincs` kerül. A `nincs` kitöltött érték, tehát
felülírja a cég-szintet; a `KITÖLTENDŐ` nem. Más jelet (`—`, „nincs kitöltve”, üres sor) ne
használj, mert az öröklés és a hiány-protokoll csak ezt a kettőt ismeri.

**Csak azt töltsd be, amit a feladat kér.** Egy tárgysor-variánshoz nem kell a versenytárs-elemzés. A skill `## Bemenet` táblája mondja meg, mi kötelező.

## A web-kutatás futtatókörnyezet-függő

Néhány építő-skill (`versenytars-elemzo`, `celcsoport-elemzo`) tartalék-útvonalként web-kutatást
kínál, ha nincs first-party adat. **Ez nem mindig elérhető:** a szállított Codex-konfiguráció a
sandboxban kikapcsolja a hálózatot (`network_access = false`), ami szándékos biztonsági
alapértelmezés.

Ezért:

- **Ne feltételezd a web-hozzáférést.** Ha a lekérés nem fut, az nem hiba, hanem a
  futtatókörnyezet határa.
- Ilyenkor a **beillesztés-útvonal az elsődleges:** kérd el a felhasználótól az oldal-szöveget,
  a posztot vagy a hirdetés-szöveget, és abból dolgozz.
- **Mondd ki egy sorban, hogy web-kutatás nélkül dolgozol**, és mi lett ezért gyengébb. Csendben
  vékonyabb kimenetet adni tilos. Ez ugyanaz a szabály, mint a hiány-protokoll 8. pontja
  („Kitalálni tilos").

## Hiány-protokoll

A `KITÖLTENDŐ` mező és a hiányzó fájl ugyanaz: nincs adat.

1. **Előbb nézd meg.** Kérdezés előtt olvasd el a kanonikus fájlt. Amit ott megtalálsz, arra soha ne kérdezz rá.
2. **Egy üzenet, nem interjú.** Ha kötelező elem hiányzik, egyetlen üzenetben kérdezd meg az összeset, legfeljebb ötöt. Mondd meg, melyik fájlba fog kerülni.
3. **Ne a fájl kitöltöttségét nézd, hanem hogy ehhez a feladathoz mi kell.** Egy sablonból másolt ajánlat-mappában mind a negyvenkét mező üres, de egy tárgysorhoz ebből kettő kell. Azt a kettőt kérdezd meg, a többi ehhez a feladathoz irreleváns. **Ha ehhez a konkrét feladathoz ötnél több hiányzó mező kellene, az már nem hiány, hanem meg nem épített fájl:** ilyenkor ne kérdezz mezőnként, hanem a 5. pont szerint járj el.
4. **A válasz a kanonikus fájlba megy.** Amit az alapító megad, azt írd be a helyére (elvégzed, és a kör végén összefoglalod), és csak utána dolgozz vele. Így a kérdés a munkaterület életében egyszer hangzik el.
5. **Ha az adat nem egy mező, hanem egy hiányzó elemzés** (nincs avatar, nincs mért márkahang, nincs termék-kontextus), ne pótold interjúval: nevezd meg az építő-skillt, és kérdezd meg, futtassuk-e előbb.
6. **Az ajánlott és opcionális hiányokra ne kérdezz.** Dolgozz nélkülük, és a 7. pont szerint jelezd, mi hiányzott.
7. **Az ütközés nem hiány.** Ha két forrás mást mond ugyanarról (két oldal ugyanarról a
   weboldalról, egy export és egy árlista), **ne válassz csendben**, ne átlagolj, és ne a
   később olvasottat vedd érvényesnek. Nevezd meg mind a két értéket a forrásával, és kérdezz.
   Amíg nincs döntés, `[ütköző forrás, megerősítendő]`, és **ilyen adat nem mehet ki
   tényként** vevő felé menő szövegben.
8. **Kitalálni tilos.** Árat, garanciát, ügyfélszámot, idézetet, dátumot valós forrás nélkül soha ne írj tényként. Ha kell a helye, jelöld `[becsült, megerősítendő]`-nek.

## Hova kerül a hiány-jelzés

Úgy csináld, ahogy egy szövegíró csinálja, amikor átad egy anyagot.

**A szállítandó fájl tiszta marad.** Nem teszünk bele belső fájlútvonalakat és hiány-listát:
azt a fájlt továbbküldik a grafikusnak vagy bemásolják a hirdetéskezelőbe.

**A hiány-jelzés a kísérő üzenetbe megy**, a kimenet után:

```md
Kész. Két kötelező adat nélkül írtam meg:

- **Ár** — a `00-agy/brand/ajanlatok/nyari-muhely/kontextus-elemek.md`-ben `KITÖLTENDŐ`.
- **Garancia** — ugyanott.

Mondd meg őket, és beírom a fájlba. Ha inkább az egész termék-kontextust rendeznénk,
futtassuk a `termek-specialista`-t.
```

**Kivétel: ami egy konkrét helyet érint, azt a helyén jelöld.** Ha a szövegben szerepelnie
kellene egy árnak, de nincs, oda `[ár, megerősítendő]` kerül, nem kitalált szám. Ez a jelölés
benne marad a fájlban, mert pont az a dolga, hogy szemet szúrjon.

**Ami túléli a beszélgetést, az az áttekintőbe megy.** Ha a hiány a projekt továbbvitelét
érinti, vedd fel a projekt `_attekintes.md`-jébe következő lépésként. A kísérő üzenet elveszik
a következő munkamenetben, az áttekintő nem.

## Kiadás előtti önellenőrzés

Minden marketing-skill futtassa le ezt a hat pontot a **saját outputján**, mielőtt átadja. A mérce a `00-agy/brand/markahang.md` II. Mit ne fejezete; ami ott `KITÖLTENDŐ`, arra az alábbi alapértelmezés áll.

1. **Mondat-közi gondolatjel: nincs.** Ne szemre ellenőrizd: keress rá a `—` és a `–` karakterre a kész szövegben, és minden találatnál döntsd el, lista- vagy cím-elválasztó-e (rendben), vagy mondat-közi (cseréld vesszőre, kettőspontra, zárójelre, vagy bontsd két mondatra).
2. **„Nem X, hanem Y" szerkezet:** a `markahang.md` II. fejezetének „»Nem X, hanem Y« korlát” mezője szerint. Ha az `KITÖLTENDŐ`: a konkrét, valódi szembeállítás rendben van („nem a tiéd a hiba, hanem a beállításé” egy szerelőnél, ahol tényleg ez a helyzet). Az elvont reflex nem: amikor a tagadott fél szalmabáb, és a mondat a „hanem” utáni részből is megállna („Nem több funkció kell, hanem rendszer.”). Ilyenkor kezdd a lényeggel. Ugyanígy mérd a kétmondatos (`Nem azért X. Hanem Y.`) és a rejtett változatot (`Nem a … -vel van baj`, `Nem X, csak Y`). Ugyanezt a mércét használja a `szoveg-emberiesito` scannere.
3. **Üres szuperlatívusz, buzzword, AI-klisé: nincs.** Például „a mai rohanó világban", „ne feledd", „forradalmi", „felbecsülhetetlen", „emeld új szintre".
4. **Kitöltetlen helyőrző: nincs.** A `[...]`, „X Ft", `[Cég neve]` alakok nem mehetnek ki. Ha egy adat hiányzik, jelöld („a kontextus nem adja meg") vagy kérdezd meg. Kivétel a szándékosan jelölt `[KITÖLTENDŐ]`.
5. **Kitalált adat: nincs.** Ár, garancia, ügyfélszám, vevői idézet, dátum, külső állítás valós forrás nélkül nem mehet ki tényként. Ha kell a helye, `[becsült, megerősítendő]`. **Ütköző adat sem mehet ki:** ha a kontextusban `[ütköző forrás, megerősítendő]` áll, azt az értéket ne írd tényként a vevő felé menő szövegbe. A lágy fabrikáció is ide tartozik: „kockázatmentes", „bárki csinálhatja", „nincs kötelezettség" csak megerősítés után.
6. **Csonka output: nincs.** Nincs „…stb.", „a többi hasonlóan", „és így tovább" rövidítés. Ami a feladat része, az ki van dolgozva.

Ha bármelyik bukik, írd át, mielőtt átadod. A skillek ezen felül a rájuk jellemző pontokat is ellenőrzik.

## Ne

- Ne hozz létre párhuzamos kontextusfájlt a projektben vagy a laboratóriumban. A termék igazsága az ajánlat-mappájában él.
- Ne másold be az agy tartalmát a skill fájljába. Hivatkozz rá.
- Ne kérdezz olyat, amit a kanonikus fájl megválaszol.
- Ne tarts állapot-táblát (termék-regiszter, csali-regiszter, avatar-állapot) a `SKILL.md`-ben. Az `_attekintes.md` fájlok hordozzák.
- Ne írj eredményterméket az agyba. A kész e-mail, hirdetés, sales-oldal a projektbe vagy a területre megy; az agy az igazság, nem a termék.

## Ellenőrzés

- A skill minden betöltött adata kanonikus fájlból vagy az alapító ebben a körben adott válaszából jön.
- Amit az alapító pótolt, az bekerült a kanonikus fájlba, és szerepel a kör végi összefoglalóban.
- A kimenet a projekt vagy a terület mappájában van, nem az agyban.
- Nincs kitalált szám, ár vagy idézet.
