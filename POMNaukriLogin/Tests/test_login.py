from Pages.Loginpage import Login
from  selenium import webdriver
import pytest
@pytest.mark.usefixtures("test_setup")
class TestLogin:

    #@pytest.fixture(scope='session')
    #def test_setup(self):
        #global driver
        #driver= webdriver.Chrome()
        #driver.get("https://www.naukri.com")
        #driver.maximize_window()
        #driver.implicitly_wait(30)
        #yield
        #driver.quit()

    def test_login(self):
        driver=self.driver
        lp=Login(driver)
        lp.Login_Button()
        lp.Un_Pwd_Button()


