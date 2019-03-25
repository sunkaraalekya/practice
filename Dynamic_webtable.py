from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///Users/alekya/pyworkspace/practice/xx.html")
driver.maximize_window()
driver.implicitly_wait(20)
ele=driver.find_element_by_xpath("//*[@id='t01']/tbody/tr")
d=len(ele)
print(d)
first="//table[@id='t01']/tbody/tr[
second=]"
  for i in d:
      driver.find_element_by_xpath(first+i+second).text