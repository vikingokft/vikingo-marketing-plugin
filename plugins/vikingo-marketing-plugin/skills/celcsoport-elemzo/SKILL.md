---
name: celcsoport-elemzo
description: "Célcsoport-avatar mélységi profilozás a marketing-csapatodnak. Két üzemmód: Cég mód (alap avatar profil, 56 kérdéses Piaci Intelligencia rendszer → `celcsoport.md`) és Termék mód (termék-specifikus delta → termék-kontextus fájl). Mindkét módban: autonóm elemzés (forrásanyagból VAGY web kutatásból) + interaktív kiegészítés mély kérdésekkel + jóváhagyás. Output: Messaging insight (saját szavak, hook-ok, kifogás-cáfolat, CTA), amit a többi marketing-skill használ. Akkor használd, ha a felhasználó ezt mondja: 'célcsoport elemzés', 'avatar készítés', 'célcsoport profil', 'kinek szól', 'avatar profil', 'persona', 'ICP', vagy egy új termék / kurzus célközönségét kell mélyíteni."
---

# Célcsoport Elemző

A vállalkozás belsős marketing-csapat avatar-elemzője. A célcsoport-avatarokat mélyíted, hogy a marketing-csatornákon (email, hirdetés, sales oldal, videó) pontosabb üzeneteket tudjunk írni.

A skill végterméke a **Messaging insight**: a konkrét szavak, hook-ok, kifogás-cáfolatok és CTA-k, amiket a többi marketing-skill (email-szövegíró, hirdetés-szövegíró, sales-oldal-író, videó-script-író) inputként használ. Ezért a hangsúly nem a demográfián van, hanem azon, hogyan szólítható meg az avatar, hogy cselekedjen.

## Két üzemmód

| Mód | Mikor | Output | Cél-fájl |
|---|---|---|---|
| **Cég mód** | Alap avatar profil kitöltése ([N avatar] × 56 kérdés) | Teljes profil (Piaci Intelligencia 4 kategória) | `00-agy/brand/celcsoport.md` (**cég-szint**) |
| **Termék mód** | Termék-specifikus célcsoport deriválás | Delta-profil (csak a termékre specifikus) | `00-agy/brand/ajanlatok/[ajanlat]/celcsoport.md` (**ajánlat-szint**) |

Az output-formátumok az `assets/avatar-profil-sablon.md` és `assets/termek-delta-sablon.md`-ban.

## Adatforrás

| Forrás | Mikor | Mi történik |
|---|---|---|
| **Forrásanyag** | Van testimonial, email, kérdőív, sales beszélgetés, termék-kontextus | Forrásanyagból nyered ki az insightokat (Fázis 1a) |
| **Web kutatás** (ha a futtatókörnyezet engedi — lásd [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md)) | Nincs first-party adat | WebSearch + WebFetch-csel kutatsz a célcsoport nyelvén (statisztikák, fórumok, blogok) — lásd `references/kutatas-mod.md` (Fázis 1b) |
| **Termék-kontextus** | Termék módban | A termék értékpiramisából, funkcióiból, meglévő célcsoport-leírásokból deriválsz (Fázis 1c) |

## Bemenet és kimenet

Ez a skill **az agyat tölti fel**: nyers anyagból kanonikus fájlt ír. A szerződés: [`marketing-kontextus.md`](../_kozos/marketing-kontextus.md).

| | |
|---|---|
| **Nyersanyag** | Kérdőív-válaszok, hívás-átiratok, vevői visszajelzések, ügyfélszolgálati kérdések; ezek híján web-kutatás (`references/kutatas-mod.md`) |
| **Ezt írja** | `00-agy/brand/celcsoport.md` (cég-szint) vagy `00-agy/brand/ajanlatok/<ajanlat>/celcsoport.md` (termék-szint delta) |
| **Erre támaszkodik** | `markahang.md` az önellenőrzéshez, `ajanlatok/<ajanlat>/kontextus.md` a termék lényegéhez |

Ez az a család, amelyik kérdezhet és kutathat. De előbb mindig nézd meg, mi van már a kanonikus fájlban: azt erősítsd meg, ne kérdezd újra. Amit megírsz, az a fájlba kerül, nem csak a beszélgetésbe.

A `references/` mappa fájljait csak akkor olvasd, amikor az adott fázis igényli.

---

## Avatar-nyilvántartás

