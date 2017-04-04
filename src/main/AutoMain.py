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
    
    write("urlValidation : starts : Test Case : "+strTestCase)
    
    if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() :
        strURL_Path = Sv.HOME_URL_PATH
        
    elif strTestCase.lower() == Sv.FIND_TEST_CASE.lower() :
#         strURL_Path = str.join(Sv.HOME_URL_PATH, Sv.EXT_CARI_URL_PATH)

        strURL_Path = Sv.HOME_URL_PATH
        
    else:
        
        raise " Test Case Not Found"
# #         write("Not Found")
#         break
    
    write("urlValidation : Ends")
    
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

# Function to Execute Test Case

def executeCase(strTestCase, driver):
    
    strTestStatus = "Failed"
    write("executeCase : Start : Test Case : "+strTestCase)  
    
    dictOverallStatus = {}
    
    if strTestCase.lower() == Sv.HOME_TEST_CASE.lower() : 
        import modules.HomePage as HP
        
         
        try :
            dictOverallStatus = HP.runTest (driver)
            strTestStatus = "Test Completed"
        except Exception as exp :
            strTestStatus = "executeCase : Failed due to Error : ", str(exp)
            
            raise utilCommon.MyError(strTestStatus)
    else :
        
        raise utilCommon.MyError("executeCase : Failed : Test Case Not Found")
    
    utilCommon.printToFile(strTestStatus, strTestCase, dictOverallStatus);
    
    write("executeCase : End : "+strTestStatus)
    
    return strTestStatus
          

############################################# main code starts here! #################################################

# if __name__ == '__main__':
# create a new Google Chrome Session
write("main : starts")

strTestStatus = "Failed"

strTestCase = input("Please input Test Case (home/find/sell/how/about) : ")

write("main : Chosen Test Case : "+strTestCase)

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

write("main : Test Status : "+strTestStatus)


    
