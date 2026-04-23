from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс для работы со страницей авторизации"""
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализация страницы авторизации

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открытие страницы авторизации

        Returns:
            LoginPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str):
        """
        Выполнение авторизации с указанными учётными данными

        Args:
            username: Имя пользователя
            password: Пароль

        Returns:
            LoginPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return self
    