import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


class TestCalculator:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_calculator(self):
        calc_page = CalculatorPage(self.driver)
        calc_page.open()
        calc_page.set_delay("45")
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")
        result = calc_page.get_result()
        assert result == "15"
        