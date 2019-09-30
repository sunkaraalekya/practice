from behave import *

use_step_matcher("re")

from selenium import webdriver
@given("user persent with loginpage")
def launch_browser():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


@when("enter username")
def user_name():
    driver.find_element_by_name("email").send_keys("alekya.cool@gmail.com")


@when("enter password")
def pwd():
    driver.find_element_by_name("pass").send_keys("Alu@9177389863")


@when("click on login")
def l_button():
    driver.find_element_by_id("loginbutton").click()

launch_browser()
user_name()
pwd()
l_button()
