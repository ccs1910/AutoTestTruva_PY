'''
Created on Apr 3, 2017

@author: csantoso
'''

from abc import ABC, abstractmethod

class AbstractTestCase(ABC):
    
    def __init__(self, driver):
        self.driver = driver
        super(AbstractTestCase, self).__init__()

    @abstractmethod
    def runTest(self):
        return
        
        