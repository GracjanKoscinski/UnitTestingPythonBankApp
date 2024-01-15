from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual


assert_equal = AssertEqual()
URL = "http://localhost:5000"


@when('I create an account using imie: "{name}", nazwisko: "{last_name}", pesel: "{pesel}"')
def utworz_konto(context, name, last_name, pesel):
    json_body = { "imie": name, "nazwisko": last_name, "pesel": pesel }
    print(json_body) 
    create_resp = requests.post(URL + "/api/accounts", json = json_body)
    assert_equal(create_resp.status_code, 201)

@step('Number of accounts in registry equals: "{count}"')
def sprawdz_liczbe_kont_w_rejestrze(context, count):
    ile_kont = requests.get(URL + f"/api/accounts/count")
    assert_equal(ile_kont.json()["count"], int(count))


@step('Account with pesel "{pesel}" exists in registry')
def sprawdz_czy_konto_z_pesel_istnieje(context, pesel):
    czy_istnieje = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(czy_istnieje.status_code, 200)
   


@step('Account with pesel "{pesel}" does not exists in registry')
def sprawdz_czy_konto_z_pesel_nie_istnieje(context, pesel):
    czy_istnieje = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(czy_istnieje.status_code, 404)

@when('I delete account with pesel: "{pesel}"')
def usun_konto(context, pesel):
    delete_resp = requests.delete(URL + f"/api/accounts/{pesel}")
    assert_equal(delete_resp.status_code, 200)


@when('I save the account registry')
def zapisz_konta(context):
    resp = requests.patch(URL  + f"/api/accounts/save")
    assert_equal(resp.status_code, 200)



@when('I load the account registry')
def load_rejestr(context):
    load_resp = requests.patch(URL + "/api/accounts/load")
    assert_equal(load_resp.status_code, 200)


@when('I update nazwisko to "{new_last_name}" for account with pesel: "{pesel}"')
def update_nazwisko(context, new_last_name, pesel):
    json_body = { "nazwisko": new_last_name}
    update_resp = requests.patch(URL + f"/api/accounts/{pesel}", json = json_body)
    assert_equal(update_resp.status_code, 200)


@then('Account with pesel "{pesel}" has nazwisko "{nazwisko}"')
def verify_nazwisko(context, pesel, nazwisko):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(response.status_code, 200)
    assert_equal(response.json()["nazwisko"], nazwisko)

