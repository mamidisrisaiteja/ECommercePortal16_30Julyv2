@auth
Feature: Authentication Module
  As a user of the e-commerce application
  I want to be able to login securely
  So that I can access my account and shop safely

  @TC_AUTH_01
  Scenario: Login with valid credentials
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And user clicks Login Button
    Then verify page has text "Products"

  @TC_AUTH_02
  Scenario: Login with invalid credentials
    Given user is on Login Page
    When user enters user name as "standard_use" and password as "secret_sauce"
    And user clicks Login Button
    Then verify page has text "Epic sadface: Username and password do not match any user in this service"
