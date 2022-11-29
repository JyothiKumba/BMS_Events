import time

from behave import *

from selenium import webdriver

@given('launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\LENOVO\Downloads\chromedriver_win32\chromedriver.exe')


@when('Open the BookMyShow browser')
def BookMyShow_Homepage(context):
    context.driver.get("https://in.bookmyshow.com/")
    context.driver.maximize_window()
    time.sleep(2)
    context.driver.implicitly_wait(30)


@then('Choose location')
def Choose_loc(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('//img[@alt="HYD"]').click()


@then('Click on Events Button')
def Event_btn(context):
    context.driver.find_element_by_xpath('//a[text()="Events"]').click()


@then('Click on Browser By Venue')
def click_on_browser(context):
    context.driver.find_element_by_xpath('(//div[text()="Browse by Venues"])[1]').click()


@then('Choose a Venue')
def click_on_VD(context):
    context.driver.find_element_by_xpath('(//button[text()="VIEW DETAILS"])[2]').click()


@then('Choose an Event')
def Stand_up(context):
    context.driver.find_element_by_xpath('//img[@alt="Vivek Samtani Live: A Stand-up Comedy Show"]').click()


@then('Click on book')
def Book(context):
    context.driver.find_element_by_xpath('//button[text()="Book"]').click()


@then('Choose a Location')
def click_on_Area(context):
    context.driver.find_element_by_xpath('//div[text()="Aaromale - Cafe & Creative Community: Hyderabad"]').click()


@then('Click on Add')
def Add_no_persons(context):
    context.driver.find_element_by_xpath('(//div[text()="Add"])[1]').click()


@then('Click on Proceed')
def proceed(context):
    context.driver.find_element_by_xpath('//button[text()="Proceed"]').click()


@then('Enter Name "{Name}"')
def Name(context,Name):
    context.driver.find_element_by_xpath('//input[@name="name"]').send_keys(Name)


@then('Enter Number "{Number}"')
def phone_no(context,Number):
    context.driver.find_element_by_xpath('//input[@name="primary_phoneNo"]').send_keys(Number)


@then('Enter Email "{Email}"')
def Email(context,Email):
    context.driver.find_element_by_xpath('//input[@name="primary_email"]').send_keys(Email)


@then('Click on checkbox1')
def checkbox1(context):
    context.driver.find_element_by_xpath('(//input[@type="checkbox"])[1]').click()

@then('Click on checkbox2')
def checkbox2(context):
    context.driver.find_element_by_xpath('(//input[@type="checkbox"])[2]').click()


@then('Click on submit')
def submit(context):
    context.driver.find_element("id",'registration-submit-button').click()


@then('Click on Login to Proceed')
def login_to_proceed(context):
    context.driver.find_element_by_xpath('//button[text()="Login to Proceed"]').click()


@then('Close Browser')
def Close_browser(context):
    context.driver.close()



