'''
Created on May 29, 2017

@author: csantoso
'''
"""
Scenario: Querying list of car brands

    When I submit an AJAX request with action truva_market_get_all_brand
    Then I receive a JSON response containing a list of all car brands



Scenario: Querying list of car models from a random brand

    When I pick a random brand as the brand AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_model
    Then I receive a JSON response containing the list of car models



Scenario Outline: Querying list of car models from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_model
    Then I receive a JSON response containing the list of car models
    Examples:
        | brand    |
        | Toyota   |
        | Honda    |
        | Daihatsu |
        | Nissan   |
        | Ford     |



Scenario Outline: Querying list of car years from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_year
    Then I receive a JSON response containing the list of car years
    Examples:
        | brand    | model        |
        | Toyota   | Avanza       |
        | Daihatsu | Xenia        |
        | Honda    | Jazz         |
        | Nissan   | Grand Livina |
        | Isuzu    | New Panther  |



Scenario Outline: Querying list of car variants from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I pick <year> as year AJAX parameter
        And I submit an AJAX request with action truva_market_get_all_variant
    Then I receive a JSON response containing the list of car variants
    Examples:
        | brand      | model        | year |
        | Toyota     | Avanza       | 2014 |
        | Toyota     | Avanza       | 2010 |
        | Isuzu      | New Panther  | 2013 |
        | Mitsubishi | Pajero Sport | 2014 |
        | Suzuki     | Ertiga       | 2012 |



Scenario Outline: Querying price range from a specific parameter set

    When I pick <brand> as brand AJAX parameter
        And I pick <model> as model AJAX parameter
        And I pick <year> as year AJAX parameter
        And I pick <variant> as variant AJAX parameter
        And I submit an AJAX request with action truva_market_get_single_price
    Then I receive a JSON response containing the minimum and maximum price
    Examples:
        | brand      | model                | year | variant           |
        | Toyota     | Avanza               | 2014 | All New Veloz A/T |
        | Honda      | Civic                | 2007 | New 2.0 A/T       |
        | Honda      | Jazz                 | 2013 | RS A/T Facelift   |
        | Toyota     | Fortuner             | 2014 | 2.5 G Diesel TRD  |
        | Toyota     | Kijang Innova Bensin | 2010 | G A/T             |
"""


from behave import *
import requests
from utilities import common as utilCommon

# @when('I submit an AJAX request with action truva_market_get_all_brand')
# def step_impl(context):
#     pass

@when('I pick a random brand as the brand AJAX parameter')
def step_impl(context):
    brand_list = ['Audi', 'BMW', 'Chevrolet', 'Daihatsu', 'Dodge', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Kia', 'Lexus', 'Mazda', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Proton', 'Subaru', 'Suzuki', 'Toyota', 'Volkswagen']
    chosen_brand = utilCommon.getRandomElementValue(brand_list, 0)
    
    print("chosen brand :",chosen_brand)
    
    if (hasattr(context, 'ajax_params')):
        context.ajax_params['brand'] = chosen_brand
    else:
        context.ajax_params = { 'brand': chosen_brand }


@when('I pick {field_value} as {field_name} AJAX parameter')
def step_impl(context, field_name, field_value):
    if (hasattr(context, 'ajax_params')):
        context.ajax_params[field_name] = field_value
    else:
        context.ajax_params = { field_name: field_value }



@then('I receive a JSON response containing a list of all car brands')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()
    print('response : ',context.response_json)
    

@then('I receive a JSON response containing the list of car models')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()
    print('response : ',context.response_json)


@then('I receive a JSON response containing the list of car years')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()
    print('response : ',context.response_json)

@then('I receive a JSON response containing the list of car variants')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()
    print('response : ',context.response_json)

@then('I receive a JSON response containing the minimum and maximum price')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()
    print('response : ',context.response_json)



