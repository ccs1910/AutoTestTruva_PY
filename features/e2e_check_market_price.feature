Feature: Checking market price

    As a prospect used car seller
    I want to know the fair market price of the car that I want to sell

    As a prospect used car buyer
    I want to know the fair market price of the car that I want to buy



Scenario: Using True Value Meter (TVM) in home page

    Given I am on Truva home page
    When I select a random brand from the TVM brand dropdown list
        And I select a random model from the TVM model dropdown list
        And I select a random year from the TVM year dropdown list
        And I select a random variant from the TVM variant dropdown list
    Then I see a non-blank minimum price
        And I see a non-blank maximum price
