class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel = pesel
        if self.czy_kod_promocyjny_poprawny(kod_promocyjny):
            self.saldo = 50
    
    def czy_kod_promocyjny_poprawny(self, kod_promocyjny):
        if kod_promocyjny == None:
            return False
        return len(kod_promocyjny) == 8 and kod_promocyjny[:5] == "PROM_"