import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url="http://localhost:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"imie":"Jan", "nazwisko":"Kowalski","pesel":"02311801475"})
        self.assertEqual(response.status_code, 201)
    
    def test_2_how_many_accounts(self):
        response = requests.get(self.url+"/count")
        self.assertEqual(response.status_code, 200)

    def test_3_serach_by_pesel(self):
        response = requests.get(self.url+"/02311801475")
        self.assertEqual(response.status_code,200)
    
    def test_4_serach_by_pesel_no_account(self):
        response = requests.get(self.url+"/02311801445")
        self.assertEqual(response.status_code,404)
    
    # def test_5_deleting_account_by_pesel(self):
    #     resposne = requests.delete(self.url+"/02311801475")
    #     self.assertEqual(resposne.status_code,301)