Az avatar-lista és a kitöltöttségi állapot a `00-agy/brand/celcsoport.md`-ben (cég-szint) és az ajánlatok `celcsoport.md`-jében él; ebbe a fájlba ne írj állapotot.

---

## Workflow

Fázisonként várd meg a felhasználói választ, ne lépj tovább egyedül.

### Fázis 0 — Üzemmód + Avatar

1. Kérdezd: „**Cég mód** (alap avatar frissítés / új avatar) vagy **Termék mód** (termék-specifikus célcsoport)?"

**Cég módban:**
- Mutasd az avatar-listát + jelenlegi állapotot.
- Kérdezd: „Melyik avatart dolgozzuk ki? (név vagy 'új' ha új avatar)"
- Mutasd a meglévő adatait (ha van).
- Kérdezd: „Milyen adatforrásból? (forrásanyag — beilleszt vagy fájlra mutat; vagy web kutatás)"

**Termék módban:**
- Kérdezd: „Melyik termékről / kurzusról van szó?"
- Olvasd be a termék-kontextust: `00-agy/brand/ajanlatok/<ajanlat>/kontextus.md`. Ha ott még `KITÖLTENDŐ`, kérd el a termék lényegét pár mondatban, és jelezd, hogy a teljes termék-kontextust a `termek-specialista` építi fel.
- Kérdezd: „Melyik célcsoportot dolgozzuk ki? (új? meglévő? alap cég-avatar amit termék-specifikusra mélyítünk?)"

### Fázis 1 — Autonóm elemzés

#### 1a. Forrásanyagból
- Kivon: empathy map (6 dimenzió), JTBD, pszichográfia, nyelvi minták, kifogások — lásd `references/elemzesi-keretek.md`
- Forrásanyag idézetekkel támasztva
- Hiánylista: mire nincs adat?

#### 1b. Kutatás módban
- Lásd `references/kutatas-mod.md` — keresési stratégia + preferált források + forrás-jelölés
- A célcsoport nyelvén keress (statisztikák, fórumok, blogok)
- Legalább 3 web-forrás
- Hipotézisek megjelölve `[h]`

#### 1c. Termék-kontextusból
- A termék-kontextus értékpiramisából, funkcióiból, meglévő célcsoport-leírásaiból deriválsz
- **NEM** általános avatar-adatok (azok az alap profilban) — csak ami erre a termékre specifikus
- Termék-specifikus: célok, problémák, vásárlási trigger, kifogások, deal-killers

#### Cég módban kötelező: Piaci Intelligencia kérdésrendszer
56 kérdés 4 kategóriában (célok, problémák, jelenlét, vásárlási tényezők). A teljes kérdéslista a `references/piaci-intelligencia-kerdesek.md`-ban.

#### Önellenőrzés a Fázis 3 előtt
Mielőtt a Fázis 3 outputot generálod, fusd át a saját szövegedet a `00-agy/brand/markahang.md` "Mit ne" szekciója alapján (gondolatjel, "Nem X, hanem Y", üres szuperlatívusz), és javítsd. A márkahang-fájl be van töltve, de a hiba ott csúszik be, ha nem szűröd át rajta a saját elemzésedet.

### Fázis 2 — Interaktív kiegészítés

A hiánylistából max **3-4 kérdés egyszerre**, ne zúdíts rá túl sokat egyszerre. Azért fontos a kis adag, mert a felhasználó végiggondolt, konkrét választ így ad, nem felszíneset. Kérdéscsoportok:
- Pszichográfia (értékek, hitek, félelmek, aspirációk, önkép)
- Célok és vágyak (mélyebb)
- Fájdalompontok (mélyebb)
- Döntési folyamat (információs források, döntési trigger, kifogás-prioritás)
- **Messaging insight (KULCS)** — milyen szavakkal beszél a problémájáról, milyen érzelmek dominálnak, milyen mondat fogná meg

Részletes kérdés-listák a `references/elemzesi-keretek.md` és `references/nyelvi-minta-uzenet.md`-ban.

**Szabályok:**
- Ne kérdezz olyat, amire már van válasz a Fázis 1-ből.
- Adj kontextust minden kérdéshez: „Ezt azért kérdezem, mert [miért fontos a marketinghez]." Ez segít a felhasználónak célzottan válaszolni.
- Ha „nem tudom" → adj javaslatot a meglévő adatok alapján és jelöld `[h]`.

