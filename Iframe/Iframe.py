from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)
ele = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
#ele is a WebElement
driver.find_element_by_id("datepicker").click()
select_ele = driver.find_element_by_xpath("//select[@class='ui-datepicker-year']")
select_year = Select(select_ele)
select_year.select_by_value("2020")
select_month = Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-month']"))
select_month.select_by_visible_text("Mar")
e_d="17"
f_p="//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
s_p="]"
final_x=f_p+"'"+e_d+"'"+s_p
driver.find_element_by_xpath(final_x).click()

#from selenium.webdriver.support.select import Select

# "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()=""17""]"