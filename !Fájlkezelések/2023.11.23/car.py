class car:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')

        self.PlateNumber = splitted[0]
        self.Brand = splitted[1]
        self.Year = int(splitted[2])
        self.Cm3 = int(splitted[3])
        self.Price = int(splitted[4])
        self.Doors = int(splitted[5])
        self.Speed = int(splitted[6])
        self.HP = int(splitted[7])
        self.Consumption = float(splitted[8])
        self.Color = (splitted[9])
        self.FirstOwner = int(splitted[10])
