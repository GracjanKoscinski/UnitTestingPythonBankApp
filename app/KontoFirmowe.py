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