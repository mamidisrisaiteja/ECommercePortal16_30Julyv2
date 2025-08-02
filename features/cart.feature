@cart
Feature: Cart Module
  As a user of the e-commerce application
  I want to be able to add and view items in my cart
  So that I can manage my purchases

  @TC_CART_01
  Scenario: View cart contents
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And user clicks Login Button
    Then verify page has text "Products"
    And user adds first product to cart
    And user clicks cart icon
    Then verify cart page has text "Your Cart"
    And verify cart contains items
