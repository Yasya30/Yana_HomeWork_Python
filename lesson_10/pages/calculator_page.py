from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        """
        Открытие страницы калькулятора

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: str):
        """
        Установка задержки перед вычислением

        Args:
            seconds: Количество секунд задержки

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button(self, button_text: str):
        """
        Нажатие на кнопку калькулятора

        Args:
            button_text: Текст на кнопке (цифра или оператор)

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()
        return self

    def get_result(self) -> str:
        """
        Получение результата вычисления

        Returns:
            str: Текст результата на экране калькулятора
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result = self.driver.find_element(By.CLASS_NAME, "screen")
        return result.text
    