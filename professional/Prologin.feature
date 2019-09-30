# Created by alekya at 2019-03-25
Feature: actitime login
  Scenario: Valid login test
    Given user persent with loginpage
    When enter username
    When enter password
    When click on login
    Then user should be presented with homepage

