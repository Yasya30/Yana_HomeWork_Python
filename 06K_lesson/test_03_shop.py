from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShop:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_shopping_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(self.driver, 10)

        # Авторизация
        wait.until(EC.presence_of_element_located(
            (By.ID, "user-name")
        )).send_keys("standard_user")

        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Добавляем 3 товара
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items:
            self.driver.find_element(
                By.XPATH,
                f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
            ).click()

        # Переход в корзину
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Оформление заказа
        self.driver.find_element(By.ID, "checkout").click()

        # Заполнение данных
        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

        # Проверка итоговой суммы
        total = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text

        assert total == "Total: $58.29"
        