import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()
parent_window = driver.current_window_handle
print(parent_window)
all_window = driver.window_handles
print(all_window)
print(type(all_window))
#driver.switch_to.window(all_window[1])

for id in all_window:
    print(id)
    if parent_window != id:
        driver.switch_to.window(id)
        driver.find_element_by_id("inputEmail").send_keys("child window")
time.sleep(5)
driver.quit()