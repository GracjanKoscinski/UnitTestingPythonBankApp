import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url="http://localhost:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"imie":"Jan", "nazwisko":"Kowalski","pesel":"12345678900"})
        self.assertEqual(response.status_code, 201)
    
    def test_2_how_many_accounts(self):
        response = requests.get(self.url+"/count")
        self.assertEqual(response.status_code, 200)

    def test_3_serach_by_pesel(self):
        response = requests.get(self.url+"/12345678900")
        self.assertEqual(response.status_code,200)
    
    def test_4_serach_by_pesel_no_account(self):
        response = requests.get(self.url+"/3")
        self.assertEqual(response.status_code,404)
    
    def test_5_updating_account(self):
        response = requests.patch(self.url + "/12345678900", json={"imie": "UpdatedName"})
        self.assertEqual(response.status_code, 200)

    def test_6_updating_account_doesnt_exist(self):
        response = requests.patch(self.url+"/3")
        self.assertEqual(response.status_code,404)
    
    def test_7_deleting_account_that_doesnt_exist(self):
        response = requests.delete(self.url + "/322")
        self.assertEqual(response.status_code,404)
    
    def test_8_deleting_account_by_pesel(self):
        response = requests.delete(self.url+"/12345678900")
        self.assertEqual(response.status_code,200)