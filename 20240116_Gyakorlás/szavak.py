
elso_szo = (input('Adja meg az első szót: '))
masodik_szo = (input('Adja meg a második szót: '))
if len(elso_szo) > len(masodik_szo):
    print(f'{elso_szo} nagyobb, mint a {masodik_szo}')
elif len(elso_szo) < len(masodik_szo):
    print(f'{elso_szo} kisebb, mint a {masodik_szo}')
else:
    print(f'{elso_szo} és {masodik_szo} egyenlő')