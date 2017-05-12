'''
Created on May 11, 2017

@author: csantoso
'''

"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.
before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.
before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
"""

# -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")

from selenium import webdriver
from utilities import static_variable as sv

import os
import datetime
import time

outFile = None

def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()
    
#     outFile = open("Status_"+datetime.datetime.now().strftime(sv.DATE_FORMAT_FILE)+".txt","w+")
    

def before_feature(context,feature):
#     outFile.write("Start")
    context.browser = webdriver.Chrome()
#     context.browser.get("https://truva.id")
    context.browser.get(sv.HOME_URL_PATH)
    
def after_feature(context,feature):
    context.browser.quit()
    
    
# def before_step(context, step):
    
def after_step(context, step):
    time.sleep(2)
