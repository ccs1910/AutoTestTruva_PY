'''
Created on Apr 3, 2017

@author: csantoso
'''
import os
import datetime

import utility.StaticVariable as Sv

from random import randrange

class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


def write(strWrite):
    print(datetime.datetime.now().strftime(Sv.DATE_FORMAT_LOG)+" : "+os.path.basename(__file__)," : ",strWrite)


def getRandomElementValue(listValue, intMin):
    
#     write("getRandomElementValue : Size of ListValue :  "+str(len(listValue)))
    intIndex = randrange(intMin, len(listValue))
#     write("getRandomElementValue : Index Number :  "+str(intIndex))
    
    return listValue[intIndex]


def printToFile(strStatus, strTestCase, dictOverallStatus):
    
    write("printToFile : Result TestScripting Case : "+strTestCase.upper())
    
    try :
#         filepath = os.path.join('C:/Users/csantoso/AppData/Local/My Private Documents/001_tools/EclipsePortable/Data/workspace/PythonOutput',"Status_"+datetime.datetime.now().strftime(Sv.DATE_FORMAT_FILE)+".txt")
#         
#         if not os.path.exists('C:/Users/csantoso/AppData/Local/My Private Documents/001_tools/EclipsePortable/Data/workspace/PythonOutput'):
#             os.makedirs('C:/Users/csantoso/AppData/Local/My Private Documents/001_tools/EclipsePortable/Data/workspace/PythonOutput')
#         
#         outFile = open(filepath, "w+")
        
        outFile = open("Status_"+datetime.datetime.now().strftime(Sv.DATE_FORMAT_FILE)+".txt","w+")
        
        outFile.write(strStatus+" on "+datetime.datetime.now().strftime(Sv.DATE_FORMAT_LOG))
        outFile.write("\n")
        
        outFile.write("==========TestScripting Case : "+strTestCase+"==========")
        outFile.write("\n")
        
        for key, value in dictOverallStatus.items():
            outFile.write(key+" = "+value)
            outFile.write("\n")
    
        outFile.close()
    except Exception as exp :
        raise str(exp)

    