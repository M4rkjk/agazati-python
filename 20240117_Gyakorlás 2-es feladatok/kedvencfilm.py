def atvalt(hossz: int) -> str:
    ora = hossz // 60  # 73 perc -> // 60 => 1
    perc = hossz % 60  # 73 % 60 => 13
    return[ora, perc]



for i in range(3):
    cim = input('Add meg egy film címét!')
    hossz = int(input('Hány perces a film?'))
    ido = atvalt(hossz)
    print(f'A(z) {cim} című film {ido[0]} óra {ido[1]} perc hosszú')
