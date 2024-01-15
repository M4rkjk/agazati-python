from eredemeny import Eredmeny

eredmenyek: list[Eredmeny] = []


def beolvas(fajlnev: str):
    fajl = open(fajlnev, 'r', encoding='UTF-8')
    fajl.readline()
    for sor in fajl:
        eredmenyek.append(Eredmeny(sor.strip()))
    fajl.close()

def celbaert_versenyzok_szama(kategoria: str) -> int:
    darab = 0
    for e in eredmenyek:
        if e.Kategoria == kategoria and e.TavSzazalek == 100:
            darab += 1
    return darab
            
def leghosszabb_nevu_versenyzo() -> Eredmeny:
    leghosszabb = eredmenyek[0]
    for e in eredmenyek:
        if len(e.Versenyzo) > len(leghosszabb.Versenyzo):
            leghosszabb = e
    return leghosszabb


def atlagos_versenyido(kategoria: str) -> float:
    osszeg = 0
    darab = 0
    for e in eredmenyek:
        if e.Kategoria == kategoria and e.TavSzazalek == 100:
            osszeg += e.ido_oraban
            darab += 1
    return osszeg / darab

    