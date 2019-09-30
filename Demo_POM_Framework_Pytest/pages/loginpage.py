class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.un_txt_bx_name='email'
        self.pwd_txt_bx_name='pass'
        self.login_btn_name='loginbutton'

    def enter_un(self):
        self.driver.find_element_by_name(self.un_txt_bx_name).send_keys("alekya.cool@gmail.com")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_txt_bx_name).send_keys("A@9177389863")

    def click_on_login(self):
        self.driver.find_element_by_id(self.login_btn_name).click()

