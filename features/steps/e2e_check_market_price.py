'''
Created on May 11, 2017

@author: csantoso
'''
from lib2to3.fixes.fix_input import context
from pydoc import importfile
from behave.model import Step



"""
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
"""

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import static_variable as sv

from utilities import common as utilCommon

# def uniqueSelectOption (strSelected, wait, driver, dictCarTrueValue) :
# #     self.__write("__uniqueSelectOption : Starts : Option : "+strSelected)
#     
#     while True :
#         webElementContainer = driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']")
#         
#         webElementContainer.click()
#         
#         listElementOptions = webElementContainer.find_elements(By.TAG_NAME,"option")
#         
#         if len(listElementOptions) > 1:
#            break 
#         else :
#             wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='"+strSelected+"']/option")))
#     
#     strSelectedItem = "temp";
#      
#     while True :
#         strSelectedItem = utilCommon.getRandomElementValue(listElementOptions, 1).get_attribute('text')
#         
#         if(strSelectedItem not in dictCarTrueValue):
#            break
#         
#     dictCarTrueValue[strSelectedItem] = "temporary";
#         
#     driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']/option[.='"+strSelectedItem+"']").click() 
#     
# #     self.__write("__uniqueSelectOption : Ends : Selected Item : "+strSelectedItem)
#     
#     return strSelectedItem


def commonSelectOption (strSelected, browser):
#     self.__write("__commonSelectOption : Starts : Option : "+strSelected)
    wait = WebDriverWait(browser,2)
    
    while True :
        webElementContainer = browser.find_element(By.XPATH,"//select[@id='"+strSelected+"']")
        
        try :
            webElementContainer.click()
        except Exception as exp : 
            strError = "__commonSelectOption : Failed Click : ", str(exp)
            raise utilCommon.MyError(strError)
        except utilCommon.MyError as mE :
            strError = "__commonSelectOption : Failed Click : ", str(mE)
            raise utilCommon.MyError(strError)
        
        listElementOptions = webElementContainer.find_elements(By.TAG_NAME,"option")
        
        if len(listElementOptions) > 1:
           break 
        else :
            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='"+strSelected+"']/option")))
    
    strSelectedItem = utilCommon.getRandomElementValue(listElementOptions, 1).get_attribute('text')
    
    browser.find_element(By.XPATH,"//select[@id='"+strSelected+"']/option[.='"+strSelectedItem+"']").click()
    
#     self.__write("__commonSelectOption : Ends : Selected Item : "+strSelectedItem)
    return strSelectedItem

@given('I am on Truva home page')
def step_impl(context): 
    print(" Do Nothing")
    pass    
    
    
@when('I select a random brand from the TVM brand dropdown list')
def step_impl(context):
    strValue = commonSelectOption('brand', context.browser)
    if(strValue is None):
        assert context.failed is True
    else:
        print("Selected Brand :",strValue)

@when('I select a random model from the TVM model dropdown list')
def step_impl(context):
    strValue = commonSelectOption('model', context.browser)
    if(strValue is None):
        assert context.failed is True
    else:
        print("Selected Model :",strValue)    

@when('I select a random year from the TVM year dropdown list')
def step_impl(context):
    strValue = commonSelectOption('year', context.browser)
    if(strValue is None):
        assert context.failed is True
    else:
        print("Selected Year :",strValue)
        
@when('I select a random variant from the TVM variant dropdown list')
def step_impl(context):
    strValue = commonSelectOption('variant', context.browser)
    if(strValue is None):
        assert context.failed is True
    else:
        print("Selected Variant :",strValue)
        
        
@then('I see a non-blank minimum price')
def step_impl(context):
    strValue = context.browser.find_element(By.XPATH,"//span[@id='tm-value-meter__min-tick']").get_attribute('innerHTML')
    if(strValue is None):
        assert context.failed is True
    else:
        print("Minimum Value :",strValue)
     
@then('I see a non-blank maximum price')
def step_impl(context):
    strValue = context.browser.find_element(By.XPATH,"//span[@id='tm-value-meter__max-tick']").get_attribute('innerHTML')
    if(strValue is None):
        assert context.failed is True
    else:
        print("Maximum Value :",strValue)
    
         