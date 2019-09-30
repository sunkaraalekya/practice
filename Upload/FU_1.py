from selenium import webdriver
import Take_Screenshot
import time
driver=webdriver.Chrome()
driver.get("https://www.naukri.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@class='topIcon notify']").click()
CW=driver.window_handles
print(CW)
driver.switch_to.window(CW[1])
driver.find_element_by_xpath("//div[contains(text( ),'Login')]").click()
driver.find_element_by_id("usernameField").send_keys("alekya.sunkara48@gmail.com")
driver.find_element_by_id("passwordField").send_keys("A@9177389863")
driver.find_element_by_xpath("//button[contains(text( ),'Login')]").click()
driver.find_element_by_xpath("//a[contains(text( ),'UPDATE PROFILE')]").click()
driver.find_element_by_id("attachCV").send_keys("/Users/alekya/Desktop/Documents/Resume_Latest/AlekyaSunkara_Resume.pdf")
exe1=driver.find_element_by_xpath("//b[@title='AlekyaSunkara_Resume.pdf']")
#exe=driver.find_element_by_id("attachCV").get_attribute("value")
print(exe1.text)
if (exe1=="AlekyaSunkara_Resume.pdf - "):
    print("Uploaded Successfully")
else:
    print("Failed to Upload")


#driver.quit()
#driver.save_screenshot("/Users/alekya/Desktop/Documents/naukri.png")
#Take_Screenshot.TakeScreenshot(driver,"First1Screenshot")
