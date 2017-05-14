'''
Created on May 13, 2017

@author: csantoso
'''
from selenium.common.exceptions import NoSuchElementException
from pip._vendor.pkg_resources import find_nothing

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

import time

def doScoreConversion(inputScore):
#     === This is Temporary, Require Correction ===
    outScore=0
    if(inputScore == 90):
        outScore = 4
    elif(inputScore == 70):
        outScore = 3
    elif(inputScore == 50):
        outScore = 2
#     else:
    return outScore
        
    
            
            

def getFilterValue(strChosenFilter, browser):

    strTempAttribute = browser.find_element(By.XPATH, "//select[@name='"+strChosenFilter+"']").get_attribute("sb")
      
    browser.find_element(By.XPATH, "//a[@id='sbSelector_"+strTempAttribute+"']").click()

    listOfElement = browser.find_elements(By.XPATH, "//ul[@id='sbOptions_"+strTempAttribute+"']/li/a")

    if(strChosenFilter.lower()=="brand".lower()):
        while True :
            strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")
             
            if(strChosenValue.lower()!= "Semua Merek".lower()):
                break
    else:
        strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")

    time.sleep(2) #apparently sleep needed to wait for the value to be displayed.
            
    browser.find_element(By.XPATH, "//ul[@id='sbOptions_"+strTempAttribute+"']/li/a[.='"+strChosenValue+"']").click()
    
    return strChosenValue


@given('I am on Truva Cari page')
def step_impl(context): 
    if context.browser.current_url != sv.HOME_URL_PATH+sv.EXT_CARI_URL_PATH:
        context.browser.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/cari/']").click()
    else :    
        if context.browser.current_url == sv.HOME_URL_PATH+sv.EXT_CARI_URL_PATH:
            print ("Current URL : "+context.browser.current_url)
            
        else:
            assert context.failed is True 
          

@when('I select a random brand from the brand dropdown list')
def step_impl(context): 
    strValue = getFilterValue("brand",context.browser)
    context.chosenBrand = strValue
    print("brand : ",strValue) 

@when('I select a random transmission from the transmission dropdown list')
def step_impl(context):
    time.sleep(2) 
    strValue = getFilterValue("transmission",context.browser)
    context.chosentransmission = strValue
    print("transmission : ",strValue)

@when('I select a random location from the in location dropdown list')
def step_impl(context): 
    time.sleep(2)
    strValue = getFilterValue("location",context.browser)
    context.chosenLocation = strValue
    print("location : ",strValue)
         
@when('I select a random score range from the in score dropdown list')
def step_impl(context): 
    time.sleep(2)
    strValue = getFilterValue("score",context.browser)
    context.chosenScore = strValue
    print("score : ",strValue)     

@when('I select a random price range from the in price dropdown list')
def step_impl(context): 
    time.sleep(2)
    strValue = getFilterValue("price",context.browser)
    context.chosenPrice = strValue
    print("price : ",strValue)   

@then('I see zero or more cars')
def step_impl(context): 
    time.sleep(2)
    listOfElements = context.browser.find_elements(By.XPATH, "//div[@class='inventory_box car_listings boxed boxed_full']/div[@class='col-lg-3 col-md-4 col-sm-6 col-xs-12']")
        
    intTotalResult = len(listOfElements)
    context.resultCarElements = listOfElements
        
    if(intTotalResult==0):
        
        print("ZERO CAR ! ")
    
    else:  
        print("Number of Cars in Page 1 : ",intTotalResult)
        
    

@then('Every car that I see matches the criteria that I selected')
def step_impl(context): 
    dictFindCarTestStatus = {}
    
    strKey= ""
    context.soldCar = 0
    
    if(len(context.resultCarElements) != 0):
        strStatus = sv.STATUS_SUCCESS
        counter = 1
        for item in context.resultCarElements :
               
#             == Validate BRAND == 
            if(context.chosenBrand.upper().startswith("SEMUA")):
                print("__doValidation : Skip : "+context.chosenBrand) 
                
                strStatus=strStatus+" : Brand=Validation_Skipped"
            else :
                strResultBrand = item.find_element(By.XPATH, "//div[@class='auto-thumb__title']").get_attribute("data-brand")
                print("__doValidation : getBrand : "+strResultBrand)
                
                if(strResultBrand!=context.chosenBrand):
                    strStatus=strStatus+" : Brand=NOK"
                    assert context.failed is True
             
