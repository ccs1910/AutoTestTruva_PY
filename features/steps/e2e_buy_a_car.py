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
    
#     if context.browser.current_url != sv.HOME_URL_PATH:
#         context.browser.find_element(By.XPATH,"//div[@class='navbar-header']/a[@href='/']").click()
#         
#     else :    
#         if context.browser.current_url == sv.HOME_URL_PATH:
#             print ("Current URL : "+context.browser.current_url)
#             
#         else:
#             assert context.failed is True   
    context.wait = WebDriverWait(context.browser, 5)
    context.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[.='Penawaran Terbaik Saat Ini']")))
    
    context.browser.find_element(By.XPATH, "//div[@class='slide'][1]/a/div[@class='car-block']/div[@class='img-flex']/img").click()

    print("Chosen Car : "+context.browser.current_url)

@when('I click on Hubungi Kami button')
def step_impl(context): 
    callUs = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-target='#buy-form-modal']")))
    callUs.click()
    

@when('I enter my name and phone number in the popped-up form')
def step_impl(context): 
    name = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='buy-form-modal']//p//input[@name='name']")))
    name.clear()
    name.click()
    name.send_keys(sv.TEST_NAME)

@when('I enter mock@truva.id in the email address field of the popped-up form')
def step_impl(context): 
    phonenum = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='buy-form-modal']//p//input[@name='phonenum']")))
    phonenum.clear()
    phonenum.click()
    phonenum.send_keys(sv.TEST_PHONENUMBER)

    email = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='buy-form-modal']//p//input[@name='email']")))
    email.clear()
    email.click()
    email.send_keys(sv.TEST_EMAIL)
    

@when('I click the Submit button in the popped-up form')
def step_impl(context): 
    submit = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='buy-form-modal']//p//input[@type='submit']")))
    submit.click()

@then('I see a notification that my message is sent in the popped-up form')
def step_impl(context):
    response = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='buy-form-modal']//form[@class='wpcf7-form sent']//div[@role='alert']")))
    
    print("Response : "+response.get_attribute('innerHTML'))
    
    if response.get_attribute('innerHTML') != sv.TEST_SUCCESS_SUBMIT :
        print("Notification : ",response.get_attribute('innerHTML'))
        assert context.failed is True 
        
        