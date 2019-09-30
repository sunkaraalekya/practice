from selenium import webdriver
import pytest
from pages.signuppage import signup

@pytest.mark.usefixtures("test_setup")
class TestSignup:

    def test_sign_up(self):
        driver=self.driver
        sp=signup(driver)
        sp.enter_fn()
        sp.enter_sn()
        sp.enter_mob_num()
        sp.enter_reg_pwd()
        sp.enter_dae()
        sp.enter_day_val()
        sp.enter_month()
        sp.enter_yr()
        sp.select_gender()
        sp.click_on_sign_up_btn()