from random import choice

def nevelo(fonev: str) -> str:
    maganhangzok = 'öüóeuioóőúaéáűí'

    if fonev[0] in maganhangzok:
        return 'Az'
    else:
        return 'A'

def jelzo() -> str:
    jelzok = ['könnyed', 'piros', 'nagy']
    return choice(jelzok)

print('Adj meg három főnevet!')
for i in range(3):
    fonev = input(f'{i+1} főnév:')
    print(f'{nevelo(fonev)} {fonev} {jelzo()}.')