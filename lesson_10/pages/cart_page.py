from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс для работы со страницей корзины"""

    def __init__(self, driver):
        """
        Инициализация страницы корзины

        Args:
            driver (webdriver): Экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        """
        Нажать кнопку оформления заказа (Checkout)

        Returns:
            CartPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(By.ID, "checkout").click()
        return self
    