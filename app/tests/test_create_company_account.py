import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    name = "Firma123"
    nip = "1234567890"
    def test_tworzenie_konta(self):
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name,self.name, "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip,self.nip, "Nip nie został zapisany!")
    
    def test_tworzenie_konta_zly_nip(self):
        nip2 = "33"
        pierwsze_konto = KontoFirmowe(self.name,nip2)
        self.assertEqual(pierwsze_konto.nip,"Niepoprawny NIP!","nip nie zostal zapisany")