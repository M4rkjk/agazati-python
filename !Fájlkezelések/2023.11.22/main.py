from autok import *
from os import system

autok_betolt()
while True:
    system('cls')
    print('0 - Kilép')
    print('1 - Új autó adatainak megaadása')
    print('2 - Adatok listázása')
    print('3 - Legerősebb autó')
    print('4 - Az adott színű autók listázása')
    valasz = input('Választás: ')
    match valasz:
        case '0':
            break
        case '1':
            auto_beker()
        case '2':
            print('A nyilvántartásban lévő autók:')
            autok_kiir(autok)
            input('Tovább...')
        case '3':
            legerosebb_auto = legerosebb()
            print('A legerősebb autó adatai: ')
            print(f'\tRendszáma: {legerosebb_auto.rendszam}')
            print(f'\tTípusa: {legerosebb_auto.tipus}')
            print(f'\tMárka: {legerosebb_auto.marka}')
            print(f'\tSzin: {legerosebb_auto.szin}')
            print(f'\tTeljesítménye: {legerosebb_auto.teljesitmeny}')
            input('Tovább....')
        case '4':
            szin = input('Milyen színű autókat listázzunk? ')
            print(f'{szin} színű autók a következőek: ')
            autok_kiir(autok_szin_alapjan(szin))
            input('Tovább....')