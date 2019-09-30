from TestData import XLUtils
import time
from selenium.webdriver.common.action_chains import ActionChains
class Login:
    #path = "/Users/alekya/Desktop/NaukriData.xlsx"
    def __init__(self,driver):
        self.driver=driver
        self.notify_btn="//*[@class='topIcon notify']"
        self.login_btn="//div[contains(text( ),'Login')]"
        self.Un_txt_bx="usernameField"
        self.Pwd_txt_bx="passwordField"
        self.l_btn="//button[contains(text( ),'Login')]"
        self.n_btn="//*[contains(text( ),'My Naukri')]"
        self.logout_btn="logout-gnb"


    def Login_Button(self):
        self.driver.find_element_by_xpath(self.notify_btn).click()
        CW = self.driver.window_handles
        print(CW)
        self.driver.switch_to.window(CW[1])
        self.driver.find_element_by_xpath(self.login_btn).click()

    def Un_Pwd_Button(self):
        path="/Users/alekya/Desktop/NaukriData.xlsx"
        rows=XLUtils.getRowCount(path,'Sheet1')
        time.sleep(5)
        for r in range(2,rows+1):
            Username=XLUtils.readData(path,'Sheet1',r,1)
            Pwd=XLUtils.readData(path,'Sheet1',r,2)
            self.driver.find_element_by_id(self.Un_txt_bx).send_keys(Username)
            self.driver.find_element_by_id(self.Pwd_txt_bx).send_keys(Pwd)
            self.driver.find_element_by_xpath(self.l_btn).click()
            time.sleep(5)
        if (self.driver.title=="Home | Mynaukri"):
            print("Test is passed")
            XLUtils.writeData(path,'Sheet1',r,3,"passed")
            act=ActionChains(self.driver)
            act.move_to_element(self.driver.find_element_by_xpath(self.n_btn)).perform()
            self.driver.find_element_by_class_name(self.logout_btn).click()
            time.sleep(5)
        else:
            print("Test Failed")
            XLUtils.writeData(path,'Sheet1',r,3,"Failed")


