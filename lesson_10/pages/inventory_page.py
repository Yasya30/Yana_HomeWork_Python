from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Класс для работы со страницей каталога товаров"""

    def __init__(self, driver):
        """
        Инициализация страницы каталога

        Args:
            driver (webdriver): Экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name: str):
        """
        Добавить товар в корзину по его названию

        Args:
            item_name (str): Название товара

        Returns:
            InventoryPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        ).click()
        return self

    def go_to_cart(self):
        """
        Перейти в корзину

        Returns:
            InventoryPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self
    