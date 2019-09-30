from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
# element=driver.find_element_by_tag_name("a")
element=driver.find_elements_by_tag_name("a")
print(type(element))

b1=[]
w1=[]
# print(len(element))
for i in element:
    r=requests.head(i.get_attribute("href"))
    if r.status_code==200:
        w1.append(i.get_attribute("href"))
    else:
        b1.append(i.get_attribute("href"))
print("brokenlinks:",b1)
print("workinglinks:",w1)

    # print(i.get_attribute("href"))
