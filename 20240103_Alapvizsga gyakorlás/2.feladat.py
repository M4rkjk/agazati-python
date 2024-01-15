from random import randint

def halmaze(szamok: list[int]) -> bool:
    # halmaz = set(szamok)
    # halmaz = []
    # for sz in szamok:
    #     if sz not in halmaz:
    #         halmaz.append(sz)

    halmaz = set(szamok)

    if len(halmaz) == len(szamok):
        return True        
    return False


print('2. feladat: Halmaz-e?')

for i in range(8):
    szamok: list[int] = []
    for i in range(5):
        szamok.append(randint(0, 9))
    print(f'1. {szamok}', end=' ---> ')
    if halmaze(szamok):
        print('Halmaznak tekinthető.')
    else:
        print('Halmaznak nem tekinthető.')