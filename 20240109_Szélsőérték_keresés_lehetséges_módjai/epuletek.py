from epulet import Epulet

epuletek: list[Epulet] = []


def beolvas(fajlnev: str):
    fajl = open(fajlnev, 'r', encoding='utf-8')
    fajl.readline()
    for sor in fajl:
        epuletek.append(Epulet(sor.strip()))
    fajl.close()


# Milyen magas a legmagasabb épület?
def legmagasabb() -> int:
    maximum_magassag = epuletek[0].magasság
    for e in epuletek:
        if e.magasság > maximum_magassag:
            maximum_magassag = e.magasság
    return maximum_magassag

# Melyik épület a legmagasabb írjuk ki több adatát is!
# v1. vagy az Epulet osztálypéldányt adom vissza
def legmagasabb_epuletv1() -> Epulet:
    legmagasabb_epulet = epuletek[0]
    for e in epuletek:
        if e.magasság > legmagasabb_epulet.magasság:
            legmagasabb_epulet = e
    return legmagasabb_epulet

# v2. vagy egy indexet adok vissza: az épület sorszámát a listában.
def legmagasabb_epulet_index() -> int:
    magasabb = 0
    for index in range(len(epuletek)):
        if epuletek[index].magasság > epuletek[magasabb].magasság:
            magasabb = index
    return magasabb

# Ha több legmagasabb is lehetséges
def legmagasabbak() -> list[Epulet]:
    _legmagasabbak = []
    for e in epuletek:
        if e.magasság == legmagasabb():
            _legmagasabbak.append(e)
    return _legmagasabbak


# Ha nem az összes épületet kell vizsgálni
# P1. Melyik a legmagasabb francia épület?
# nem tehetem bele az első elemet a max változómba!
def legmagasabb_epulet_adott_orszagban(orszag: str) -> Epulet:
    _legnagyobb_magassag = -1
    _legmagasabb_epulet = None
    for e in epuletek:
        if e.ország == orszag and e.magasság > _legnagyobb_magassag:
            _legnagyobb_magassag = e.magasság
            _legmagasabb_epulet = e
    return _legmagasabb_epulet
