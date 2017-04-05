'''
Created on Apr 3, 2017

@author: csantoso
'''
import os
import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utility.StaticVariable  as Sv
import utility.Common as utilCommon


dictFindCarTestStatus = {}


class HomePage(object):
    def __write(self,strWrite):
        print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)
    
    
    def __uniqueSelectOption (self,strSelected, wait, driver, dictCarTrueValue) :
        self.__write("__uniqueSelectOption : Starts : Option : "+strSelected)
        
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
        
        self.__write("__uniqueSelectOption : Ends : Selected Item : "+strSelectedItem)
        
        return strSelectedItem
            
          
            
    def __commonSelectOption (self, strSelected, wait, driver):
        self.__write("__commonSelectOption : Starts : Option : "+strSelected)
        
        while True :
            webElementContainer = driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']")
            
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
        
    #     __write("__commonSelectOption : Element Size : "+str(len(listElementOptions)))
        
        strSelectedItem = utilCommon.getRandomElementValue(listElementOptions, 1).get_attribute('text')
        
        driver.find_element(By.XPATH,"//select[@id='"+strSelected+"']/option[.='"+strSelectedItem+"']").click()
        
        self.__write("__commonSelectOption : Ends : Selected Item : "+strSelectedItem)
        
        return strSelectedItem
             
      
    def __canSeeMarketPrice(self, driver) :
            
        self.__write("__canSeeMarketPrice : Starts")
        
        strCanSeeMarketPrice_Status = Sv.STATUS_NOK;
        
        wait = WebDriverWait(driver,10)
        
        self.__write("__canSeeMarketPrice : Run the Test 3 times ")
        
        dictCarTrueValue = {}
        
        counterCarTrueValue = 0
        
        
        while(counterCarTrueValue < 3) :
                    
            strValue = ""
            
            # Deciding Choose Brand        
    #         __write("__canSeeMarketPrice : Choose Brand ")
            strKey = self.__uniqueSelectOption(Sv.MARKET_PRICE_OPTION_BRAND, wait, driver, dictCarTrueValue)
                             
            #         Decide Choose Model
    #         __write("__canSeeMarketPrice : Choose Model ")
            strValue=strValue+"||"+self.__commonSelectOption(Sv.MARKET_PRICE_OPTION_MODEL, wait, driver)
    
    
            #         Decide Choose YEAR
    #         __write("__canSeeMarketPrice : Choose YEAR ")        
            strValue=strValue+"||"+self.__commonSelectOption(Sv.MARKET_PRICE_OPTION_YEAR, wait, driver)
    
    
            #         Decide Choose Variant
    #         __write("__canSeeMarketPrice : Choose Variant ")        
            strValue=strValue+"||"+self.__commonSelectOption(Sv.MARKET_PRICE_OPTION_VARIANT, wait, driver)
            
            #        get Min & MAx Price
            time.sleep(1) #wait for value to be loaded
            strValue=strValue+"|| min : "+ driver.find_element(By.XPATH,"//span[@id='tm-value-meter__min-tick']").get_attribute('innerHTML')
            strValue=strValue+"|| max : "+ driver.find_element(By.XPATH,"//span[@id='tm-value-meter__max-tick']").get_attribute('innerHTML')        
             
            dictCarTrueValue[strKey] = strValue  
            
            counterCarTrueValue = counterCarTrueValue + 1
            
            time.sleep(2) #wait for value to be loaded
                
        self.__write("__canSeeMarketPrice : Crawl Result : "+str(dictCarTrueValue))
        
    #     Validation
        self.__write("__canSeeMarketPrice : Start Validation : ensure No Value in dictionary is not empty")
        
        counterWrong = 0
        for key, value in dictCarTrueValue.items():
            if ((value == "temporary") | (value is None)) :
                counterWrong = counterWrong + 1
            else :
    #             print("min : ",value[value.index("|| min : "):value.index("|| max : ")].split(' ')[3])
    #             print("max : ",value[value.index("|| max : "):].split(' ')[3])
                if(value[value.index("|| min : "):value.index("|| max : ")].split(' ')[3] is None) | (value[value.index("|| min : "):value.index("|| max : ")].split(' ')[3]=="") | (value[value.index("|| max : "):].split(' ')[3] is None) | (value[value.index("|| max : "):].split(' ')[3]==""):
                    counterWrong = counterWrong + 1
                    
            
        if (counterWrong > 0 ):
            dictFindCarTestStatus[Sv.CAN_SEE_MARKET_PRICE] = strCanSeeMarketPrice_Status
        else:
            strCanSeeMarketPrice_Status = Sv.STATUS_OK
            dictFindCarTestStatus[Sv.CAN_SEE_MARKET_PRICE] = strCanSeeMarketPrice_Status
    
    
def runTest(driver):
    
    hp = HomePage()
    
    hp._HomePage__write("runTest : Start");
    
    hp._HomePage__write("runTest : Can See Market Price?");
    hp._HomePage__canSeeMarketPrice(driver)
    
    hp._HomePage__write("runTest : End : "+str(dictFindCarTestStatus))
    
    return dictFindCarTestStatus
    
    
    
    
    

        