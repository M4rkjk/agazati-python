from hires import Híres

hires_nok: list[Híres] = []

for i in range(3):
    nev = input('Add meg egy híres nő nevét! ')
    foglalkozas = input('Add meg a foglalkozását! ')
    nemzetiseg = input('Add meg a nemzetiségét (a/n)! ')
    hires_nok.append(Híres(nev, foglalkozas, nemzetiseg))

for h in hires_nok:
    print(f'{h.elotag()} {h.nev} egy híres {h.foglalkozas}') 