import requests
from behave import *
url = "http://localhost:5000/api/accounts"

@given('a new account with PESEL "{new_pesel}"')
def step_create_account(context, new_pesel):
    requests.post(url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": new_pesel})
    context.new_pesel = new_pesel

@when('an incoming transfer of {amount:d} is made to the account')
def step_incoming_transfer(context, amount):
    response = requests.post(url + "/" + context.new_pesel + "/transfer", json={"amount": amount, "type": "incoming"})
    context.response = response

@when('an outgoing transfer of {amount:d} is made from the account')
def step_outgoing_transfer(context, amount):
    response = requests.post(url + "/" + context.new_pesel + "/transfer", json={"amount": amount, "type": "outgoing"})
    context.response = response

@when('an incoming transfer of {amount:d} is made to a non-existing account with PESEL "{non_existing_pesel}"')
def step_non_existing_account_transfer(context, amount, non_existing_pesel):
    response = requests.post(url + "/" + non_existing_pesel + "/transfer", json={"amount": amount, "type": "incoming"})
    context.response = response

@then('the response status code should be {status_code:d}')
def step_check_response_status(context, status_code):
    assert context.response.status_code == status_code

@then('the account balance should be {balance:d}')
def step_check_account_balance(context, balance):
    konto = requests.get(url + "/" + context.new_pesel).json()
    actual_balance = konto.get("saldo", None)
    print(f"Actual Balance: {actual_balance}")
    assert actual_balance == balance

@given('an incoming transfer of {amount:d} is made to the account')
def step_incoming_transfer(context, amount):
    response = requests.post(url + "/" + context.new_pesel + "/transfer", json={"amount": amount, "type": "incoming"})
    context.response = response

@when('an outgoing transfer of {amount:d} is made from the account')
def step_outgoing_transfer(context, amount):
    response = requests.post(url + "/" + context.new_pesel + "/transfer", json={"amount": amount, "type": "outgoing"})
    context.response = response
