class Híres:
    def __init__(self, nev, foglalkozas, nemzetiseg) -> None:
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg =  nemzetiseg


    def elotag(self):
        if self.nemzetiseg == 'a':
            return 'Mrs'
        else:
            return 'Frau'