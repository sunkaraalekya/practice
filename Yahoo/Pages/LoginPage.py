from TestData import XLutils
import time
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.Username="login-username"

    def UserName(self):
        path = "/Users/alekya/Desktop/Yahoo.xlsx"
        rows = XLutils.getRowCount(path, 'Login')
        for r in range(2,rows+1):
            Username=XLutils.readData(path,'Login',r,1)
            time.sleep(5)
            self.driver.find_element_by_id(self.Username).send_keys(Username)
            time.sleep(5)


