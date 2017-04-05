'''
Created on Apr 3, 2017

@author: csantoso
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import utility.StaticVariable  as Sv

import utility.Common as utilCommon

import os.path

import datetime


class AutoMain(object):
    
# Function to __write logs
    def __write(self,strWrite):
        print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)
  
# Function to validate URL

#     def __urlValidation(self,strTestCase):
#         strURL_Path = ""
#         
#         self.__write("__urlValidation : starts : Test Case : "+strTestCase)
#         
#         if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
#             strURL_Path = Sv.HOME_URL_PATH
#             
#         elif strTestCase.lower() == Sv.FIND_TEST_CASE.lower() :
#     #         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)
#     
#             strURL_Path = Sv.HOME_URL_PATH
#             
#         else:
#             
#             raise " Test Case Not Found"
#     # #         __write("Not Found")
#     #         break
#         
#         self.__write("__urlValidation : Ends : "+strURL_Path)
#         
#         return strURL_Path
    
       
    # Function to Execute TestScripting Case
    
    def __executeCase(self,strTestCase, driver):
        
        strTestStatus = Sv.STATUS_FAILED
        self.__write("__executeCase : Start : Test Case : "+strTestCase)  
        
        dictOverallStatus = {}
        
        if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() : 
            import modules.HomePage as HP
            
             
            try :
                dictOverallStatus = HP.runTest (driver)
                strTestStatus = Sv.STATUS_SUCCESS
            except Exception as exp :
                
                strTestStatus = Sv.STATUS_FAILED
                strExceptionMsg = "__executeCase : Error : ", str(exp)
                
                raise utilCommon.MyError(strExceptionMsg)
            
        elif strTestCase.lower() == Sv.FIND_TEST_CASE.lower() :
            import modules.FindCarPage as FCP
            
            try :
                dictOverallStatus = FCP.runTest (driver)
                strTestStatus = Sv.STATUS_SUCCESS
            except Exception as exp :
                
                strTestStatus = Sv.STATUS_FAILED
                strExceptionMsg = "__executeCase : Error : ", str(exp)
                
                raise utilCommon.MyError(strExceptionMsg) 
            
            except utilCommon.MyError as mE :
                
                strExceptionMsg = "__executeCase : Error : ", str(exp)
                
                raise utilCommon.MyError(strExceptionMsg) 
                          
        else :
            
            raise utilCommon.MyError("__executeCase : Test Case Not Found")
        
        utilCommon.printToFile(strTestStatus, strTestCase, dictOverallStatus);
        
        self.__write("__executeCase : End : "+strTestStatus)
        
        return strTestStatus
              
    
    ############################################# main code starts here! #################################################
    
    # create a new Google Chrome Session
if __name__ == '__main__':
#         am = AutoMain()
    
    am = AutoMain()
    am._AutoMain__write("main : starts")
    
    strTestStatus = Sv.STATUS_FAILED
    
    strTestCase = input("Please input Test Case (home/find/sell/how/about) : ")
    
    am._AutoMain__write("main : Chosen Test Case : "+strTestCase)
    
#     strURL_Path = am._AutoMain__urlValidation(strTestCase)
    
    am._AutoMain__write("main : Start the Chrome : Chosen URL path : "+Sv.HOME_URL_PATH)
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(Sv.HOME_URL_PATH)
    
    am._AutoMain__write("main : Execute : "+ strTestCase)
    
    try : 
        strTestStatus = am._AutoMain__executeCase(strTestCase, driver)
    except utilCommon.MyError as mE :
        
        am._AutoMain__write("main : Execute : "+strTestStatus+" :Error: "+str(mE))
    
#     driver.close()
    
    am._AutoMain__write("main : Test Status : "+strTestStatus)
    
    
        
