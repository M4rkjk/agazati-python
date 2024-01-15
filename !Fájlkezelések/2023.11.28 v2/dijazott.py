class dijazott:
    def __init__(self, sor: str) -> None:
        # év;típus;keresztnév;vezetéknév
        adatok = sor.split(';')
        self.ev = int(adatok[0])
        self.tipus = adatok[1]
        self.keresztnev = adatok[2]
        self.vezeteknev = adatok[3]
        self.teljesnev = self.keresztnev + " " + self.vezeteknev

