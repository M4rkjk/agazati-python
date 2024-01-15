from epuletek import *

beolvas('legmagasabb.txt')
print(f'A legmagasabb épólet magassága: {legmagasabb()} m.')

legmagasabb_epulet = legmagasabb_epuletv1()
print(f'A legmagasabb épület:')
print(f'\tNeve: {legmagasabb_epulet.név}')
print(f'\tMagassága: {legmagasabb_epulet.magasság}')
print(f'\tÉpült: {legmagasabb_epulet.épült}')
print(f'\tOrszág: {legmagasabb_epulet.ország}')
print(f'\tVáros: {legmagasabb_epulet.város}')

print('Legmagasabb épületek: ')
for l in legmagasabbak():
    print(f'\tneve: {l.név}')

print('A legmagasabb francia épület')
legmagasabb_francia = legmagasabb_epulet_adott_orszagban('Franciaország')
print(f'\tMagassága: {legmagasabb_francia.magasság}')
print(f'\tÉpült: {legmagasabb_francia.épült}')
print(f'\tOrszág: {legmagasabb_francia.ország}')
print(f'\tVáros: {legmagasabb_francia.város}')