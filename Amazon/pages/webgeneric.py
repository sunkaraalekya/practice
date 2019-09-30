from selenium.webdriver.support.select import Select

from pages.locgeneric import Loc_generic


class WebGeneric(Loc_generic):
    def __init__(self,driver):
        Loc_generic.__init__(self,driver)
        global lc
        lc=Loc_generic(driver)

    def enter(self, locator_type, locator_val, input_val):
        e = self.locator(locator_type, locator_val)
        e.send_keys(input_val)

    def click(self, locator_type, locator_val):
        e = self.locator(locator_type, locator_val)
        e.click()

    def select_val(self,loc_type,loc_val,input_val):
        obj_d=Select(self.locator(loc_type,loc_val))
        obj_d.select_by_value(input_val)

    def select_index(self,loc_type,loc_val,input_val):
        obj_m=Select(self.locator(loc_type,loc_val))
        obj_m.select_by_index(input_val)

    def select_visible_text(self,loc_type,loc_val,input_val):
        obj_y=Select(self.locator(loc_type,loc_val))
        obj_y.select_by_visible_text(input_val)