class Register:
    def __init__(self,driver):
        self.driver=driver
        self.reg_link="//*[text()='REGISTER']"
        self.fn_txt_bx="firstName"
        self.ln_txt_bx="lastName"
        self.phone_txt_bx="phone"
        self.email_txt_bx="userName"
        self.address_txt_bx="address1"
        self.address1_txt_bx="address2"
        self.city_txt_bx="city"
        self.state_txt_bx="state"
        self.pst_code_txt_bx="postalCode"
        self.country_drpdwn="country"
        self.country_val="//option[@value='92']"
        self.un_txt_bx="email"
        self.pwd_txt_bx="password"
        self.confirmpwd_txt_bx="confirmPassword"
        self.submit_btn="register"
        # self.signin_btn="//*[text()='sign-in']"

    def click_on_reglink(self):
        self.driver.find_element_by_xpath(self.reg_link).click()

    def enter_fn(self):
        self.driver.find_element_by_name(self.fn_txt_bx).send_keys("Alekya")

    def enter_ln(self):
        self.driver.find_element_by_name(self.ln_txt_bx).send_keys("Sunkara")

    def enter_phone(self):
        self.driver.find_element_by_name(self.phone_txt_bx).send_keys("9876787653")

    def enter_email(self):
        self.driver.find_element_by_name(self.email_txt_bx).send_keys("abc@gmail.com")

    def enter_address(self):
        self.driver.find_element_by_name(self.address_txt_bx).send_keys("Jayanagar 9th block")

    def enter_address1(self):
        self.driver.find_element_by_name(self.address1_txt_bx).send_keys("svc")

    def enter_city(self):
        self.driver.find_element_by_name(self.city_txt_bx).send_keys("bangalore")

    def enter_state(self):
        self.driver.find_element_by_name(self.state_txt_bx).send_keys("karnataka")

    def enter_pstcode(self):
        self.driver.find_element_by_name(self.pst_code_txt_bx).send_keys("500069")

    def enter_country(self):
        self.driver.find_element_by_name(self.country_drpdwn).click()

    def enter_country_value(self):
        self.driver.find_element_by_xpath(self.country_val).click()

    def enter_un(self):
        self.driver.find_element_by_name(self.un_txt_bx).send_keys("Alekya")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_txt_bx).send_keys("A@9177")

    def enter_confirmpwd(self):
        self.driver.find_element_by_name(self.confirmpwd_txt_bx).send_keys("A@9177")

    def click_on_submit_btn(self):
        self.driver.find_element_by_name(self.submit_btn).click()

    # def click_on_signin_link(self):
    #     self.driver.find_element_by_xpath(self.signin_btn).click()








