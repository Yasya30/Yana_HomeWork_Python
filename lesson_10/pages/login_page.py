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
            driver (webdriver): Экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открыть страницу авторизации в браузере

        Returns:
            LoginPage: Экземпляр класса для цепочки вызовов
        """
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str):
        """
        Выполнить авторизацию с указанными учётными данными

        Args:
            username (str): Имя пользователя
            password (str): Пароль

        Returns:
            LoginPage: Экземпляр класса для цепочки вызовов
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return self
    