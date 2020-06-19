from behave import *

from src.main import main

use_step_matcher("re")


@given("I open the application")
def step_impl(context):
    pass


@when("I search for (?P<File_a>.+) , (?P<File_b>.+) , (?P<Dir_a>.+) and (?P<Dir_b>.+)")
def step_impl(context, File_a, File_b, Dir_a, Dir_b):
    main(path='C:\\', file_a=File_a, file_b=File_b, dir_a=Dir_a, dir_b=Dir_b)


@when("I run search according to mission statement")
def step_impl(context):
    main(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')


@then('I validate that the search output csv file has the following attributes "(?P<Columns>.+)"')
def step_impl(context, Columns):
    with open('file_list.csv', 'r') as file:
        data = file.readline()
        data = data.replace('\n', '')
        for cvs_at in data.split(','):
            assert cvs_at in Columns


@step('I validate that the search output csv file has the following text "(?P<Text>.+)"')
def step_impl(context, Text):
    with open('file_list.csv', 'r') as file:
        data = file.read()
        assert Text in data
