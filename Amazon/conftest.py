import pytest
import testdata.constants as  Dataval
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    # chrome_options=webdriver.ChromeOptions()
    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='ff':
        driver=webdriver.Firefox()

    driver.get(Dataval.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()

































# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(30)
# time.sleep(30)
# driver.find_element_by_xpath("//span[@class='nav-line-2']").click()
# driver.find_element_by_name("email").send_keys("9177389863")
# driver.find_element_by_id("continue").click()
# driver.find_element_by_id("ap_password").send_keys("Alu@9177389863")
# driver.find_element_by_class_name("a-button-input").click()
# driver.find_element_by_xpath("//*[@href='/gp/site-directory?ref_=nav_shopall_btn']").click()
# driver.find_element_by_xpath("//*[@href='/headphones/b?ie=UTF8&node=1388921031&ref_=sd_allcat_sbc_tvelec_headphones' and contains(text(),'Headphones')]").click()
# cart=driver.find_element_by_xpath("//*[@id='100_dealView_0']/div/div[2]/div/div/div[9]/div/a/span/i/span")
# driver.execute_script("arguments[0].scrollIntoView();",cart)