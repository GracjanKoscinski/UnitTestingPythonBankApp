import unittest
from unittest.mock import patch
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestBankAccountTransfers(unittest.TestCase):
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
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_przelew_przychodzacy_poprawny_firma(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 0
        konto_1.przelew_przychodzacy(100)
        self.assertEqual(konto_1.saldo, 100, "saldo niepoprawne!")
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_przelew_wychodzacy_poprawny_firma(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(50)
        self.assertEqual(konto_1.saldo, 50, "saldo niepoprawne!")
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_przelew_wychodzacy_niepoprwany_firma(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(150)
        self.assertEqual(konto_1.saldo, 100, "saldo niepoprawne!")
    
    def test_przelew_express_osobisty_poprawny(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 100
        konto_1.przelew_express_wychodzacy(10)
        self.assertEqual(konto_1.saldo, 89, "saldo niepoprawne!")

    def test_przelew_express_osobisty_niepoprawny(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 100
        konto_1.przelew_express_wychodzacy(150)
        self.assertEqual(konto_1.saldo, 100, "saldo niepoprawne!")
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')       
    def test_przelew_express_firmowy_poprawny(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto_firmowe = KontoFirmowe("nazwa","8461627563")
        konto_firmowe.saldo = 10
        konto_firmowe.przelew_express_wychodzacy(5)
        self.assertEqual(konto_firmowe.saldo,0,"saldo niepoprawne!")
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_przelew_express_firmowy_niepoprawny(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto_firmowe = KontoFirmowe("nazwa","8461627563")
        konto_firmowe.saldo = 10
        konto_firmowe.przelew_express_wychodzacy(100)
        self.assertEqual(konto_firmowe.saldo,10,"saldo niepoprawne!")
    
    

    #osoba nie ma wystarczajacych srodkow na wykonanie przelewu
