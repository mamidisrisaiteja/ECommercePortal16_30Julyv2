@inventory @smoke
Feature: Inventory Module
  As a user of the e-commerce application
  I want to be able to view and interact with products
  So that I can manage my shopping experience

  Background:
    Given the user navigates to the login page
    And user logs in with valid credentials

  @TC_INV_01
  Scenario: Verify product listing
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And user clicks Login Button
    Then verify page has text "Products"
    And verify page has text "Add to cart"

  @TC_INV_02
  Scenario: Sort products by Name (A–Z)
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And user clicks Login Button
    Then verify page has text "Products"
    And user clicks Sort Icon
    And user clicks Sort the Products by Name (A–Z)
    Then all the products must be sorted from A to Z
