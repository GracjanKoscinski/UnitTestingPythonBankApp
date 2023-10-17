from .Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel="Niepoprawny pesel!"
        else:
            self.pesel = pesel

        #jeżeli urodzony po 1960 to sprawdz czy dobry kod
        if self.pesel != "Niepoprawny pesel!":
            if self.czy_urodzony_po_1960(pesel) and self.czy_kod_promocyjny_poprawny(kod_promocyjny):
                self.saldo = 50
    
    def czy_kod_promocyjny_poprawny(self, kod_promocyjny):
        if kod_promocyjny == None:
            return False
        return len(kod_promocyjny) == 8 and kod_promocyjny[:5] == "PROM_"
    
    def czy_urodzony_po_1960(self,pesel):
        if int(pesel[2:4]) > 12 and int(pesel[2:4]) < 81:
            return True
            #print("Osoba urodzona po 2000 roku")
        elif int(pesel[2:4]) < 13 and int(pesel[:2]) > 60:
            return True
            #print("Osoba urodzona między 1960 (nie włącznie) a 2000 rokiem")
        else:
            return False