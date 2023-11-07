from .Konto import Konto

class KontoFirmowe(Konto):
    express_trasnfer_fee = 5
    def __init__(self, name, nip):
        super().__init__()
        self.name = name
        self.nip = nip
        self.saldo = 0
        if len(self.nip) != 10:
            self.nip = "Niepoprawny NIP!"
    
    def zaciagnij_kredyt(self, kwota_kredytu):
       if(self.saldo >= kwota_kredytu*2) and -1775 in self.historia:
           self.saldo += kwota_kredytu
           return True
       else:
           return False