import requests
import unittest

class TestAccountTransfers(unittest.TestCase):
    url_accounts_save = "http://localhost:5000/api/accounts/save"
    url_accounts_load = "http://localhost:5000/api/accounts/load"
    url_accounts_count = "http://localhost:5000/api/accounts/count"
    url_accounts = "http://localhost:5000/api/accounts"
    imie = "Jan"
    nazwisko = "Kowalski"
    pesel = "12345678900"

    @classmethod
    def setUpClass(cls):
        requests.post(cls.url_accounts, json={"imie":cls.imie,"nazwisko":cls.nazwisko,"pesel":cls.pesel})
    
    @classmethod
    def tearDownClass(cls):
        requests.delete(cls.url_accounts + "/" + cls.pesel)
    
    def test_save_load_accounts(self):
        response = requests.patch(self.url_accounts_save)
        self.assertEqual(response.status_code, 200)
        load_response = requests.patch(self.url_accounts_load)
        self.assertEqual(load_response.status_code, 200)
        get_response = requests.get(self.url_accounts + "/" + self.pesel)
        self.assertEqual(get_response.status_code, 200)
        #sprawdz czy dane sie zgadzaja
        self.assertEqual(get_response.json()["imie"], self.imie)
        self.assertEqual(get_response.json()["nazwisko"], self.nazwisko)
        self.assertEqual(get_response.json()["pesel"], self.pesel)
        self.assertEqual(get_response.json()["saldo"], 0)
        self.assertEqual(get_response.json()["historia"], [])
        delete_response = requests.delete(self.url_accounts + "/" + self.pesel)
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(requests.get(self.url_accounts_count).json()["count"], 0)
        