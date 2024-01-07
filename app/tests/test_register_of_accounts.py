import unittest
from ..KontoOsobiste import KontoOsobiste
from ..RegisterOfAccounts import RegisterOfAccounts
from unittest.mock import patch
class TestRegisterOfAccounts(unittest.TestCase):
    imie = "imie"
    nazwisko = "nazwisko"
    pesel = "12345678900"

    @classmethod
    def setUpClass(cls):
        RegisterOfAccounts.register = []
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
    
    def test_3_wyszukiwanie_po_pesel(self):
        konto_4 = KontoOsobiste(self.imie,self.nazwisko,"12345578900")
        RegisterOfAccounts.addToRegister(konto_4)
        found = RegisterOfAccounts.searchByPesel("12345578900")
        self.assertEqual(found,konto_4)

    def test_4_wyszukiwanie_po_pesel_blednie(self):
        konto_5 = KontoOsobiste(self.imie,self.nazwisko,"12345578900")
        RegisterOfAccounts.addToRegister(konto_5)
        found = RegisterOfAccounts.searchByPesel("1234557338900")
        self.assertEqual(found,None)

    @patch('app.RegisterOfAccounts.RegisterOfAccounts.collection')
    def test_5_zaladuj_konta_z_bazy_danych(self,mock_collection):
        mock_collection.find.return_value = [{"imie": "imie", "nazwisko": "nazwisko", "pesel": "12345678900", "saldo": 0, "historia": []}]
        RegisterOfAccounts.loadFromDatabase()
        self.assertEqual(len(RegisterOfAccounts.register),1)
        self.assertEqual(RegisterOfAccounts.register[0].imie,"imie")
        self.assertEqual(RegisterOfAccounts.register[0].nazwisko,"nazwisko")
        self.assertEqual(RegisterOfAccounts.register[0].pesel,"12345678900")
        self.assertEqual(RegisterOfAccounts.register[0].saldo,0)
        self.assertEqual(RegisterOfAccounts.register[0].historia,[])

    @patch('app.RegisterOfAccounts.RegisterOfAccounts.collection')
    def test_6_czy_ladowanie_z_bazy_czysci_liste(self,mock_collection):
        mock_collection.find.return_value = [{"imie": "imie", "nazwisko": "nazwisko", "pesel": "12345678900", "saldo": 0, "historia": []}]
        RegisterOfAccounts.loadFromDatabase()
        self.assertEqual(len(RegisterOfAccounts.register),1)
        RegisterOfAccounts.loadFromDatabase()
        self.assertEqual(len(RegisterOfAccounts.register),1)
    
    @patch('app.RegisterOfAccounts.RegisterOfAccounts.collection')
    def test_7_zapisz_konta_do_bazy_danych(self,mock_collection):
       RegisterOfAccounts.register = []
       konto = KontoOsobiste(self.imie,self.nazwisko,self.pesel)
       konto.saldo = 100
       konto.historia = [1,2,3]
       RegisterOfAccounts.addToRegister(konto)
       RegisterOfAccounts.saveToDatabase()
       mock_collection.delete_many.assert_called_once_with({})
       mock_collection.insert_one.assert_called_once_with({"imie": konto.imie, "nazwisko": konto.nazwisko, "pesel": konto.pesel, "saldo": konto.saldo, "historia": konto.historia})

    @patch('app.RegisterOfAccounts.RegisterOfAccounts.collection')
    def test_8_zapisz_wiele_kont_do_bazy(self, mock_collection):
        konto1 = KontoOsobiste("imie1", "nazwisko1", "pesel1")
        konto2 = KontoOsobiste("imie2", "nazwisko2", "pesel2")
        RegisterOfAccounts.addToRegister(konto1)
        RegisterOfAccounts.addToRegister(konto2)
        RegisterOfAccounts.saveToDatabase()
        # 3 ponieważ jedno konto tworzy setUpClass
        assert mock_collection.insert_one.call_count == 3

    @patch('app.RegisterOfAccounts.RegisterOfAccounts.collection')
    def test_9_zapisz_do_bazy_gdy_rejestr_pusty(self, mock_collection):
        RegisterOfAccounts.register = []
        RegisterOfAccounts.saveToDatabase()
        mock_collection.delete_many.assert_called_once_with({})
        assert mock_collection.insert_one.call_count == 0

    @classmethod
    def tearDownClass(cls):
        RegisterOfAccounts.register = []