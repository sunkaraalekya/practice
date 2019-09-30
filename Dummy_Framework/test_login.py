from selenium import webdriver
import pytest

class TestLogin:
    @pytest.fixture(scope='session')
    def test_setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("http://localhost:8080/login?from=%2F")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_login(self,test_setup):
        driver.find_element_by_name("j_username").send_keys("admin")
        driver.find_element_by_name("j_password").send_keys("manager")
        driver.find_element_by_name("Submit").click()

    def test_logout(self,test_setup):
        driver.find_element_by_xpath("//*[text()='log out']").click()

