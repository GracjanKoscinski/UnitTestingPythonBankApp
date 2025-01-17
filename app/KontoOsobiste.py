from .Konto import Konto
from datetime import date
class KontoOsobiste(Konto):
    express_trasnfer_fee = 1
    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
        super().__init__()
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
    
    def zaciagnij_kredyt(self, kwota_kredytu):
        if all(element > 0 for element in self.historia[-3:]) and len(self.historia) >= 3:
            self.saldo += kwota_kredytu
            return True
        elif sum(self.historia[-5:]) > kwota_kredytu and len(self.historia) >= 5:
            self.saldo += kwota_kredytu
            return True
        else:
            return False

    def wyslij_historie_na_maila(self, adresat, SMTPConnection):
        today = date.today()
        topic = f"Wyciąg z dnia {str(today)}"
        content = f"Twoja historia konta to: {self.historia}"
        result = SMTPConnection.wyslij(topic, content, adresat)
        return result