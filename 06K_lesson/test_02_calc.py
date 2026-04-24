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
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        wait = WebDriverWait(self.driver, 10)

        # Вводим задержку 45
        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидаем результат 15 (таймаут 60 секунд)
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        result = self.driver.find_element(By.CLASS_NAME, "screen")
        assert result.text == "15"
        