from selenium import webdriver
from pages.homepage import Homepage
from pages.loginpage import Loginpage
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    # @pytest.fixture(scope='session')
    # def test_setup(self):
    #     global driver
    #     driver=webdriver.Chrome()
    #     driver.get("https://www.facebook.com/")
    #     driver.maximize_window()
    #     driver.implicitly_wait(30)
    #     yield
    #     driver.quit()

    def test_login(self):
        driver=self.driver
        lp=Loginpage(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login()

    def test_logout(self):
        driver=self.driver
        lp=Homepage(driver)
        lp.click_navigation_drpdwn()
        lp.click_logout_btn()

        # driver.find_element_by_id("userNavigationLabel").click()
        # driver.find_element_by_xpath("//*[text()='_54nh']").click()
