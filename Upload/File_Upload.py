from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//input[@id='email']").send_keys('alekya.cool@gmail.com')
driver.find_element_by_xpath("//input[@id='pass']").send_keys('A@9177389863')
driver.find_element_by_id("loginbutton").click()
driver.find_element_by_name("composer_photo[]").send_keys("/Users/alekya/Desktop/Flower.jpg")
driver.find_element_by_xpath("//button[@type='submit']/child::div").click()
time.sleep(5)
#driver.switch_to.alert().accept()

driver.close()