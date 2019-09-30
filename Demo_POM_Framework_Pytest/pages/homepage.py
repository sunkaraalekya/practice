class Homepage:
    def __init__(self,driver):
        self.driver=driver
        self.navigation_drpdwn='userNavigationLabel'
        self.logout_btn_name="//*[@class='_54nh']"

    def click_navigation_drpdwn(self):
        self.driver.find_element_by_id(self.navigation_drpdwn).click()

    def click_logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_btn_name).click()



