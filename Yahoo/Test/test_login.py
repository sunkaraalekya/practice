from Pages.LoginPage import Login
from  selenium import webdriver

import pytest
@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver=self.driver
        lp=Login(driver)
        lp.UserName()
