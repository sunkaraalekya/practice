from selenium.webdriver.support.select import Select
from testdata import constants as data
class Loc_generic:
    def __init__(self,driver):
        self.driver=driver

    def locator(self,loc_type,locator_val):
        try:
            if loc_type=="xpath":
                ele=self.driver.find_element_by_xpath(locator_val)

            elif loc_type=="name":
                ele=self.driver.find_element_by_name(locator_val)
            return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()

    # def select_drop_down(self,day_loc_type,day_loc_val,m_loc_type,m_loc_val,y_loc_type,y_loc_val):
    #     obj_d=Select(self.locator(self,day_loc_type,day_loc_val))
    #     obj_d.select_by_value(data.d_value)
    #     obj_m=Select(self.locator(self,m_loc_type,m_loc_val))
    #     obj_m.select_by_index(data.d_index)
    #     obj_y=Select(self.locator(self,y_loc_type,y_loc_val))
    #     obj_y.select_by_visible_text(data.d_year)


