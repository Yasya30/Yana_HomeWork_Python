import allure
import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Тест калькулятора с задержкой")
    @allure.description("Проверка работы калькулятора с задержкой 45 секунд (7+8=15)")
    def test_calculator(self):
        with allure.step("Открыть страницу калькулятора"):
            calc_page = CalculatorPage(self.driver)
            calc_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay("45")

        with allure.step("Нажать кнопки: 7 + 8 ="):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Проверить результат"):
            result = calc_page.get_result()
            assert result == "15", f"Ожидалось 15, получено {result}"
            