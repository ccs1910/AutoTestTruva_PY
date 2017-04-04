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

# Function to write logs
def write(strWrite):
    print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+" : "+os.path.basename(__file__)," : ",strWrite)
  
# Function to validate URL

def urlValidation(strTestCase):
    strURL_Path = ""
    
    write("urlValidation : starts : TestScripting Case : "+strTestCase)
    
    if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
        strURL_Path = Sv.HOME_URL_PATH
        
    elif strTestCase.lower() == Sv.FIND_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)

        strURL_Path = Sv.HOME_URL_PATH
        
    else:
        
        raise " TestScripting Case Not Found"
# #         write("Not Found")
#         break
    
    write("urlValidation : Ends : "+strURL_Path)
    
    return strURL_Path

# Use these for another test case. 
#     elif strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)
#     
#     elif strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)
#         
#     elif strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)    
#         
#     elif strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)
#     

# Function to Execute TestScripting Case

def executeCase(strTestCase, driver):
    
    strTestStatus = Sv.STATUS_FAILED
    write("executeCase : Start : TestScripting Case : "+strTestCase)  
    
    dictOverallStatus = {}
    
    if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() : 
        import modules.HomePage as HP
        
         
        try :
            dictOverallStatus = HP.runTest (driver)
            strTestStatus = Sv.STATUS_SUCCESS
        except Exception as exp :
            
            strTestStatus = Sv.STATUS_FAILED
            strExceptionMsg = "executeCase : Error : ", str(exp)
            
            raise utilCommon.MyError(strExceptionMsg)
    else :
        
        raise utilCommon.MyError("executeCase : TestScripting Case Not Found")
    
    utilCommon.printToFile(strTestStatus, strTestCase, dictOverallStatus);
    
    write("executeCase : End : "+strTestStatus)
    
    return strTestStatus
          

############################################# main code starts here! #################################################

# if __name__ == '__main__':
# create a new Google Chrome Session
write("main : starts")

strTestStatus = Sv.STATUS_FAILED

strTestCase = input("Please input TestScripting Case (home/find/sell/how/about) : ")

write("main : Chosen TestScripting Case : "+strTestCase)

strURL_Path = urlValidation(strTestCase)

write("main : Start the Chrome : Chosen URL path : "+strURL_Path)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.maximize_window()
driver.get(strURL_Path)

write("main : Execute : "+ strTestCase)

try : 
    strTestStatus = executeCase(strTestCase, driver)
except utilCommon.MyError as mE :
    
    write("main : Execute : "+strTestStatus+" :Error: "+str(mE))

driver.close()

write("main : TestScripting Status : "+strTestStatus)


    
