from eredmenyek import *
import math

beolvas('ub2017egyeni.txt')
print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')
print(f'3.3 feladat: Célba érkező női sportolók: {celbaert_versenyzok_szama("Noi")}')
print(f'3.4 feladat: A leghosszabb nevű futó')
leghosszabb_nevu_futo = leghosszabb_nevu_versenyzo()
print(f'\tNév: {leghosszabb_nevu_futo.Versenyzo}')
print(f'\tRajtszám: {leghosszabb_nevu_futo.Rajtszam}')
print(f'\tVersenyidő: {leghosszabb_nevu_futo.Versenyido}')

atlag = atlagos_versenyido("Ferfi")
ora = math.floor(atlag)
perc = math.floor((atlag - ora) * 60)
mperc = math.floor((((atlag - ora) * 60) - perc) * 60)

atlag_mp = atlag * 3600
print(f'3.5 feldat: Férfi sportolók átlagos ideje: {atlag} óra {atlag_mp} mp')
print(f'{ora}:{perc}:{mperc}')

mperc = str(atlag_mp % 60).zfill(2)
perc = str((atlag_mp // 60) % 60).zfill(2)
ora = str(atlag_mp // 3600).rjust(2, '0')
# ora = str(1).zfill(2)
# perc = str(5).zfill(2)
# mperc = str(4).zfill(2)

print(f'{ora}:{perc}:{mperc}')