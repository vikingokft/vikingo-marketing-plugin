# Voice Profiling Framework

A szókincs, mondatszerkezet és retorikai eszközök mélyebb elemzéséhez. A Fázis 1-ben használd.

## Szókincs-kategóriák

A szókincs a hangnem legkézzelfoghatóbb összetevője. Minden szövegmintában keresd ezeket. A „Példa" oszlop csak illusztráció — a cég saját mintáiból gyűjtsd be a tényleges szavakat.

| Kategória | Mit keress | Példa (illusztráció) |
|---|---|---|
| **Erősítők** | Pozitív jelzők, felkiáltások | brutálisan, szuper, iszonyú, giga |
| **Köznyelvi fordulatok** | Laza, beszélt nyelvi kifejezések | király, na de, hagyjuk is |
| **Átmeneti kifejezések** | Összekötő szavak, mondatindítók | szóval, viszont, ráadásul, egyébként, amúgy |
| **Őszinteség-jelzők** | Vallomásos, bevallós kifejezések | bevallom, őszintén, nem szégyellem, rájöttem |
| **Biztonságérzet** | Megnyugtató, bátorító | ne aggódj, ez normális, nem kell megijedni |
| **Javaslattevés** | Ajánlás, útmutatás | én azt ajánlom, próbáld ki, érdemes figyelni |
| **Anti-szókincs** | Tiltott szavak, kerülendő | egyedülálló, kihagyhatatlan, garantált, kedves barátom |

## Mondatszerkezet és ritmus

A „Cég-átlag" oszlop a cég `00-agy/brand/markahang.md`-jéből mért referencia — ahol még nincs adat, mérd be a szövegmintákból.

| Szempont | Mit mérj | Cég-átlag (kitöltendő) |
|---|---|---|
| **Mondathossz** | Szavak száma mondatonként | Email: ~[X] szó; Edukáció: ~[X] szó |
| **Bekezdés-hossz** | Sorok száma bekezdésenként | Email: [X]% 1-soros; Edukáció: átlag [X] szó |
| **Ritmus** | Rövid-hosszú váltakozás | [pl. pattogós rövid + kifejtő közepes, soha nem egyhangú] |
| **Kiemelések** | Félkövér, dőlt, zárójelezés | [pl. max 3-5 félkövér; zárójelben személyes belső monológ] |

## Retorikai eszközök

A „Cég-példa" oszlopba a cég tényleges mintáiból emelj be idézetet.

| Eszköz | Leírás | Cég-példa (kitöltendő) |
|---|---|---|
| **Hook-Story-Pitch** | Nyitás → történet → ajánlat | [pl. email és videó alap-struktúrája] |
| **Személyes sztori** | Konkrét kor, helyszín, helyzet | [pl. „[életkor] voltam", „[helyszín]"] |
| **Ellentétpárok** | Kontraszt, fordulat | [pl. „[motiváció]" vs. „[eredmény]"] |
| **Relativizálás** | Az ajánlat gyengítése hitelességért | [pl. „Nem sürgős megvásárolni"] |
| **Paradox CTA** | Csökkenti a nyomást, emeli a motivációt | [a cég jellegzetes lezárása] |
| **Zárójelezés** | Lehalkított személyes megjegyzés | Mindig emberi hang, soha nem technikai |

## Elemzési módszertan (lépésről lépésre)

1. **Korpusz áttekintés** — hány szöveg, milyen típus, milyen időszak, hozzávetőleges szómennyiség
2. **Dimenzió pontozás** — 8 dimenzió 1-10, idézettel
3. **Szókincs gyűjtés** — kategóriánként, gyakorisággal, megjelölve ami a guide-ban nincs
4. **Minta felismerés** — ismétlődő nyitások, zárások, visszatérő témák, mondatindítások
5. **Anti-minta keresés** — AI-minták (redundancia, „Nem X, nem Y, hanem Z"), túl formális/céges fordulatok, inkonzisztenciák

## Output-jelzés

Ha nagy a szórás egy dimenzión belül (pl. 6 és 9 között), jelezd:
> „A közvetlenség 6-9 között mozog, az átlag 7, de van 2 nagyon erős kitörés ([X] és [Y] minta)."
