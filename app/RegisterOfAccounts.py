from .KontoOsobiste import KontoOsobiste
from pymongo import MongoClient
class RegisterOfAccounts:
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['konta']
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
    
    @classmethod
    def saveToDatabase(cls):
        cls.collection.delete_many({})
        for konto in cls.register:
            cls.collection.insert_one({"imie:": konto.imie, "nazwisko": konto.nazwisko, "pesel": konto.pesel, "saldo": konto.saldo, "historia:": konto.historia})
    
    @classmethod
    def loadFromDatabase(cls):
        for konto in cls.collection.find():
            cls.register.append(KontoOsobiste(konto["imie"], konto["nazwisko"], konto["pesel"], konto["saldo"], konto["historia"]))