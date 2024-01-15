class Eredmeny:
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.Versenyzo = adatok[0]
        self.Rajtszam = int(adatok[1])
        self.Kategoria = adatok[2]
        self.Versenyido = adatok[3]
        self.TavSzazalek = int(adatok[4])

        
        ido_adatok = self.Versenyido.split(':')
        self.ido_oraban = int(ido_adatok[0]) + int(ido_adatok[1]) / 60 + int(ido_adatok[2]) / 3600
                             #óra                  #perc / 60                   #masodperc / 3600