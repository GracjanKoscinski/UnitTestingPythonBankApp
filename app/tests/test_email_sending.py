import unittest
from unittest.mock import MagicMock, patch
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
from ..SMTPConnection import SMTPConnection
from datetime import date
class TestEmailSending(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678900"
    name = "Firma123"
    nip = "8461627563"

    def test_email_personal_acc_true(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("adres@gmail.com",smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {str(date.today())}",f"Twoja historia konta to: {konto.historia}","adres@gmail.com")
    

    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_email_company_account_true(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto = KontoFirmowe(self.name,self.nip)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=True)
        status = konto.wyslij_historie_na_maila("adres@gmail.com",smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {str(date.today())}",f"Historia konta Twojej firmy to: {konto.historia}","adres@gmail.com")
    
    def test_email_personal_acc_false(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=False)
        status = konto.wyslij_historie_na_maila("adres@gmail.com",smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {str(date.today())}",f"Twoja historia konta to: {konto.historia}","adres@gmail.com")
    
    @patch('app.KontoFirmowe.KontoFirmowe.czy_w_rejestrze')
    def test_email_company_account_false(self,czy_w_rejestrze):
        czy_w_rejestrze.return_value = True
        konto = KontoFirmowe(self.name,self.nip)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=False)
        status = konto.wyslij_historie_na_maila("adres@gmail.com",smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {str(date.today())}",f"Historia konta Twojej firmy to: {konto.historia}","adres@gmail.com")
