Feature: Account Transfers

    

  Scenario: Perform incoming transfer to an existing account
    Given a new account with PESEL "02311801470"
    When an incoming transfer of 500 is made to the account
    Then the account balance should be 500
 
  Scenario: Attempt incoming transfer to a non-existing account
    When an incoming transfer of 500 is made to a non-existing account with PESEL "12311801475"
    Then the response status code should be 404

  Scenario: Perform outgoing transfer
    Given a new account with PESEL "02311801471"
    Given an incoming transfer of 600 is made to the account
    When an outgoing transfer of 100 is made from the account
    Then the account balance should be 500

  Scenario: Attempt outgoing transfer with insufficient balance
    Given a new account with PESEL "02311801472"
    Given an incoming transfer of 600 is made to the account
    When an outgoing transfer of 700 is made from the account
    Then the account balance should be 600