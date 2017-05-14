'''
Created on May 13, 2017

@author: csantoso
'''

"""
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
"""

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import static_variable as sv

from utilities import common as utilCommon

import time


@given('I am on a random car detail page on Truva')
def step_impl(context): 
#     print(" Move to Cari/Beli Page : ",context.browser.current_url)
    
    if context.browser.current_url != sv.HOME_URL_PATH+sv.EXT_CARI_URL_PATH:
        context.browser.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/cari/']").click()
        time.sleep(3)
    else :    
        if context.browser.current_url == sv.HOME_URL_PATH+sv.EXT_CARI_URL_PATH:
            print ("Current URL : "+context.browser.current_url)
            
        else:
            assert context.failed is True   


@when('I click on Hubungi Kami button')
def step_impl(context): 
    pass

@when('I enter my name and phone number in the popped-up form')
def step_impl(context): 
    pass

@when('I enter mock@truva.id in the email address field of the popped-up form')
def step_impl(context): 
    pass

@when('I click the Submit button in the popped-up form')
def step_impl(context): 
    pass

@then('I see a notification that my message is sent in the popped-up form')
def step_impl(context): 
    pass

