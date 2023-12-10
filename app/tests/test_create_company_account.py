import unittest
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch


class TestCreateBankAccount(unittest.TestCase):
    name = "Firma123"

    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_tworzenie_konta(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        nip = "8461627563"
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.name,self.name, "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip,nip, "Nip nie został zapisany!")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_tworzenie_konta_z_nieistniejacym_nip(self,czy_w_rejestrze):
        nip = "1234567891"
        czy_w_rejestrze.return_value = False
        with self.assertRaises(Exception) as context:
            KontoFirmowe(self.name,nip)
        self.assertTrue("This NIP does not exist" in str(context.exception))

    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_tworzenie_konta_zla_dlugosc(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = False
        nip = "1"
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.name,self.name, "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip,"Niepoprawny NIP!", "Nip powinien być niepoprawny!")

    @patch('requests.get')
    def test_czy_w_rejestrze_false(self, mock_get):
        nip = "1234567891"
        mock_get.return_value.status_code = 404
        with self.assertRaises(ValueError):
            KontoFirmowe(self.name, nip)
    
    @patch('requests.get')
    def test_czy_w_rejestrze_true(self, mock_get):
        nip = "1234567891"
        mock_get.return_value.status_code = 200
        pierwsze_konto = KontoFirmowe(self.name,nip)
        self.assertEqual(pierwsze_konto.nip,nip, "Nip nie został zapisany!")
