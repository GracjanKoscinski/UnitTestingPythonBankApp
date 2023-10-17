import unittest

from ..KontoOsobiste import KontoOsobiste

class TestBankAccountTransfers(unittest.TestCase):
    #osoba moze zrobic przelew i robi
    def test_przelew_przychodzacy_poprawny(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 0
        konto_1.przelew_przychodzacy(100)
        self.assertEqual(konto_1.saldo, 100, "saldo niepoprawne!")
    def test_przelew_wychodzacy_poprawny(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(50)
        self.assertEqual(konto_1.saldo, 50, "saldo niepoprawne!")
    def test_przelew_wychodzacy_niepoprwany(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(150)
        self.assertEqual(konto_1.saldo, 100, "saldo niepoprawne!")
    
    

    #osoba nie ma wystarczajacych srodkow na wykonanie przelewu
