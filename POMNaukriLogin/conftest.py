import pytest
import TestData.XLUtils
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default='chrome')

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    PROXY="localhost:1234"
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)


    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='ff':
        driver=webdriver.Firefox()

    driver.get("https://www.naukri.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()
