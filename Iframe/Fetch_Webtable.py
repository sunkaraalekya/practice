from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///Users/alekya/pyworkspace/practice/xx.html")
driver.maximize_window()
driver.implicitly_wait(20)
cell_val=driver.find_elements_by_xpath("//*[@id='t01']/tbody/tr")
# print(cell_val)

# converted = cell_val.text

for i in cell_val:
    print(i.text)