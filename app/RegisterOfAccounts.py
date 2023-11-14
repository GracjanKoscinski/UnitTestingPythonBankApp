from .KontoOsobiste import KontoOsobiste

class RegisterOfAccounts:
    register = []

    @classmethod
    def addToRegister(cls,account:KontoOsobiste):
        cls.register.append(account)
    

    @classmethod
    def howManyAccounts(cls):
        return len(cls.register)
    
    @classmethod
    def searchByPesel(cls, pesel):
        for konto in cls.register:
            if konto.pesel==pesel:
                return konto
        return None