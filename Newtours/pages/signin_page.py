class Signin:
    def __init__(self,driver):
        self.driver=driver
        self.sign_off_link="//*[text()='SIGN-OFF']"
        self.signin_username_txt_bx="userName"
        self.signin_pwd_txt_bx="password"
        self.signin_btn="login"

    def click_on_signoff(self):
        self.driver.find_element_by_xpath(self.sign_off_link).click()

    def enter_username(self):
        self.driver.find_element_by_name(self.signin_username_txt_bx).send_keys("Alekya")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.signin_pwd_txt_bx).send_keys("A@9177")

    def click_on_signin(self):
        self.driver.find_element_by_name(self.signin_btn).click()
