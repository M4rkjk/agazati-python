def sikeres(pontszam: int) -> bool:
    return pontszam > 48

while True:
    nev = input("Adja meg a vizsgázó nevét! ")
    if nev == '':
        break
    pontszam = int(input('Adja meg a pontszámát! '))
    if sikeres(pontszam):
        print(f'{nev} Vizsgája sikeres. ')
    else:
        print(f'{nev} Vizsgája sikertelen')