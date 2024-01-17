elso_szam = int(input('Adja meg az első számot: '))
masodik_szam = int(input('Adja meg a második számot: '))
if elso_szam > masodik_szam:
    print(f'{elso_szam} nagyobb, mint a {masodik_szam}')
elif elso_szam < masodik_szam:
    print(f'{elso_szam} kisebb, mint a {masodik_szam}')
else:
    print(f'{elso_szam} és {masodik_szam} egyenlő')