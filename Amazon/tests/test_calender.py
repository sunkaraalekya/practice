import time

from selenium import webdriver
from pages.Calenderpage import Calender_page
import pytest


@pytest.mark.usefixtures("test_setup")
class TestDrpDwn:
    def test_drp(self):
        driver = self.driver
        dd = Calender_page(driver)
        dd.select_dae()
        dd.select_month()
        dd.select_year()