from cbadas import CBadás

cbadasok: list[CBadás] = []


def beolvasas(fajlnev: str):
    fajl = open(fajlnev, 'r', encoding='UTF-8')
    fajl.readline()
    for sor in fajl:
        cbadasok.append(CBadás(sor.strip()))
    fajl.close()


def bejegyzesek_szama(nev: str) -> int:
    darab = 0
    for c in cbadasok:
        if c.nev == nev:
            darab += 1
    return darab

def legtobb_adas() -> int:
    legtobb = cbadasok[0].adasDB
    for c in cbadasok:
        if c.adasDB > legtobb:
            legtobb = c.adasDB
    return legtobb

def mentes(fajlnev: str) -> None:
    fajl = open(fajlnev, 'w', encoding='utf-8')
    fajl.write('Kezdes;Nev;AdasDb\n')
    for c in cbadasok:
        perc = c.ora * 60 + c.perc
        fajl.write(f' {perc};{c.nev};{c.adasDB}')
        fajl.close()