
szam_mp = 8435

Óra = szam_mp / 3600
maradék = szam_mp % 3600

Perc = maradék / 60
maradék = maradék % 60

Masodperc = maradék


print(f'{Óra} Óra {Perc:.0f} Perc {Masodperc} Másodperc')
