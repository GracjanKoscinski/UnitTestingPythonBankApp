from .Konto import Konto
import requests
from datetime import date
import os
from dotenv import load_dotenv
load_dotenv()

class KontoFirmowe(Konto):
    express_trasnfer_fee = 5
    def __init__(self, name, nip):
        super().__init__()
        self.name = name
        self.nip = nip
        self.saldo = 0
        if len(self.nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            czy_w_rejestrze = self.czy_w_rejestrze(self.nip)
            if not czy_w_rejestrze:
                raise ValueError("This NIP does not exist")
    
    def zaciagnij_kredyt(self, kwota_kredytu):
       if(self.saldo >= kwota_kredytu*2) and -1775 in self.historia:
           self.saldo += kwota_kredytu
           return True
       else:
           return False
    
    def czy_w_rejestrze(self, nip):
        today = date.today()
        base_url = os.getenv("url")
        url = base_url+"/"+str(nip)+"?date="+str(today)
        response = requests.get(url)
        print(response.status_code)
        if response.status_code==200:
            return True
        return False
