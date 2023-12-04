import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url="http://localhost:5000/api/accounts"

    def test_a_create_account(self):
        response = requests.post(self.url, json={"imie":"Jan", "nazwisko":"Kowalski","pesel":"12345678900"})
        self.assertEqual(response.status_code, 201)
    
    def test_b_how_many_accounts(self):
        response = requests.get(self.url+"/count")
        self.assertEqual(response.status_code, 200)

    def test_c_serach_by_pesel(self):
        response = requests.get(self.url+"/12345678900")
        self.assertEqual(response.status_code,200)
    
    def test_d_serach_by_pesel_no_account(self):
        response = requests.get(self.url+"/3")
        self.assertEqual(response.status_code,404)
    
    def test_e_updating_account(self):
        response = requests.patch(self.url + "/12345678900", json={"imie": "UpdatedName"})
        self.assertEqual(response.status_code, 200)

    def test_f_updating_account_doesnt_exist(self):
        response = requests.patch(self.url+"/3")
        self.assertEqual(response.status_code,404)
    
    def test_g_deleting_account_that_doesnt_exist(self):
        response = requests.delete(self.url + "/322")
        self.assertEqual(response.status_code,404)
    
    def test_h_deleting_account_by_pesel(self):
        response = requests.delete(self.url+"/12345678900")
        self.assertEqual(response.status_code,200)

# #konta muszą mieć różny pesel
    def test_i_create_account(self):
        response = requests.post(self.url, json={"imie":"Paweł", "nazwisko":"Kowalski","pesel":"12345678900"})
        self.assertEqual(response.status_code, 201)
    
    def test_j_create_account(self):
        response = requests.post(self.url, json={"imie":"Michał", "nazwisko":"Kowalski","pesel":"12345678900"})
        self.assertEqual(response.status_code, 409)
    
    @classmethod
    def tearDownClass(cls):
        requests.delete("http://localhost:5000/api/accounts/12345678900")