#             == Validate SCORE ==              
            if(context.chosenScore.upper().startswith("SEMUA")):
                print("__doValidation : Skip : "+context.chosenScore) 
                strStatus=strStatus+" : Score=Validation_Skipped"
            else :
                strResultScore = item.find_element(By.XPATH, "//div[@class='auto-thumb__score']").get_attribute('innerHTML')
 
                print("__doValidation : getScore : "+strResultScore.strip("<span class=\"max\">&nbsp;/&nbsp;5</span>"))
                 
                floatResultScore = float(strResultScore.strip("<span class=\"max\">&nbsp;/&nbsp;5</span>"))
                 
#                 floatChosenScore = float(context.chosenScore.replace("> ",""))
                floatChosenScore = doScoreConversion(float(context.chosenScore.replace("> ","")))
                                
                if(floatResultScore<floatChosenScore):
                    strStatus=strStatus+" : Score=NOK"
                    assert context.failed is True
                    
#             == Validate PRICE ==                     
            if(context.chosenPrice.upper().startswith("SEMUA")):
                print("__doValidation : Skip : "+strPrice) 
                strStatus=strStatus+" : Price=Validation_Skipped"
            else:
                strResultPrice = item.find_element(By.XPATH, "//div[@class='auto-thumb__price']").get_attribute('innerHTML')
                print("__doValidation : getPrice : "+strResultPrice)
                 
                intResultPrice = int(strResultPrice.strip().replace(".","").strip("Rp"))
                intChosenPrice = int(context.chosenPrice.replace("< ","").replace(".","").strip("Rp"))
                 
                if(intResultPrice>intChosenPrice):
                    strStatus=strStatus+" : Price=NOK"
                    assert context.failed is True
                    

#             == Validate TRANSMISSION ==                    
            if(context.chosentransmission.upper().startswith("SEMUA")):
                print("__doValidation : Skip : "+context.chosentransmission)
                strStatus=strStatus+" : Transmission=Validation_Skipped"
            else:
                strResultTransmission = item.find_element(By.XPATH,"//table/tbody/tr/td[2]").get_attribute("title")
                print("__doValidation : getTransmission : "+strResultTransmission)
                
                if(context.chosentransmission not in strResultTransmission) :
                    strStatus=strStatus+" : Transmission=NOK"
                    assert context.failed is True
                   
                   
#             == Validate LOCATION ==                    
            if(context.chosenLocation.upper().startswith("SEMUA")):
                print("__doValidation : Skip : "+context.chosenLocation)
                strStatus=strStatus+" : Location=Validation_Skipped"
            else:
                strResultLocation = item.find_element(By.XPATH,"//table/tbody/tr/td[3]").get_attribute("title")
                print("__doValidation : getLocation : "+strResultLocation)
                
                if(strResultLocation!=context.chosenLocation):
                    strStatus=strStatus+" : Location=NOK"
                    assert context.failed is True
            
#             == GET SOLD CAR ==            
            try:
                item.find_element(By.XPATH,"//div[@class='auto-thumb__sold-filter']")
                context.soldCar =+1
            except NoSuchElementException:
                print("*Nothing To DO* : Sold Car : "+str(context.soldCar))
                 
            
            dictFindCarTestStatus["Result #"+str(counter)+" outOf "+str(len(context.resultCarElements))]=strStatus
            counter=counter+1
            
        print(dictFindCarTestStatus)
    else:
#         dictFindCarTestStatus[strKey] = sv.STATUS_FAILED+" : TotalResult= "+len(context.resultCarElements)
        print(sv.STATUS_FAILED+" : Total Result= "+str(len(context.resultCarElements)))   

@then('Every car that I see are available for sale')
def step_impl(context): 
    if(context.soldCar > 0):
        print("Sold Car / Not Available : "+str(context.soldCar))
        assert context.failed is True
    