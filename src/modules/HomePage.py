'''
Created on Apr 3, 2017

@author: csantoso
'''
import os
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

import utility.StaticVariable  as Sv
import utility.Common as utilCommon
from _ast import Not


dictHomeTestStatus = {}


def write(strWrite):
    print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)


def _uniqueSelectOption (strSelected, wait, driver, dictCarTrueValue) :
    write("_uniqueSelectOption : Starts : Option : "+strSelected)
    
    while True :
        webElementContainer = driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']")
        
        webElementContainer.click()
        
        listElementOptions = webElementContainer.find_elements(By.TAG_NAME,"option")
        
        if len(listElementOptions) > 1:
           break 
        else :
            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='"+strSelected+"']/option")))
    
    strSelectedItem = "temp";
     
    while True :
        strSelectedItem = utilCommon.getRandomElementValue(listElementOptions, 1).get_attribute('text')
        
        if(strSelectedItem not in dictCarTrueValue):
           break
        
    dictCarTrueValue[strSelectedItem] = "temporary";
        
    driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']/option[.='"+strSelectedItem+"']").click() 
    
    write("_uniqueSelectOption : Ends : Selected Item : "+strSelectedItem)
    
    return strSelectedItem
        
      
        
def _commonSelectOption (strSelected, wait, driver):
    write("_commonSelectOption : Starts : Option : "+strSelected)
    
    while True :
        webElementContainer = driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']")
        
        try :
            webElementContainer.click()
        except Exception as exp : 
            strError = "_commonSelectOption : Failed Click : ", str(exp)
            raise utilCommon.MyError(strError)
        
        listElementOptions = webElementContainer.find_elements(By.TAG_NAME,"option")
        
        if len(listElementOptions) > 1:
           break 
        else :
            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='"+strSelected+"']/option")))
    
#     write("_commonSelectOption : Element Size : "+str(len(listElementOptions)))
    
    strSelectedItem = utilCommon.getRandomElementValue(listElementOptions, 1).get_attribute('text')
    
    driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']/option[.='"+strSelectedItem+"']").click()
    
    write("_commonSelectOption : Ends : Selected Item : "+strSelectedItem)
    
    return strSelectedItem
         
  
def canSeeMarketPrice(driver) :
        
    write("canSeeMarketPrice : Starts")
    
    strCanSeeMarketPrice_Status = "NOK";
    
    wait = WebDriverWait(driver,10)
    
    write("canSeeMarketPrice : Run the Test 3 times ")
    
    dictCarTrueValue = {}
    
    counterCarTrueValue = 0
    
    
    while(counterCarTrueValue < 3) :
                
        # Deciding Choose Brand
        strValue = ""
        
        write("canSeeMarketPrice : Choose Brand ")
        strKey = _uniqueSelectOption(Sv.MARKET_PRICE_OPTION_BRAND, wait, driver, dictCarTrueValue)
                         
        #         Decide Choose Model

        write("canSeeMarketPrice : Choose Model ")
        strValue=strValue+"||"+_commonSelectOption(Sv.MARKET_PRICE_OPTION_MODEL, wait, driver)

        write("canSeeMarketPrice : Choose YEAR ")        
        #         Decide Choose YEAR
        strValue=strValue+"||"+_commonSelectOption(Sv.MARKET_PRICE_OPTION_YEAR, wait, driver)

        write("canSeeMarketPrice : Choose Variant ")        
        #         Decide Choose Variant
        strValue=strValue+"||"+_commonSelectOption(Sv.MARKET_PRICE_OPTION_VARIANT, wait, driver)
        
        #        get Min & MAx Price
        
#         while True : 
#             
#             print(1)
#             strminPrice = driver.find_element(By.XPATH,'//span[@id="tm-value-meter__min-tick"]').get_attribute('text')
# #             driver.find_element(By.XPATH,"//span[@id='tm-value-meter__min-tick']").get_attribute('text')
#             
#             if(strminPrice is not None):
#                 print(2)
#                 break
#             else :
#                 print(3)
#                 time.sleep(5)
# #                 wait.until(EC.text_to_be_present_in_element((By.XPATH,"//span[@id='tm-value-meter__max-tick']")))
#         
#        
#         print(driver.find_element(By.XPATH,'//span[@id="tm-value-meter__min-tick"]').get_attribute('class'))
#         
#         strValue=strValue+"||"+ driver.find_element(By.XPATH,"//span[@id='tm-value-meter__min-tick']").get_attribute('text')
#         strValue=strValue+"||"+ driver.find_element(By.XPATH,"//span[@id='tm-value-meter__max-tick']").get_attribute('text')        
#         
        dictCarTrueValue[strKey] = strValue  
        
        counterCarTrueValue = counterCarTrueValue + 1
        
        time.sleep(2)
            
    write("canSeeMarketPrice : Crawl Result : "+str(dictCarTrueValue))
    
#     Validation
    write("canSeeMarketPrice : Start Validation : ensure No Value in dictionary is not empty")
    
    counterWrong = 0
    for key, value in dictCarTrueValue.items():
        if ((value == "temporary") | (value is None)) :
            counterWrong = counterWrong + 1
            
        
    if (counterWrong > 0 ):
        dictHomeTestStatus[Sv.CAN_SEE_MARKET_PRICE] = strCanSeeMarketPrice_Status
    else:
        strCanSeeMarketPrice_Status = "OK"
        dictHomeTestStatus[Sv.CAN_SEE_MARKET_PRICE] = strCanSeeMarketPrice_Status
    
    
def runTest(driver):
    
    write("runTest : Start");
    
    canSeeMarketPrice(driver)
    
    write("runTest : End : "+str(dictHomeTestStatus))
    
    return dictHomeTestStatus
    
    
    
    
    

        