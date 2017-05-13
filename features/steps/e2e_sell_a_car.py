'''
Created on May 12, 2017

@author: csantoso
'''

"""
Feature: Selling a car

    As a prospect used car seller
    I want to let Truva know that I am interested to sell my car via Truva



Scenario: Submitting information in Jual page

    # Given I am on Truva home page
    Given I am on Truva Jual page
    When I enter my name and phone number in the displayed form
        And I enter mock@truva.id in the email address field of the form
        And I enter my car information in the form
        And I click the Submit button
    Then I see a notification that my message is sent
        # And I receive an email from Truva
"""
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import static_variable as sv

from utilities import common as utilCommon

import time

@given('I am on Truva Jual page')
def step_impl(context): 
    context.browser.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/jual/']").click()
    time.sleep(3)
    
    if context.browser.current_url == sv.HOME_URL_PATH+sv.EXT_JUAL_URL_PATH:
        print ("Current URL : "+context.browser.current_url)
    else:
        assert context.failed is True  
        
    print("Check All Elements")
    elements = context.browser.find_elements(By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input")#"//form[@action='/jual/#wpcf7-f5-p9-o2']/p")
    for element in elements:
        print(element.get_attribute("type"))
        print(element.get_attribute("innerHTML"))
#         print(element.find_element(By.XPATH,"//input").get_attribute("placeholder"))


@when('I enter my name and phone number in the displayed form')
def step_impl(context):
#     time.sleep(2)
    
#     wait = WebDriverWait(context.browser, 10)
    
#     name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
#     name.clear()
#     name.send_keys("Test")
#     phonenum = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='phonenum']")))
#     phonenum.clear()
#     phonenum.send_keys("08110011011")
    
    print("inserting name")
    context.browser.execute_script("document.getElementsByName('_wpcf7').type='none'")
    context.browser.execute_script('document.getElementsByName("name").value="TestName"')
    context.browser.execute_script('document.getElementsByName("name").placeholder="TestName"')
    context.browser.find_element(By.XPATH,"//input[@name='name']").click()
    context.browser.find_element(By.XPATH,"//input[@name='name']").send_keys("Test Name")
    print("inserting phoneNumber")
    context.browser.execute_script('document.getElementsByName("phonenum").value="08110011011"')

    pass

@when('I enter mock@truva.id in the email address field of the form')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    
    email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
    email.clear()
    email.send_keys("mock@truva.id")

    pass

@when('I enter my car information in the form')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    
    model = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='model']")))
    model.clear()
    model.send_keys("Honda")
    
    year = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='year']")))
    year.clear()
    year.send_keys("2016")
    
    odo = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='odo']")))
    odo.clear()
    odo.send_keys("100000")
    
    location = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='location']")))
    location.clear()
    location.send_keys("Bali")
    
    pass

@when('I click the Submit button')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    
    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']")))
#     submit.clear()
    submit.click()
    pass


@then('I see a notification that my message is sent')
def step_impl(context):
    pass

