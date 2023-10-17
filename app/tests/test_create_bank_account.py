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
        self.assertEqual(pierwsze_konto.pesel, self.pesel,"Pesel nie został zapisany!")
        
    def test_tworzenie_konta_z_krotkim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, "12345678")
        self.assertEqual(konto.pesel,"Niepoprawny pesel!", "wartosc nie zostala zapisana")
    
    def test_tworzenie_konta_z_dlugim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, "123453333678")
        self.assertEqual(konto.pesel,"Niepoprawny pesel!", "wartosc nie zostala zapisana")

    def test_tworzenie_konta_z_poprawnym_kodem_promocyjnym(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "kod nie zostal zaakceptowany!")
    
    def test_tworzenie_konta_z_niepoprawnym_kodem_promocyjnym(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_12345")
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")
    
    def test_tworzenie_konta_z_niepoprawnym_kodem_promocyjnym_preffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "TEST_XYZ")
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")
    
    def test_osoba_urodzona_w_1970(self):
        konto = Konto(self.imie, self.nazwisko, "70010112345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "kod nie został zaakceptowany")
    
    def test_osoba_urodzona_w_1970_zly_kod(self):
        konto = Konto(self.imie, self.nazwisko, "70010112345", "ZLY_KOD")
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")
    
    def test_osoba_urodzona_w_1970_zly_pesel(self):
        konto = Konto(self.imie, self.nazwisko,"700101", "PROM_XYZ" )
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")

    def test_osoba_urodzona_w_1960(self):
        konto = Konto(self.imie, self.nazwisko, "60010112345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")

    def test_osoba_urodzona_w_1960_zly_kod(self):
        konto = Konto(self.imie, self.nazwisko, "60010112345", "ZLY_KOD")
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")

    def test_osoba_urodzona_w_1960_zly_pesel(self):
        konto = Konto(self.imie, self.nazwisko,"60010112345333", "PROM_XYZ" )
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")
    
    def test_osoba_urodzona_w_2003(self):
        konto = Konto(self.imie, self.nazwisko, "03310112345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "kod nie został zaakceptowany")
    
    def test_osoba_urodzona_w_2003_zly_kod(self):
        konto = Konto(self.imie, self.nazwisko,"03311801475", "ZLY_KOD" )
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")
    
    def test_osoba_urodzona_w_2003_zly_pesel(self):
        konto = Konto(self.imie, self.nazwisko,"0333333333333333333333", "PROM_XYZ" )
        self.assertEqual(konto.saldo, 0, "kod został zaakceptowany(nie powinien zostać zaakceptowany)")


    #tutaj proszę dodawać nowe testy