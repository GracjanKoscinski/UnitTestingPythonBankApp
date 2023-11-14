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
   return jsonify({"count":count})   #Twoja implementacja endpointu




@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
   #Twoja implementacja endpointu
   konto = RegisterOfAccounts.searchByPesel(pesel)
   return jsonify(konto.__dict__), 200

if __name__ == '__main__':
   app.run(debug=True)