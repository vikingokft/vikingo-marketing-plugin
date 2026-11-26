# A referencia elemzése

Mindkét listán menj végig. Konkrétan írj: a „modern, prémium, letisztult” nem ad döntést. A szándékos hiányokat is jegyezd fel (például „nincs árnyék”, „nincs ikon”), mert ezek is a karakter részei.

## 1. Az alapok

| Terület | Mit nézz |
|---|---|
| Színek | Melyik a domináns felület, melyik a szöveg, melyik a kiemelés, és mennyi van belőlük. Világos és sötét szakaszok váltakozása. |
| Betűk | Talpas, talpatlan vagy display; súlyok, dőlt, betűköz, nagybetű. A H1, H2 és a törzs méretaránya. A címsorok sortörése és hossza. |
| Elrendezés | Tartalomszélesség, margók, oszloparányok, igazítás, mennyi az üres tér, szimmetria vagy tudatos aszimmetria. |
| Formák és mélység | Lekerekítés, szegély, árnyék vagy annak hiánya, és ezek következetessége. |
| Komponensek | Gombok (kitöltött, kontúros, állapotok), kártyák, űrlapmezők, navigáció, lábléc. |
| Vonalak | Rácsvonalak, keretek, elválasztók, aláhúzások: vastagság, szín, hol futnak végig, mi igazodik hozzájuk. |
| Logó | A referencia logójának jellege (szöveges vagy jeles, súly, nagybetű, betűköz): ebből lesz a szöveges logó, ha a vállalkozásnak nincs. |

## 2. A jellegzetességek

Ezek teszik az oldalt felismerhetővé. Mindegyiknél: van-e, milyen, hol, milyen gyakran.

| Elem | Példák arra, mi lehet |
|---|---|
| Címsorkezelés | Egy kulcsszó dőlttel, más betűvel vagy színnel; aláhúzás, ecsetcsík, kézírásos jel; óriás méret; vegyes súly. |
| Felső címkék | A cím fölötti kis szöveg: nagybetűs, monospace, keretben, számozva, ikonnal. |
| Háttér | Sima szín, papírtextúra, szemcse, rács, színátmenet, óriás betű vagy monogram a háttérben. |
| Dekor-réteg | Vonalak, formák, mintadarabok, matricák, kézi rajzok a tartalom körül. |
| Szekcióhatárok | Egyenes vágás, hullám, íves él, cakkos él, átlós vágás, futó szalagszöveg. |
| Képkezelés | Fotó vagy illusztráció; tónus, színkezelés (fekete-fehér, meleg, telített); kivágás (téglalap, ív, kör, kivágott alak); keret; átfedés a szöveggel. |
| Ikonok | Vannak-e egyáltalán; vonalas, tömör, kézi rajzos; vonalvastagság, méret, szín. |
| Illusztráció | Stílus (vonalas, festett, geometrikus), szín, hol szerepel. |
| Mozgás | Belépő animáció, hover, görgetésre kirajzolódó elem, futó szöveg. Csak ha ténylegesen látod. |
| Ritmus | Hogyan váltakoznak a levegős és sűrű, képes és szöveges, világos és sötét szakaszok. Mi az oldal emlékezetes megoldása. |

## 3. A szignó

Válaszd ki azt az egy-két formai elemet, ami nélkül az oldal nem lenne ugyanaz. Jó szignó az, ami:

- több elemen is visszatér (gomb, képkeret, szekcióhatár, címke),
- egyszerűen leírható, így az AI bármilyen új felületen újra tudja alkotni,
- a tárgyi világból tartalmat kaphat.

Egy példa: a Vikingo arculatában a cikcakk (rúnaél) ilyen. Ott van a szövegdoboz szélén, a portrékereten, a címkék végén és a háttérmintán.

## 4. Kerülendők (anti-slop)

Ezek az AI-designok felismerhető jelei. Csak akkor kerülhetnek a rendszerbe, ha a referenciában ténylegesen ott vannak:

