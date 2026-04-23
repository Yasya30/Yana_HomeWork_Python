from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполнение формы заказа данными покупателя

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс

        Returns:
            CheckoutPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self) -> str:
        """
        Получение итоговой суммы заказа

        Returns:
            str: Текст итоговой суммы (например, "Total: $58.29")
        """
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total.text
    