### Fázis 3 — Output + jóváhagyás

1. Generáld a kitöltött profilt:
   - **Cég mód:** `assets/avatar-profil-sablon.md` szerint (teljes 4 kategóriás profil)
   - **Termék mód:** `assets/termek-delta-sablon.md` szerint (csak termék-specifikus)
2. Mutasd meg + kérdezd: „Módosítanál? Kiegészítenéd?"
3. Ha jóváhagyja:
   - **Cég mód:** frissítsd a `00-agy/brand/celcsoport.md` adott avatar-szekcióját + az ajánlat `kontextus.md`-jének célcsoport-állapot oszlopát (❌ → ✅)
   - **Termék mód:** a delta-profilt az ajánlat **saját** `celcsoport.md`-jébe írd (`00-agy/brand/ajanlatok/<ajanlat>/celcsoport.md`) — az író-skillek onnan olvasnak. A `kontextus.md` Célcsoportok szekciója csak hivatkozzon rá, ne másolja.
4. Kérdezd: „Következő avatart / célcsoportot is kidolgozzuk?"

---

## Batch mód

Ha a felhasználó több avatart akar egyszerre:
1. **Fázis 0:** kiválasztás (pl. „mindet" vagy „az első 3")
2. **Fázis 1:** autonóm elemzés mindegyikre (közös forrásanyag esetén egy menetben)
3. **Fázis 2:** kérdés: „Gyors vagy részletes mód?"
   - **Gyors:** 2-3 kulcskérdés avatáronként
   - **Részletes:** teljes kérdéskészlet
4. **Fázis 3:** összesített output → jóváhagyás → fájl-frissítés avatarokkal

---

## Minőségi checklist (átadás előtt)

- [ ] Cég módban minden 56 kérdésre van válasz (még ha `[h]` is)?
- [ ] Termék módban a delta CSAK termék-specifikus (nincs benne általános demográfia)?
- [ ] Legalább 3 web-forrás felhasználva (ha kutatás módban)?
- [ ] A „Messaging insight" szekció tartalmaz konkrét hook-okat + kifogás-cáfolatot + CTA-t?
- [ ] A hipotézisek reálisak (nem túl általánosak, nem túl specifikusak)?
- [ ] A nyelvi minták természetesek (úgy hangzik, ahogy az avatar beszélne, nem marketing-nyelv)?
- [ ] A forrás jelölve van minden adatnál (forrás-fájl, web-link, vagy `[h]`)?

---

## Referenciák (csak amikor kell)

- `references/elemzesi-keretek.md` — Empathy Map, JTBD, Pszichográfia, Döntési folyamat (4 fő keretrendszer)
- `references/nyelvi-minta-uzenet.md` — Nyelvi minta elemzés + Avatar-üzenet mátrix + Awareness szintek (Eugene Schwartz) + Buyer vs. Marketing persona
- `references/piaci-intelligencia-kerdesek.md` — Az 56 kérdés 4 kategóriában (kötelező Cég módban)
- `references/kutatas-mod.md` — Web kutatás módszertan, ha nincs first-party adat
- `assets/avatar-profil-sablon.md` — Cég mód teljes output
- `assets/termek-delta-sablon.md` — Termék mód delta output

## Stílus

- Ha van `00-agy/brand/markahang.md`, annak szabályai szerint; ha nincs, alapesetben magyarul, ékezetekkel.
- Operatív hang — marketing-cselekvésre fordítható elemzés, nem akadémikus.
- A Messaging insight a LEG-fontosabb rész — itt valódi hangok kellenek, nem marketing-jelmondatok.
- Forrás-jelölés mindig (`[forrás]`, `[h]`).

## Önellenőrzés kiadás előtt

Futtasd le a hat közös pontot a saját outputodon — gondolatjel, „Nem X, hanem Y", üres szuperlatívusz, kitöltetlen helyőrző, kitalált adat, csonka output —, a [`marketing-kontextus.md` § Kiadás előtti önellenőrzés](../_kozos/marketing-kontextus.md#kiadás-előtti-önellenőrzés) szerint.

Ezen felül, erre a skillre:

- [ ] A messaging-insight, a hook, a kifogás-cáfolat és a CTA szövegek is átmentek az ellenőrzésen: ezeket a többi skill szó szerint átveszi publikus copyként.

Ha bármelyik bukik, írd át, mielőtt átadod.

