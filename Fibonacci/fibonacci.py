# 0, 1, 1, 1, 2, 3, 5, 8, 13, 21...
# A nulladik eleme 0, az első eleme 1,
# a további elemeket az elöző kettő összegeként kapjuk.
# a(n) = a(n-1) + a(n-2)
# aktuális = elöző + előzö_elötti
# Kérjünk be egy n számot és írjuk ki a sorozat első n darab elemét!

n = int(input('Hány elemű legyen a sorozat?: '))

elozo_elotti = 0
elozo = 1

if n >= 2:
    print('0 1', end='')
elif n ==1:
    print('0')
for i in range(n-2): #pl. 10 elemű sorozatnál (mivel az első két elem megvan) 8 elemet kell kiszámolni
    aktualis = elozo_elotti + elozo
    elozo_elotti = elozo
    elozo = aktualis
    print(aktualis, end=' ')