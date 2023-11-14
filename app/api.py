from flask import Flask, request, jsonify
from .RegisterOfAccounts import RegisterOfAccounts
from .KontoOsobiste import KontoOsobiste




app = Flask(__name__)


@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
   dane = request.get_json()
   print(f"Request o stworzenie konta z danymi: {dane}")
   konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
   RegisterOfAccounts.addToRegister(konto)
   return jsonify({"message": "Konto stworzone"}), 201




@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
   count = RegisterOfAccounts.howManyAccounts()
   return jsonify({"count":count}), 200




@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
   konto = RegisterOfAccounts.searchByPesel(pesel)
   if konto != None:
      return jsonify(konto.__dict__), 200
   else:
      return jsonify({"message":"Nie ma konta o takim peselu"}), 404

#delete
# @app.route("/api/accounts/<pesel>", methods=['DELETE'])
# def usun_konto(pesel):
#    konto = RegisterOfAccounts.searchByPesel(pesel)
#    RegisterOfAccounts.register.remove(konto)
#    return jsonify({"message":"Usunięto konto"},301)
   


#patch

if __name__ == '__main__':
   app.run(debug=True)