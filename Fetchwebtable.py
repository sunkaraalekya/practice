from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///Users/alekya/pyworkspace/practice/xx.html")
driver.maximize_window()
driver.implicitly_wait(20)
ele=driver.find_element_by_xpath("//*[@id='t01']/tbody/tr")
# conv = print(ele.text)
val=len(ele.text)
# path=
for i in ele.text:

    driver.find_element_by_xpath("//*[@id='t01']/tbody/tr[i]").text