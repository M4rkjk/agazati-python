from cbadasok import *

beolvasas('cb.txt')
print('3. feladat: CB-rádió')
print(f'3.2 feladat: Bejegyzések száma: {len(cbadasok)} db.')
print(f'3.3 feladat: Sanyihoz tartozó bejegyzések száma: {bejegyzesek_szama("Sanyi")} db')
print(f'3.4 feladat: A legtöbb adás: ')
legtobb = legtobb_adas()
for c in cbadasok:
    if c.adasDB == legtobb:
        print(f'\tIdő: {c.ora}:{c.perc} Darab: {c.adasDB} Név: {c.nev}')

