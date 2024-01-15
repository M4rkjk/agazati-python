class fogadasi_fordulo:
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.év = int(adatok[0])
        self.hét = int(adatok[1])
        self.fordulo = int(adatok[2])
        self.T13p1 = int(adatok[3])
        self.Ny13p1 = int(adatok[4])
        self.eredmenyek = adatok[5]

    def volt_döntetlen(self) -> bool:
        for e in self.eredmenyek:
            if e == 'X':
                return True
        return False