- lila-kék színátmenet, színátmenetes szöveg, üveghatás,
- egyforma kártyák rácsban, mindegyikben egy ikon a cím fölött,
- Inter, Roboto vagy Arial címsorként,
- minden szakaszon ugyanaz a beúszó animáció, rugózó mozgás,
- dekoratív sorszámok (01, 02, 03) a tartalmi szakaszok mellett,
- generikus stockfotós hangulat, kép nélküli üres díszdobozok,
- emoji ikon helyett.

A címsorban egy szó kiemelése sokszor elcsépelt. Csak akkor használd, ha a referencia is így csinálja, vagy a tárgyi világból jön a formája (ilyen például a méretvonal a kertésznél).

## Kiolvasó szkript a böngészőhöz

A referenciaoldalon futtasd (a böngésző JavaScript-eszközével). A leggyakoribb betűket, színeket, lekerekítéseket és a címsorok stílusát adja vissza.

```js
(() => {
  const szamol = {}, tipus = (k, v) => { if (!v) return; szamol[k] = szamol[k] || {}; szamol[k][v] = (szamol[k][v] || 0) + 1; };
  const elemek = [...document.querySelectorAll('body *')].filter(e => e.offsetParent !== null).slice(0, 4000);
  for (const e of elemek) {
    const s = getComputedStyle(e);
    if (e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) {
      tipus('betu', s.fontFamily.split(',')[0].replace(/["']/g, '').trim());
      tipus('szovegszin', s.color);
    }
    if (s.backgroundColor !== 'rgba(0, 0, 0, 0)') tipus('hatter', s.backgroundColor);
    if (s.borderRadius !== '0px') tipus('lekerekites', s.borderRadius);
    if (s.boxShadow !== 'none') tipus('arnyek', s.boxShadow.slice(0, 60));
    if (s.backgroundImage !== 'none') tipus('hatterkep', s.backgroundImage.slice(0, 60));
  }
  const hex = v => v.replace(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/g, (m, r, g, b, a) =>
    '#' + [r, g, b].map(x => (+x).toString(16).padStart(2, '0')).join('') + (a !== undefined && +a < 1 ? ` (${Math.round(a * 100)}%)` : ''));
  const top = o => Object.entries(o || {}).sort((a, b) => b[1] - a[1]).slice(0, 8).map(([k, n]) => [hex(k), n]);
  const cimek = ['h1', 'h2', 'h3'].map(t => { const e = document.querySelector(t); if (!e) return null; const s = getComputedStyle(e);
    return { t, szoveg: e.textContent.trim().slice(0, 60), betu: s.fontFamily, meret: s.fontSize, suly: s.fontWeight, sor: s.lineHeight, koz: s.letterSpacing, stilus: s.fontStyle, nagybetu: s.textTransform }; });
  // gombok: a látható, nem „ugrás a tartalomra” linkek közül, amelyiknek háttere vagy kerete van
  const gombok = [...document.querySelectorAll('a, button')].filter(e => e.offsetParent !== null && !/skip|ugrás/i.test(e.textContent)
    && e.getBoundingClientRect().width > 60).filter(e => { const s = getComputedStyle(e); return s.backgroundColor !== 'rgba(0, 0, 0, 0)' || s.borderStyle !== 'none'; }).slice(0, 3);
  return { betuk: top(szamol.betu), szovegszinek: top(szamol.szovegszin), hatterek: top(szamol.hatter), lekerekitesek: top(szamol.lekerekites),
    arnyekok: top(szamol.arnyek), hatterkepek: top(szamol.hatterkep), cimek,
    gombok: gombok.map(g => { const gs = getComputedStyle(g); return { szoveg: g.textContent.trim().slice(0, 30), hatter: hex(gs.backgroundColor), szin: hex(gs.color),
      keret: hex(gs.border), lekerekites: gs.borderRadius, padding: gs.padding, betu: gs.fontFamily.split(',')[0], meret: gs.fontSize, nagybetu: gs.textTransform }; }) };
})()
```
