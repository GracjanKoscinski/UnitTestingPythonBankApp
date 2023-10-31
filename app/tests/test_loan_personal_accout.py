import unittest
from parameterized import parameterized

from ..KontoOsobiste import KontoOsobiste

class TestBankAccountLoanPersonal(unittest.TestCase):
    imie = "imie"
    nazwisko = "nazwisko"
    pesel = "12345678900"

    def setUp(self):
        self.konto = KontoOsobiste(self.imie,self.nazwisko,self.pesel)

    @parameterized.expand([
    ([-100,100,100,100],500,True,500),
    ([100,100],500,False,0),
    ([-100,100,-100,200],500,False,0),
    ([-100, 100, -100, 200,-100,-100],500,False,0),
    ([-100, 100, -100, -10, 300, 400],500,True,500),
    ([100, -1000, 300, 400],500,False,0)
    ])
    def test_zaciaganie_kredytow(self,historia,kwota,oczekiwany_wynik,oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany,oczekiwany_wynik)
        self.assertEqual(self.konto.saldo,oczekiwane_saldo)
