Feature: Selling a car

    As a prospect used car seller
    I want to let Truva know that I am interested to sell my car via Truva



Scenario: Submitting information in Jual page

    Given I am on Truva Jual page
    When I enter my name and phone number in the displayed form
        And I enter 'mock@truva.id' in the email address field of the form
        And I enter my car information in the form
        And I click the Submit button
    Then I see a notification that my message is sent
        # And I receive an email from Truva
