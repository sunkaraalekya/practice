import pytest
@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("https://login.yahoo.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()