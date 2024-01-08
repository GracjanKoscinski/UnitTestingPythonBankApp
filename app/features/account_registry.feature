Feature: Account registry


  Scenario: User is able to create a new account
    Given Number of accounts in registry equals: "0"
    When I create an account using imie: "kurt", nazwisko: "cobain", pesel: "02311801475"
    Then Number of accounts in registry equals: "1"
    And Account with pesel "02311801475" exists in registry

  Scenario: User is able to create a second account
    Given Number of accounts in registry equals: "1"
    When I create an account using imie: "john", nazwisko: "doe", pesel: "12345678900"
    Then Number of accounts in registry equals: "2"


  Scenario: Admin user is able to save the account registry
    When I save the account registry
    Then Number of accounts in registry equals: "2"

  Scenario: User is able to update last name saved in account
    Given Account with pesel "02311801475" exists in registry
    When I update nazwisko to "kobain" for account with pesel: "02311801475"
    Then Account with pesel "02311801475" has nazwisko "kobain"
  
  Scenario: User is able to load account registry
    Given Account with pesel "02311801475" exists in registry
    And Account with pesel "12345678900" exists in registry
    When I load the account registry
    Then Number of accounts in registry equals: "2"
    And Account with pesel "02311801475" exists in registry
    And Account with pesel "12345678900" exists in registry


  Scenario: User is able to delete both accounts
    Given Account with pesel "02311801475" exists in registry
    And Account with pesel "12345678900" exists in registry
    When I delete account with pesel: "02311801475"
    Then Account with pesel "02311801475" does not exists in registry
    When I delete account with pesel: "12345678900"
    Then Account with pesel "12345678900" does not exists in registry
    And Number of accounts in registry equals: "0"

  Scenario: User is able to delete already created account
    When I create an account using imie: "kurt", nazwisko: "cobain", pesel: "02311801475"
    Then Number of accounts in registry equals: "1"
    When I delete account with pesel: "02311801475"
    Then Account with pesel "02311801475" does not exists in registry
    And Number of accounts in registry equals: "0"