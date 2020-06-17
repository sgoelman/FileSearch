# Created by sgoel at 17/06/2020
Feature: SearchFiles and Folders
  Tests that validate search criteria


  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
    Given I am logged in to application
    When I convert DNA:"<DNA>" to amino acid
    Then I validate that I receive the correct "<Output shortest sequence>"
    And I validate that I receive the correct "<Output total different combinations>"
    And I validate that I receive the correct "<Total amino acid sequences>"
    Examples:
      | DNA | Output shortest sequence | Output total different combinations | Total amino acid sequences |
      | TGC | is', 'MPPPPP*', '        | AA se                               | 20 DNA                     |