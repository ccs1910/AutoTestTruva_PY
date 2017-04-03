'''
Created on Apr 3, 2017

@author: csantoso
'''

# if __name__ == '__main__':
#     pass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create a new Google Chrome Session

driver = webdriver.Chrome()
driver.implicitly_wait(30)
# driver.maximize_window()

driver.get("https://truva.id")


