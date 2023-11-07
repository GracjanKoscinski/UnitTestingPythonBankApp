import unittest
from ..KontoOsobiste import KontoOsobiste
from ..RegisterOfAccounts import RegisterOfAccounts

class TestRegisterOfAccounts(unittest.TestCase):
    imie = "imie"
    nazwisko = "nazwisko"
    pesel = "12345678900"

    @classmethod
    def setUpClass(cls):
        konto = KontoOsobiste(cls.imie,cls.nazwisko,cls.pesel)
        RegisterOfAccounts.addToRegister(konto)

    def test_1_dodanie_konta(self):
        konto_1 = KontoOsobiste(self.imie,self.nazwisko,self.pesel)
        konto_2 = KontoOsobiste(self.imie+"a",self.nazwisko,self.pesel)
        RegisterOfAccounts.addToRegister(konto_1)
        RegisterOfAccounts.addToRegister(konto_2)
        self.assertEqual(RegisterOfAccounts.howManyAccounts(),3)
    
    def test_2_dodanie_konta(self):
        konto_3 = KontoOsobiste(self.imie+"b",self.nazwisko,self.pesel)
        RegisterOfAccounts.addToRegister(konto_3)
        self.assertEqual(RegisterOfAccounts.howManyAccounts(),4)
    
    @classmethod
    def tearDownClass(cls):
        RegisterOfAccounts.register = []