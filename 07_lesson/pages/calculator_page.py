from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button(self, button_text):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()
        return self

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result = self.driver.find_element(By.CLASS_NAME, "screen")
        return result.text
    