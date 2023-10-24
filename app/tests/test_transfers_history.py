import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestBankAccountTransfersHistory(unittest.TestCase):

    def test_historia_konto_osobiste_przychodzacy(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 0
        konto_1.przelew_przychodzacy(100)
        self.assertEqual(konto_1.historia, [100], "historia niepoprawna!")
    def test_historia_konto_osobiste_wychodzacy(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(50)
        self.assertEqual(konto_1.historia, [-50], "historia niepoprawna!")
    def test_historia_konto_osobiste_express(self):
        konto_1 = KontoOsobiste("imie","nazwisko","10000000000")
        konto_1.saldo = 300
        konto_1.przelew_express_wychodzacy(100)
        self.assertEqual(konto_1.historia, [-100,-1], "historia niepoprawna!")
    #konto firmowe
    def test_historia_konto_firma_przychodzacy(self):
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 100
        konto_1.przelew_przychodzacy(50)
        self.assertEqual(konto_1.historia, [50], "saldo niepoprawne!")
    def test_historia_konto_firma_wychodzacy(self):
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 100
        konto_1.przelew_wychodzacy(50)
        self.assertEqual(konto_1.historia, [-50], "saldo niepoprawne!")
    def test_historia_konto_firma_express(self):
        konto_1 = KontoFirmowe("nazwa","1234567890")
        konto_1.saldo = 100
        konto_1.przelew_express_wychodzacy(50)
        self.assertEqual(konto_1.historia, [-50,-5], "saldo niepoprawne!")

    