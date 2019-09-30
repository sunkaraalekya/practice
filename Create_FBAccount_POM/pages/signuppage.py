import testdata.constants as Dataval
class signup:
    def __init__(self,driver):
        self.driver=driver
        self.fn_txt_bx_name="firstname"
        self.sn_txt_bx_name="lastname"
        self.mob_num_ea_bx_name="reg_email__"
        self.np_txt_bx_name="reg_passwd__"
        self.day_drpdown="birthday_day"
        self.day_value="//*[text()='8']"
        self.month_drpdown="birthday_month"
        self.yr_drpdown="birthday_year"
        self.gender_rb="sex"
        self.sign_up_btn="//*[text()='Sign Up']"

    def enter_fn(self):
        self.driver.find_element_by_name(self.fn_txt_bx_name).send_keys("Alekya")

    def enter_sn(self):
        self.driver.find_element_by_name(self.sn_txt_bx_name).send_keys("Sunkara")

    def enter_mob_num(self):
        self.driver.find_element_by_name(self.mob_num_ea_bx_name).send_keys(Dataval.MOBILENO)

    def enter_reg_pwd(self):
        self.driver.find_element_by_name(self.np_txt_bx_name).send_keys(Dataval.PWD)

    def enter_dae(self):
        self.driver.find_element_by_name(self.day_drpdown).click()

    def enter_day_val(self):
        self.driver.find_element_by_xpath(self.day_value).click()

    def enter_month(self):
        self.driver.find_element_by_name(self.month_drpdown).send_keys("Apr")

    def enter_yr(self):
        self.driver.find_element_by_name(self.yr_drpdown).send_keys("1990")

    def select_gender(self):
        self.driver.find_element_by_name(self.gender_rb).click()

    def click_on_sign_up_btn(self):
        self.driver.find_element_by_xpath(self.sign_up_btn).click()








