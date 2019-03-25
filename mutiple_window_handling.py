from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
#driver.quit()
time.sleep(30)
driver.find_element_by_xpath("//span[text()='Login']").click()
parent_window=driver.current_window_handle
print(parent_window)
all_window=driver.window_handles
print(all_window)
print(type(all_window))
driver.switch_to.window(all_window[1])
# time.sleep(50)
driver.find_element_by_id("inputEmail").send_keys("alekya.cool@gmail.com")
driver.find_element_by_name("password").send_keys("1234")
# driver.find_element_by_class_name("recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox").click()
driver.find_element_by_id("login").click()

