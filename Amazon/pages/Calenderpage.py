from pages.webgeneric import WebGeneric



class Calender_page(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.day="//*[@name='birthday_day']"
        self.month="//*[@name='birthday_month']"
        self.year="//*[@name='birthday_year']"
        global wb
        wb=WebGeneric(driver)

    def select_dae(self):
        self.select_val("xpath",self.day,"8")

    def select_month(self):
        self.select_index("xpath",self.month,"4")

    def select_year(self):
        self.select_visible_text("xpath",self.year,"1990")
