'''
Created on Apr 4, 2017

@author: csantoso
'''
import unittest
from unicodedata import decimal
from re import sub

import time

import locale


class Test(unittest.TestCase):


    def testName(self):
        print("i am testing the string and other python Script in here")
        
        start_time = time.clock()
         
        print("start : "+str(start_time))
        
        strTest = "< Rp50.000"
        print ("<span class=\"max\">&nbsp;/&nbsp;5</span>")
       
        
        print(strTest.replace("> ","").strip("Rp"))
        floatTest = int(strTest.replace("< ","").replace(".","").strip("Rp"))
        print(floatTest)
        

        time.sleep(3)
#         print("time : "+str(time.time()))
        
        print("prco : "+str(time.perf_counter()))
                
#         strExecutionTime = str(time.clock() - start_time)
        
#         print("test : "+ strExecutionTime)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    