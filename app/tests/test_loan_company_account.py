import unittest
from parameterized import parameterized
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestBankAccountLoanPersonal(unittest.TestCase):
    nazwa = "nazwa"
    nip = "8461627563"
    def setUp(self):
        self.konto = KontoFirmowe(self.nazwa,self.nip)

    @parameterized.expand([
    ([-1775,100,100,100],1000,500,True,1500),
    ([100,-100,200,-1775],500,300,False,500),
    ([100,100,200,300],1000,50,False,1000),
    ([100,100,20,-30],10,50,False,10)
    ])
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_zaciaganie_kredytow(self,historia,saldo,kwota,oczekiwany_wynik,oczekiwane_saldo,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        self.konto.historia = historia
        self.konto.saldo = saldo
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany,oczekiwany_wynik)
        self.assertEqual(self.konto.saldo,oczekiwane_saldo)
