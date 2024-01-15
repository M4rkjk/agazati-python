from car import car

cars : list[car] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for row in file:
        new_car = car(row)
        cars.append(new_car)
        # cars.append(car(row))
    file.close


def print_all_data() -> None:
    for c in cars:
        print(f'{c.PlateNumber} - {c.Brand} - {c.Cm3}cm3  - {c.Price}Ft')


def count_cars_by_speed(speed: int) -> int:
    """
    Megszámolja, hogy hány olyan autó van amelynek a végsebessége eléri a megadott speedet.
    """ 
    counter = 0
    for c in cars:
        if c.Speed >= speed:
            counter += 1
    return counter

def count_cars_by_brand(brand: str) -> int:
    """
    Megszámolja, hogy hány brand típusú autó van.
    """ 
    counter = 0
    for c in cars:
        if c.Brand == brand:
            counter += 1
    return counter

def avg_consumption() -> float:
    sum_consumption = 0
    for c in cars:
        sum_consumption += c.Consumption
    return sum_consumption / len(cars)

def avg_price_by_brand(brand : str) -> float:
    sum_price = 0
    counter = 0
    for c in cars:
        if c.Brand == brand:
            sum_price += c.Price
            counter += 1
    return sum_price / counter

def most_expernsive_car() -> car:
    most_expernsive = cars[0]
    for c in cars:
        if c.Price > most_expernsive.Price:
            most_expernsive = c
    return most_expernsive

def highest_HP_by_brand(brand: str) -> car:
    highest_HP = -1
    highest_HP_car = None
    for c in cars:
        if c.Brand == brand and c.HP > highest_HP:
            highest_HP = c.HP
            highest_HP_car = c
    return highest_HP_car