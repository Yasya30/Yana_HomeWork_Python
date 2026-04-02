,import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCalc:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_calculator(self):
        self.driver.get("https://www.calculator.net/")
        wait = WebDriverWait(self.driver, 10)

        buttons = ["1", "+", "2", "="]
        for btn in buttons:
            element = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{btn}']")
                )
            )
            element.click()

        result = wait.until(
            EC.presence_of_element_located(
                (By.ID, "sciOutPut")
            )
        )
        assert "3" in result.text