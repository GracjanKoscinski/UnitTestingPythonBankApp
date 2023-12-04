import unittest

from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch
@patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
class TestCreateBankAccount(unittest.TestCase):
    name = "Firma123"
    def test_tworzenie_konta(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        nip = "8461627563"
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.name,self.name, "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip,nip, "Nip nie został zapisany!")
    
    def test_tworzenie_konta_z_nieistniejacym_nip(self,czy_w_rejestrze):
        nip = "1234567891"
        czy_w_rejestrze.return_value = False
        with self.assertRaises(Exception) as context:
            konto = KontoFirmowe(self.name,nip)
            self.assertTrue("This NIP does not exist" in str(context.exception))