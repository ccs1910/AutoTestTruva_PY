Feature: Buying a car

    As a prospect used car buyer
    I want to let Truva know that I am interested to buy a particular car



Scenario: Submitting my contact information in car detail page

    Given I am on a random car detail page on Truva
    When I click on Hubungi Kami button 
        And I enter my name and phone number in the popped-up form
        #And I enter my name and phone number in the displayed form
        And I enter mock@truva.id in the email address field of the popped-up form
        #And I enter mock@truva.id in the email address field of the form
        And I click the Submit button in the popped-up form
    Then I see a notification that my message is sent in the popped-up form
        # And I receive an email from Truva
