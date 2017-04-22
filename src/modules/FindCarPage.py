'''
Created on Apr 3, 2017

@author: csantoso
'''
import os
import datetime
import time

from selenium.webdriver.common.by import By

import utility.StaticVariable  as Sv
import utility.Common as utilCommon
from builtins import str


dictFindCarTestStatus = {}

class FindCarClass(object):
    def __write(self, strWrite):
        print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)
    
    def __runTheFilter(self, driver):
        self.__write("__runTheFilter : Starts");
    
        self.__write("__runTheFilter : Randomly start test 3 times"); #can't validate location. 
        
        counterRunTheFilter = 0
        
        dictRunTheFilter={}
        
        try:
            while(counterRunTheFilter < 2) :
                self.__write("__runTheFilter : counter #"+str(counterRunTheFilter)+" : "+Sv.FIND_OPTION_BRAND)
                
                if(counterRunTheFilter > 0):
#                     self.__write("__runTheFilter : TEST ")
                    driver.find_element(By.XPATH, "//li/a[@class='gradient_button reset']").click()  #reset the filter to run 2nd test
                
                time.sleep(2)
               
                strBrand = self.__getFilterValue(Sv.FIND_OPTION_BRAND, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strTransmission = self.__getFilterValue(Sv.FIND_OPTION_TRANSMISSION, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strLocation = self.__getFilterValue(Sv.FIND_OPTION_LOCATION, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strScore = self.__getFilterValue(Sv.FIND_OPTION_SCORE, driver, dictRunTheFilter)
                
                time.sleep(3)
                
                strPrice = self.__getFilterValue(Sv.FIND_OPTION_PRICE, driver, dictRunTheFilter)
                
#                 dictRunTheFilter[strBrand] = strTransmission+"||"+strLocation+"||"+strScore+"||"+strPrice
                
                counterRunTheFilter=counterRunTheFilter+1
                
                time.sleep(3)
                
                self.__write("__runTheFilter : Test #"+str(counterRunTheFilter)+" : Validation : Start")
                
                self.__doValidation(strBrand, strTransmission, strLocation, strScore, strPrice, driver)
                
                self.__write("__runTheFilter : Test #"+str(counterRunTheFilter)+" : Validation : End")
                
                time.sleep(2)
        except Exception as exp:
            strExceptionMsg = "__runTheFilter : Error : ", str(exp)
            self.__write("__runTheFilter : Error : "+str(exp))
            raise strExceptionMsg
        
        except utilCommon.MyError as mE :
            strError = "__runTheFilter : Error : ", str(mE)
            raise utilCommon.MyError(strError)
            
               
#         self.__write("__runTheFilter : Result Validation : All result should contain the car brand Name or based on the first chosen filter.");
        
        
    #Added Validation by Christian 19-April-2017        
    def __doValidation(self, strBrand, strTransmission, strLocation, strScore, strPrice, driver):
        self.__write("__doValidation : Start : "+strBrand);
        
        listOfElements = driver.find_elements(By.XPATH, "//div[@class='inventory_box car_listings boxed boxed_full']/div[@class='col-lg-3 col-md-4 col-sm-6 col-xs-12']")
        
        intTotalResult = len(listOfElements)
        
        self.__write("__doValidation : Total Result Page 1 : "+str(intTotalResult))
        
        strKey= strBrand+"||"+strTransmission+"||"+strLocation+"||"+strScore+"||"+strPrice
        
        if(intTotalResult==0):
            
            dictFindCarTestStatus[strKey] = Sv.STATUS_FAILED+" : TotalResult="+str(intTotalResult)
        
        else:
            strStatus = Sv.STATUS_SUCCESS
            counter = 1
            for item in listOfElements :
                 
                if(strBrand.upper().startswith("SEMUA")):
                    self.__write("__doValidation : Skip : "+strBrand) 
                    strStatus=strStatus+" : Brand=Validation_Skipped"
                else :
                    strResultBrand = item.find_element(By.XPATH, "//div[@class='auto-thumb__title']").get_attribute("data-brand")
                    self.__write("__doValidation : getBrand : "+strResultBrand)
                    
                    if(strResultBrand!=strBrand):
                        strStatus=strStatus+" : Brand=NOK"
                 
                 
                if(strScore.upper().startswith("SEMUA")):
                    self.__write("__doValidation : Skip : "+strScore) 
                    strStatus=strStatus+" : Score=Validation_Skipped"
                else :
                    strResultScore = item.find_element(By.XPATH, "//div[@class='auto-thumb__score']").get_attribute('innerHTML')
                    self.__write("__doValidation : getScore : "+strResultScore)
                
                    
                    self.__write("__doValidation : getScore : "+strResultScore.strip("<span class=\"max\">&nbsp;/&nbsp;5</span>"))
                    
                    floatResultScore = float(strResultScore.strip("<span class=\"max\">&nbsp;/&nbsp;5</span>"))
                    
                    self.__write(str(floatResultScore))
                    
                    floatChosenScore = float(strScore.replace("> ",""))
                    if(floatResultScore<floatChosenScore):
                        strStatus=strStatus+" : Score=NOK"
                        
                if(strPrice.upper().startswith("SEMUA")):
                    self.__write("__doValidation : Skip : "+strPrice) 
                    strStatus=strStatus+" : Price=Validation_Skipped"
                else:
                    strResultPrice = item.find_element(By.XPATH, "//div[@class='auto-thumb__price']").get_attribute('innerHTML')
                    self.__write("__doValidation : getPrice : "+strResultPrice)
                    
#                     Parse Price from String to int
                    intResultPrice = int(strResultPrice.strip().replace(".","").strip("Rp"))
                    intChosenPrice = int(strPrice.replace("< ","").replace(".","").strip("Rp"))
                    
                    if(intResultPrice>intChosenPrice):
                        strStatus=strStatus+" : Price=NOK"
                        
                        
                if(strTransmission.upper().startswith("SEMUA")):
                    self.__write("__doValidation : Skip : "+strTransmission)
                    strStatus=strStatus+" : Transmission=Validation_Skipped"
                else:
                    strResultTransmission = item.find_element(By.XPATH,"//table/tbody/tr/td[2]").get_attribute("title")
                    self.__write("__doValidation : getTransmission : "+strResultTransmission)
                    
                    if(strTransmission not in strResultTransmission) :
                        strStatus=strStatus+" : Transmission=NOK"
                       
                       
                        
                if(strLocation.upper().startswith("SEMUA")):
                    self.__write("__doValidation : Skip : "+strLocation)
                    strStatus=strStatus+" : Location=Validation_Skipped"
                else:
                    strResultLocation = item.find_element(By.XPATH,"//table/tbody/tr/td[2]").get_attribute("title")
                    self.__write("__doValidation : getLocation : "+strResultLocation)
                    
                    if(strResultLocation!=strLocation):
                        strStatus=strStatus+" : Location=NOK"
                     
                
                dictFindCarTestStatus[strKey+"||#"+str(counter)+"/"+str(intTotalResult)]=strStatus
                counter=counter+1
                
#             dictFindCarTestStatus[strKey]=strStatus
            self.__write(str(dictFindCarTestStatus))
                    
        
    def __getFilterValue(self, strChosenFilter, driver, dictRunTheFilter):
        
        try:
            self.__write("__getFilterValue : Start : "+strChosenFilter);
            
            strTempAttribute = driver.find_element(By.XPATH, "//select[@name='"+strChosenFilter+"']").get_attribute("sb")
            
#             self.__write("__getFilterValue : 1 : "+strTempAttribute)
            
            driver.find_element(By.XPATH, "//a[@id='sbSelector_"+strTempAttribute+"']").click()
    
            listOfElement = driver.find_elements(By.XPATH, "//ul[@id='sbOptions_"+strTempAttribute+"']/li/a")
    
            if(strChosenFilter.lower()==Sv.FIND_OPTION_BRAND.lower()):
                while True :
                    strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")
                     
                    if(strChosenValue not in dictRunTheFilter and strChosenValue.lower()!=Sv.FIND_OPTION_BRAND_SEMUA.lower()):
                        break
            else:
                strChosenValue = utilCommon.getRandomElementValue(listOfElement, 0).get_attribute("text")
    
#             self.__write("__getFilterValue : 4 : "+strChosenValue)
            
            time.sleep(2) #apparently sleep needed to wait for the value to be displayed.
                    
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
    
    fcp = FindCarClass()
    
    fcp._FindCarClass__write("runTest : Start");
    
    time.sleep(1)
    
#     driver.implicitly_wait(3)
    driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav pull-right']//a[@href='/cari/']").click()
    
    fcp._FindCarClass__write("runTest : Run the Filter?");
    
    try:
        fcp._FindCarClass__runTheFilter(driver)
        
    except Exception as exp:
        strExceptionMsg = "runTest : Error : ", str(exp)
        fcp._FindCarClass__write("runTest : Error : "+str(exp))
        raise strExceptionMsg
    
    except utilCommon.MyError as mE :
        strError = "runTest : Error : ", str(mE)
        raise utilCommon.MyError(strError)
            
        
    
    fcp._FindCarClass__write("runTest : End : "+str(dictFindCarTestStatus))
    
    return dictFindCarTestStatus