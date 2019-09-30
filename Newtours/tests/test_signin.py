import  pytest
from pages.registerpage import Register
from pages.signin_page import Signin
from pages.flightpage import Flight
import time

@pytest.mark.usefixtures("test_setup")
class Test_flight:

    def test_register(self):
        driver=self.driver
        rp=Register(driver)
        rp.click_on_reglink()
        rp.enter_fn()
        rp.enter_ln()
        rp.enter_phone()
        rp.enter_email()
        rp.enter_address()
        rp.enter_address1()
        rp.enter_city()
        rp.enter_state()
        rp.enter_pstcode()
        rp.enter_country()
        rp.enter_country_value()
        rp.enter_un()
        rp.enter_pwd()
        rp.enter_confirmpwd()
        rp.click_on_submit_btn()
        time.sleep(30)
        # rp.click_on_signin_link()

    def test_signin(self):
        driver=self.driver
        sp=Signin(driver)
        sp.click_on_signoff()
        sp.enter_username()
        sp.enter_pwd()
        sp.click_on_signin()

    def test_flight(self):
        driver=self.driver
        fp=Flight(driver)
        fp.choose_type()
        fp.select_passenger()
        fp.select_departing_from()
        fp.select_on()
        fp.select_arriving_in()
        fp.select_returning()
        fp.select_services()
        fp.select_airline()
        fp.click_on_continue()
