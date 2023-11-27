import requests
import unittest

class TestAccountTransfers(unittest.TestCase):

    url = "http://localhost:5000/api/accounts"
    pesel = "12345678900"

    def setUp(self):
        requests.post(self.url, json={"imie":"Jan","nazwisko":"Kowalski","pesel":self.pesel})
    
    def tearDown(self):
        requests.delete(self.url + "/" + self.pesel)
    
    def test_incoming_transfer_account_exists(self):
        konto = requests.get(self.url+"/"+self.pesel).json()
        response = requests.post(self.url+"/"+self.pesel+"/transfer", json={"amount":500,"type":"incoming"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(konto["saldo"],0)
    
    def test_incoming_transfer_account_doesnt_exist(self):
        response = requests.post(self.url+"/"+"02311801475"+"/transfer", json={"amount":500,"type":"incoming"})
        self.assertEqual(response.status_code, 404)
    
    def test_outgoing_transfer(self):
        requests.post(self.url+"/"+self.pesel+"/transfer",json={"amount":600,"type":"incoming"})
        requests.post(self.url+"/"+self.pesel+"/transfer",json={"amount":100,"type":"outgoing"})
        konto = requests.get(self.url+"/"+self.pesel).json()
        self.assertEqual(konto["saldo"], 500)
    
    def test_failed_outgoing_transfer(self):
        requests.post(self.url+"/"+self.pesel+"/transfer",json={"amount":600,"type":"incoming"})
        requests.post(self.url+"/"+self.pesel+"/transfer",json={"amount":700,"type":"outgoing"})
        konto = requests.get(self.url+"/"+self.pesel).json()
        self.assertEqual(konto["saldo"], 600)