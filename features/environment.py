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

def before_feature(context,feature):
    context.config.setup_logging()
    
    context.browser = webdriver.Chrome()
    context.browser.get("https://truva.id")
#     context.browser.get(sv.HOME_URL_PATH)
    
    
    
    
        
def after_feature(context,feature):
    context.config.setup_logging()
    context.browser.quit()