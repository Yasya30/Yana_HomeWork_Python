import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_form_validation(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        wait = WebDriverWait(self.driver, 10)

        first_name = wait.until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        first_name.send_keys("Иван")

        last_name = self.driver.find_element(By.ID, "lastName")
        last_name.send_keys("Петров")

        email = self.driver.find_element(By.ID, "userEmail")
        email.send_keys("ivan@test.com")

        gender = self.driver.find_element(
            By.XPATH, "//label[text()='Male']"
        )
        gender.click()

        mobile = self.driver.find_element(By.ID, "userNumber")
        mobile.send_keys("1234567890")
        mobile.send_keys("\n")

        success = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "modal-content")
            )
        )
        assert success.is_displayed()
