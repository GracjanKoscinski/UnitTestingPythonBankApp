from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, name, nip):
        self.name = name
        self.nip = nip
        self.saldo = 0
        if len(self.nip) != 10:
            self.nip = "Niepoprawny NIP!"