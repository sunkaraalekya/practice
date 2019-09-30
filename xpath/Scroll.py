from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://azure.microsoft.com/en-us/")
driver.implicitly_wait(30)
driver.maximize_window()
# Case1
# driver.execute_script("window.scrollBy(0,1000)","")
ele=driver.find_element_by_xpath("//h3[text()='DevOps']")
# Case2
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# Case 3
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")