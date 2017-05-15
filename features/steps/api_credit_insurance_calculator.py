'''
Created on May 15, 2017

@author: buherman
'''

from behave import *
import requests

@given('I pick {field_value} as {field_name} AJAX parameter')
def step_impl(context, field_name, field_value):
    if (hasattr(context, 'ajax_params')):
        context.ajax_params[field_name] = field_value
    else:
        context.ajax_params = { field_name: field_value }

@when('I submit an AJAX request with action {action}')
def step_impl(context, action):
    url = 'https://truva.id/wp-admin/admin-ajax.php'
    payload = { 'action': action }
    if (hasattr(context, 'ajax_params')):
        payload.update(context.ajax_params)
    context.response = requests.post(url, payload)
    print(context.response)

@then('I receive a plain text response {text}')
def step_impl(context, text):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    print('Actual response text = {:s}'.format(context.response.text))
    assert context.response.text == text

@then('I receive a JSON response')
def step_impl(context):
    print('Actual status code = {:d}'.format(context.response.status_code))
    assert context.response.status_code == 200
    context.response_json = context.response.json()

@then('JSON field {field_name} is equal to {field_value}')
def step_impl(context, field_name, field_value):
    actual = context.response_json[field_name]
    print('Actual {:s} = {:s}'.format(field_name, actual))
    assert actual == field_value
