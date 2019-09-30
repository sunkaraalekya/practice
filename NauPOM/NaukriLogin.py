from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import Xutils
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.naukri.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@class='topIcon notify']").click()
CW=driver.window_handles
print(CW)
driver.switch_to.window(CW[1])
driver.find_element_by_xpath("//div[contains(text( ),'Login')]").click()
path="/Users/alekya/Desktop/NaukriData.xlsx"
rows=Xutils.getRowCount(path,'Sheet1')
time.sleep(5)
for r in range(2,rows+1):
    username=Xutils.readData(path,"Sheet1",r,1)
    pwd=Xutils.readData(path,"Sheet1",r,2)
    driver.find_element_by_id("usernameField").send_keys(username)
    driver.find_element_by_id("passwordField").send_keys(pwd)
    driver.find_element_by_xpath("//button[contains(text( ),'Login')]").click()
    time.sleep(5)
    if (driver.title=="Home | Mynaukri"):
        print("Testcase is passed")
        Xutils.writeData(path,'Sheet1',r,3,"Passed")
        act = ActionChains(driver)
        act.move_to_element(driver.find_element_by_xpath("//*[contains(text( ),'My Naukri')]")).perform()
        wait=WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable(By.CLASS_NAME,'logout-gnb')).click()

        #driver.find_element_by_class_name("logout-gnb").click()
        #time.sleep(5)
    else:

        print("Testcase is Failed")
        Xutils.writeData(path,'Sheet1',r,3,"Failed")




