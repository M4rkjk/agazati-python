from HegyekMo import *

beolvas('hegyekMo.txt')
print(f'3. feladat: Hegycsúcsok száma: {hegyek_szama()}')
print(f'4. feladat: Hegycsúszok átlagos magassága: {atlag_magassag()} m.')
print(f'5. feladat: A legmagasabb hegycsúcs adatai:')
legmagasabb_hegy = legmagasabb()
print(f'\tNév: {legmagasabb_hegy.nev}')
print(f'\tHegység: {legmagasabb_hegy.hegyseg}')
print(f'\tMagasság: {legmagasabb_hegy.magassag}')
magassag = int(input('6. feladat: Kérek egy magasságot: '))
if van_magasabb(magassag):
    print(f'\t van {magassag} m-nél magasabb hegycsúcs')
print(f'7. feladat: 3000 lábnál magasabb hegycsúcszok száma: {darab_magasabb_mint(3000)}db.')

print(f'8. feladat: Hegység statisztika:')
for key, value in hegy_statisztika().items():
    print(f'\t{key}: {value} db')

mentes('Bükk-vidék', 'bukk-videk.txt')