class Flight:
    def __init__(self,driver):
        self.driver=driver
        self.type_rbtn="//input[@value='oneway']"
        self.passengers_drpdwn="passCount"
        self.passengers_value="//option[@value='2']"
        self.departing_from_drpdwn="fromPort"
        self.date_on_month_drpdwn="fromMonth"
        self.date_on_day_drpdwn="fromDay"
        self.arriving_in_drpdwn="toPort"
        self.returning_month_drpdwn="toMonth"
        self.retunring_day_drpdwn="toDay"
        self.servclass_rbtn="//*[@value='Business']"
        self.airline_drpdwn="airline"
        self.continue_btn="findFlights"

    def choose_type(self):
        self.driver.find_element_by_xpath(self.type_rbtn).click()

    def select_passenger(self):
        self.driver.find_element_by_name(self.passengers_drpdwn).click()
        self.driver.find_element_by_xpath(self.passengers_value).click()

    def select_departing_from(self):
        self.driver.find_element_by_name(self.departing_from_drpdwn).send_keys("paris")

    def select_on(self):
        self.driver.find_element_by_name(self.date_on_month_drpdwn).send_keys("April")
        self.driver.find_element_by_name(self.date_on_day_drpdwn).send_keys("11")

    def select_arriving_in(self):
        self.driver.find_element_by_name(self.arriving_in_drpdwn).send_keys("London")

    def select_returning(self):
        self.driver.find_element_by_name(self.returning_month_drpdwn).send_keys("April")
        self.driver.find_element_by_name(self.retunring_day_drpdwn).send_keys("13")

    def select_services(self):
        self.driver.find_element_by_xpath(self.servclass_rbtn).click()

    def select_airline(self):
        self.driver.find_element_by_name(self.airline_drpdwn).send_keys("Pangea Airlines")

    def click_on_continue(self):
        self.driver.find_element_by_name(self.continue_btn).click()
