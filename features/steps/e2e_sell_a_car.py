'''
Created on May 12, 2017

@author: csantoso
'''


from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import static_variable as sv

from utilities import common as utilCommon

import time

@given('I am on Truva Jual page')
def step_impl(context): 
    
    if context.browser.current_url != sv.HOME_URL_PATH+sv.EXT_JUAL_URL_PATH:
        context.browser.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/jual/']").click()
        time.sleep(3)
    else :    
        if context.browser.current_url == sv.HOME_URL_PATH+sv.EXT_JUAL_URL_PATH:
            print ("Current URL : "+context.browser.current_url)
        else:
            assert context.failed is True  
        
        """DO NOT DELETE, FOR DEBUG"""
#     print("Check All Elements") 
#     elements = context.browser.find_elements(By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input")#"//form[@action='/jual/#wpcf7-f5-p9-o2']/p")
#     for element in elements:
#         print("type: ",element.get_attribute("type"))
#         
#         if(element.get_attribute("name") is None):
#             assert context.failed is True


@when('I enter my name and phone number in the displayed form')
def step_impl(context):

    wait = WebDriverWait(context.browser, 3)
    
    name = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='name']")))
    name.clear()
    name.click()
    name.send_keys(sv.TEST_NAME)

    phonenum = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='phonenum']")))
    phonenum.clear()
    phonenum.click()
    phonenum.send_keys(sv.TEST_PHONENUMBER)
    

@when('I enter mock@truva.id in the email address field of the form')
def step_impl(context):
    wait = WebDriverWait(context.browser, 3)
    
    email = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='email']")))
    email.click()
    email.send_keys(sv.TEST_EMAIL)
    
@when('I enter my car information in the form')
def step_impl(context):
    wait = WebDriverWait(context.browser, 3)
    
    model = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='model']")))
    model.clear()
    model.click()
    model.send_keys(sv.TEST_MODEL)
    
    year = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='year']")))
    year.clear()
    year.click()
    year.send_keys(sv.TEST_YEAR)
    
    odo = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='odo']")))
    odo.clear()
    odo.click()
    odo.send_keys(sv.TEST_ODO)
    
    location = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@name='location']")))
    location.clear()
    location.click()
    location.send_keys(sv.TEST_LOCATION)
    

@when('I click the Submit button')
def step_impl(context):
    wait = WebDriverWait(context.browser, 3)
    
    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/p//input[@type='submit']")))
#     submit.clear()
    submit.click()
    


@then('I see a notification that my message is sent')
def step_impl(context):
    wait = WebDriverWait(context.browser, 5)
    
    response = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/jual/#wpcf7-f5-p9-o2']/div[@role='alert']")))
#     print(response.get_attribute('innerHTML'))
    
    if response.get_attribute('innerHTML') != sv.TEST_SUCCESS_SUBMIT :
        print("Notification : ",response.get_attribute('innerHTML'))
        assert context.failed is True
    