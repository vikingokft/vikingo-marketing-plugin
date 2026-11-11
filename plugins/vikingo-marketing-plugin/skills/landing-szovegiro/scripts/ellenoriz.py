#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ellenoriz.py - a landing-szovegiro kimenetének gyors ellenőrzése.

  python3 ellenoriz.py <LANDING>/szoveg.md

(<LANDING> a landing kimeneti mappája, lásd a SKILL.md Mentés sorát.)

A fájl eleji fejléc `recept:` sorából (például „L8 · Webinár · hosszú”) kikeresi a receptet a skill
references/receptek.md fájljából, és megnézi, hogy a recept blokkjai megvannak-e a helyes sorrendben.
A kiegészítéssel hozzáadott blokkot nem hibának, hanem „plusz blokknak” jelzi. Kiírja a kimaradt blokkokat,
a [KITÖLTENDŐ] helyeket és a tipográfiai hibákat (mondat közbeni gondolatjel, egyenes vagy angol idézőjel).
"""
import os
import re
import sys

RECEPTEK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'receptek.md')
# a receptekben rövidítve álló blokkok teljes neve (a blokklista.md szerint)
ALNEV = {'CTA': 'CTA szakasz', 'CTA + űrlap': 'CTA szakasz', 'CTA + jelentkezés': 'CTA szakasz',
         'Problémák': 'Problémák és következményeik', 'Termékjellemzők': 'Termékjellemzők, funkciók'}


def blokknev(nyers):
    """„Árak ✱ (értékösszesítő)” -> („Árak”, True)"""
    elhagyhato = '✱' in nyers
    nev = re.sub(r'\([^)]*\)', '', nyers).replace('✱', '').strip()
    return ALNEV.get(nev, nev), elhagyhato


def receptek():
    """{'L8': [(blokknév, elhagyható), …]} a receptek.md `**Lnn · …:** A → B → …` soraiból."""
    out = {}
    for sor in open(RECEPTEK, encoding='utf-8'):
        m = re.match(r'^-?\s*\*\*(L\d+) · [^*]*:\*\*\s*(.+?)\s*$', sor)
        if m and '→' in m.group(2):
            out[m.group(1)] = [blokknev(x) for x in m.group(2).split('→')]
    return out


def recept_blokkok(md):
    m = re.search(r'^recept:\s*(L\d+)\b', md, flags=re.M)
    if not m:
        return None, None
    return m.group(1), receptek().get(m.group(1))


# A márka-agy belső jelölései: a márka-agynak szólnak, az oldalra nem kerülhetnek (szabalyok.md 7.)
BELSO_JELOLES = re.compile(
    r'\[\[\s*HIÁNYZIK[^\]]*\]\]'
    r'|\((?:következtetés|saját állítás|piaci hang|kockázatos állítás|kizárva|elmesélt|belső'
    r'|kitalált|megerősítendő|feltételezés)\b[^)]*\)'
    r'|\[(?:becsült|ütköző forrás)\b[^\]]*\]',
    flags=re.I)


def main(path):
    md = open(path, encoding='utf-8').read()
    if md.startswith('---'):
        if '\n---' not in md[3:]:
            print('HIBA: a fájl eleji fejléc (---) nincs lezárva egy második --- sorral.')
            return 1
        test = md[3:].split('\n---', 1)[1]
    else:
        test = md
    fejek = re.findall(r'^##\s+(\d+)\.\s+(.+?)\s*$', test, flags=re.M)
    hibak, kimaradt, kitoltendo = [], [], []
    nevek = [re.sub(r'\s*✱\s*$', '', n) for _, n in fejek]
    kod, vart = recept_blokkok(md)
    plusz = []
    if not kod:
        hibak.append('A fejlécben nincs `recept:` sor (például „recept: L8 · Webinár · hosszú”).')
    elif not vart:
        hibak.append(f'A(z) {kod} recept nincs a references/receptek.md-ben.')
    else:
        # a recept blokkjai sorrendben, közöttük lehet kiegészítéssel hozzáadott (plusz) blokk
        j = 0
        for i, nev in enumerate(nevek, 1):
            if j < len(vart) and nev == vart[j][0]:
                j += 1
            else:
                plusz.append(f'{i}. {nev}')
        if j < len(vart):
            hibak.append(f'A(z) {kod} recept blokkjai nincsenek meg sorrendben: a(z) {j + 1}. blokk („{vart[j][0]}”) hiányzik vagy rossz helyen áll.')
            hibak.append('  A recept sora: ' + ' → '.join(n + (' ✱' if e else '') for n, e in vart))
    reszek = re.split(r'^##\s+\d+\.\s+.+$', test, flags=re.M)[1:]
    for (n, nev), resz in zip(fejek, reszek):
        szoveg = resz.strip()
        if szoveg.startswith('Kimarad:'):
            kimaradt.append(f'{n}. {nev}: {szoveg.splitlines()[0]}')
        for m in re.findall(r'\[KITÖLTENDŐ[^\]]*\]', szoveg):
            kitoltendo.append(f'{n}. {nev}: {m}')
        # a számtartomány nagykötőjele (60–90) helyes, csak a mondat közbeni gondolatjel hiba
        mondatkozi = re.sub(r'(?<=\d)–(?=\d)', '', szoveg)
        for jel, mi, hol in (('—', 'hosszú gondolatjel', szoveg), ('–', 'gondolatjel', mondatkozi),
                             ('"', 'egyenes idézőjel („…” kell; idézeten belül »…«, véleményben is, a szavakhoz nem nyúlva)', szoveg), ('“', 'angol idézőjel („…” kell; idézeten belül »…«)', szoveg)):
            if jel in hol:
                hibak.append(f'{n}. {nev}: {mi} a szövegben.')
        for m in BELSO_JELOLES.finditer(szoveg):
            hibak.append(f'{n}. {nev}: belső jelölés maradt a szövegben: „{m.group(0)}” (ez a márka-agynak szól, töröld vagy írd át).')
    figyelj, cimsorok = [], []
    for (n, nev), resz in zip(fejek, reszek):
        fv = re.search(r'^\*\*Felvezető:\*\*\s*(.+?)\s*$', resz, flags=re.M)
        for cs in re.findall(r'^###\s+(.+?)\s*$', resz, flags=re.M):
            db = len(re.findall(r'\w+', cs))
            cimsorok.append((n, nev, cs, db, fv.group(1) if fv else ''))
            if fv and fv.group(1).strip(' .') == cs.strip(' .'):
                figyelj.append(f'{n}. {nev}: a felvezető ugyanaz, mint a címsor.')
            if '!' in cs:
                figyelj.append(f'{n}. {nev}: felkiáltójel a címsorban.')
            fv = None
    elsok = [c[2].split()[0].lower() for c in cimsorok if c[1] != 'GYIK' and c[2].split()]
    for i in range(len(elsok) - 2):
        if elsok[i] == elsok[i + 1] == elsok[i + 2]:
            figyelj.append(f'Három címsor egymás után „{elsok[i]}” szóval kezdődik.')
    felv = sum(1 for c in cimsorok if c[4])
    szavak = len(re.findall(r'\w+', '\n'.join(reszek)))
    print(f'Recept: {kod or "?"} · blokkok: {len(fejek)} · szavak: {szavak} · címsorok: {len(cimsorok)}, ebből felvezetővel: {felv}')
    if plusz and not hibak:
        print('\nPlusz blokk a recepthez képest (kiegészítés? nézd át):')
        for x in plusz:
            print('  - ' + x)
    if cimsorok:
        print('\nCímsorok (szószám):')
        for n, nev, cs, db, f in cimsorok:
            if nev != 'GYIK':
                print(f'  {n}. {f + " · " if f else ""}{cs} ({db})')
    if figyelj:
        print('\nFIGYELJ (nem hiba, nézd át):')
        for x in figyelj:
            print('  - ' + x)
    for cim, lista in (('Kimaradt blokk', kimaradt), ('[KITÖLTENDŐ]', kitoltendo)):
        if lista:
            print(f'\n{cim} ({len(lista)}):')
            for x in lista:
                print('  - ' + x)
    if hibak:
        print('\nHIBA:')
        for h in hibak:
            print('  - ' + h)
        return 1
    print('\nRendben.')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
