# számoljuk meg, hogy hány elem felel meg egy adott feltételnek

from random import randint

szamok = []

for i in range(randint (10, 40)):
    szamok.append(randint(-100, 100))

print(szamok)

# hány elem van a listában
print(f'{len(szamok)} darab szám kerül legenerálásra')

# hány páros szám van a listában?
paros_szam_darab = 0
for szam in szamok:
    if szam % 2 == 0:
        paros_szam_darab += 1
print(f'{paros_szam_darab} páros szám van a számok között. ')


# hány negatív szám van a listában
negativ = 0
for szam in szamok:
    if szam < 0:
        negativ += 1
print(f'{negativ} negatív szám van a számok között. ')