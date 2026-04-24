from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора

        Args:
            driver (webdriver): Экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        """
        Открыть страницу калькулятора в браузере

        Returns:
            CalculatorPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: str):
        """
        Установить задержку перед вычислением

        Args:
            seconds (str): Количество секунд задержки

        Returns:
            CalculatorPage: Экземпляр класса для цепочки вызовов
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button(self, button_text: str):
        """
        Нажать кнопку калькулятора

        Args:
            button_text (str): Текст на кнопке (например, "7", "+", "=")

        Returns:
            CalculatorPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()
        return self

    def get_result(self) -> str:
        """
        Получить результат вычисления

        Returns:
            str: Число на экране калькулятора
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result = self.driver.find_element(By.CLASS_NAME, "screen")
        return result.text
    