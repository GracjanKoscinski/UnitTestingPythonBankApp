import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678900"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie,self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko,self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        
    
    def test_tworzenie_konta_z_peselem(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.pesel, self.pesel,"Pesel nie został zapisany!")

    #tutaj proszę dodawać nowe testy