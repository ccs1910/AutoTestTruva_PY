Feature: Searching for cars

    As a prospect used car buyer
    I want to find cars according to my criteria



Scenario: Using advanced search filters

	Given I am on Truva Cari page
	When I select a random brand from the brand dropdown list
    	And I select a random transmission from the transmission dropdown list
    	And I select a random location from the in location dropdown list
		And I select a random score range from the in score dropdown list
        And I select a random price range from the in price dropdown list
    Then I see zero or more cars
        And Every car that I see matches the criteria that I selected
        And Every car that I see are available for sale



# Scenario: Using search bar in home page



# Scenario: Registering to Truva consultation service
