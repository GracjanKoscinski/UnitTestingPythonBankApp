import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    name = "Firma123"
    def test_tworzenie_konta(self):
        nip = "1234567890"
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.name,self.name, "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip,nip, "Nip nie został zapisany!")
    
    def test_tworzenie_konta_zly_nip(self):
        nip = "33"
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.nip,"Niepoprawny NIP!","nip nie zostal zapisany")