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

class FindCarPage(object):
    def __write(self, strWrite):
        print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)
    
    def __runTheFilter(self, driver):
        self.__write("__runTheFilter : Starts");
    
        self.__write("__runTheFilter : Randomly start test 3 times"); #can't validate location. 
        
        counterRunTheFilter = 0
        
        dictRunTheFilter={}
        
        try:
            while(counterRunTheFilter < 3) :
                self.__write("__runTheFilter : counter #"+str(counterRunTheFilter)+" : "+Sv.FIND_OPTION_BRAND)
                
                if(counterRunTheFilter > 0):
                    self.__write("__runTheFilter : TEST ")
                    driver.find_element(By.XPATH, "//li/a[@class='gradient_button reset']").click()
                
                time.sleep(3)
               
                strBrand = self.__getFilterValue(Sv.FIND_OPTION_BRAND, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strTransmission = self.__getFilterValue(Sv.FIND_OPTION_TRANSMISSION, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strLocation = self.__getFilterValue(Sv.FIND_OPTION_LOCATION, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strScore = self.__getFilterValue(Sv.FIND_OPTION_SCORE, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strPrice = self.__getFilterValue(Sv.FIND_OPTION_PRICE, driver, dictRunTheFilter)
                
                dictRunTheFilter[strBrand] = strTransmission+"||"+strLocation+"||"+strScore+"||"+strPrice
                
                counterRunTheFilter=counterRunTheFilter+1
                
                time.sleep(3)
        except Exception as exp:
            strExceptionMsg = "__runTheFilter : Error : ", str(exp)
            self.__write("__runTheFilter : Error : "+str(exp))
            raise strExceptionMsg
        
        except utilCommon.MyError as mE :
            strError = "__runTheFilter : Error : ", str(mE)
            raise utilCommon.MyError(strError)
            
               
        self.__write("__runTheFilter : Result Validation : All result should contain the car brand Name or based on the first chosen filter.");
        
        
    def __getFilterValue(self, strChosenFilter, driver, dictRunTheFilter):
        
        try:
            self.__write("__getFilterValue : Start : "+strChosenFilter);
            
            strTempAttribute = driver.find_element(By.XPATH, "//select[@name='"+strChosenFilter+"']").get_attribute("sb")
            
            self.__write("__getFilterValue : 1 : "+strTempAttribute)
            
            driver.find_element(By.XPATH, "//a[@id='sbSelector_"+strTempAttribute+"']").click()
    
            listOfElement = driver.find_elements(By.XPATH, "//ul[@id='sbOptions_"+strTempAttribute+"']/li/a")
    
            if(strChosenFilter.lower()==Sv.FIND_OPTION_BRAND.lower()):
                strChosenValue = "Mazda"
#                 while True :
#                     strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")
#                     
#                     if(strChosenValue not in dictRunTheFilter):
#                         break
            else:
                strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")
    
            self.__write("__getFilterValue : 4 : "+strChosenValue)
                    
            driver.find_element(By.XPATH, "//ul[@id='sbOptions_"+strTempAttribute+"']/li/a[.='"+strChosenValue+"']").click()
            
            self.__write("__getFilterValue : Ends : Chosen Value : "+strChosenValue)
            
            return strChosenValue        
        
        except Exception as exp:
            strExceptionMsg = "__getFilterValue : Error : ", str(exp)
            self.__write("__getFilterValue : Error : "+str(exp))
            raise strExceptionMsg
        
        except utilCommon.MyError as mE :
            strError = "__getFilterValue : Error : ", str(mE)
            raise utilCommon.MyError(strError)



def runTest(driver):
    
    fcp = FindCarPage()
    
    fcp._FindCarPage__write("runTest : Start");
    
    time.sleep(1)
    driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/cari/']").click()
    
    fcp._FindCarPage__write("runTest : Run the Filter?");
    
    try:
        fcp._FindCarPage__runTheFilter(driver)
        
    except Exception as exp:
        strExceptionMsg = "runTest : Error : ", str(exp)
        fcp._FindCarPage__write("runTest : Error : "+str(exp))
        raise strExceptionMsg
    
    except utilCommon.MyError as mE :
        strError = "runTest : Error : ", str(mE)
        raise utilCommon.MyError(strError)
            
        
    
    fcp._FindCarPage__write("runTest : End : "+str(dictFindCarTestStatus))
    
    return dictFindCarTestStatus