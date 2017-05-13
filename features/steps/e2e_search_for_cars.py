'''
Created on May 13, 2017

@author: csantoso
'''

"""
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
        
"""  


from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import static_variable as sv

from utilities import common as utilCommon


@given('I am on Truva Cari page')
def step_impl(context): 
    pass     

@when('I select a random brand from the brand dropdown list')
def step_impl(context): 
    pass        

@when('I select a random transmission from the transmission dropdown list')
def step_impl(context): 
    pass     

@when('I select a random location from the in location dropdown list')
def step_impl(context): 
    pass     

@when('I select a random score range from the in score dropdown list')
def step_impl(context): 
    pass     

@when('I select a random price range from the in price dropdown list')
def step_impl(context): 
    pass   

@then('I see zero or more cars')
def step_impl(context): 
    pass   

@then('Every car that I see matches the criteria that I selected')
def step_impl(context): 
    pass   

@then('Every car that I see are available for sale')
def step_impl(context): 
    pass   