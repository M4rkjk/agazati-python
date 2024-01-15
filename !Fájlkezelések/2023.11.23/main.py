from cars import * 

load_from_file('autok.csv')
print_all_data()


# Hány autó szerepel a nyílvántartásban?
print(f'A nyilvántartásban {len(cars)} darab autó szerepel.')


# Hány olyan autó van, amely legalább  200km/h-ra képes.
print(f'{count_cars_by_speed(200)} olyan autó van, amely gyorsabb mint 200kmh/h.')

# Hány adott (Suzuki) autó van a nyílvántartásban?
print(f' {count_cars_by_brand("Suzuki")} Suzuki típusú autó van a nyílvántartásban')

# Mennyi a nyílvántartásban szereplő autók átlag fogyasztása?
print(f'a nyílvántartásban szereplő autók átlag fogyasztása {avg_consumption()} 1/100km')

# Mennyi a megadott típusú autók átlag ára?
print(f'Az Opel típusú autók átlag ára: {avg_price_by_brand("Opel")}Ft')

# Melyik a legdrágább autó?
print('A legdrágább autó adatai: ')
most_expernsive = most_expernsive_car()
print(f'\tRendszáma: {most_expernsive.PlateNumber}')
print(f'\tTípusa: {most_expernsive.Brand}')
print(f'\tÁra: {most_expernsive.Price}')
print(f'\t Lóerő: {most_expernsive.HP}')

# Melyik a legnagyobb teljesitmenyű Lada?
print('A legnagyobb teljeítményű Lada adatai:')
highest_HP = highest_HP_by_brand('Lada')
print(f'\tRendszáma: {highest_HP.PlateNumber}')
print(f'\tKöbcentije: {highest_HP.Cm3}')
print(f'\tÁra: {highest_HP.Price}')
print(f'\t Lóerő: {highest_HP.HP}')
