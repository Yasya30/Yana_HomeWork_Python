from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_form_validation(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        wait = WebDriverWait(self.driver, 10)

        # Заполняем форму
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']")
        )).send_keys("Иван")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']"
        ).send_keys("Петров")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='address']"
        ).send_keys("Ленина, 55-3")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']"
        ).send_keys("test@skypro.com")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='phone']"
        ).send_keys("+7985899998787")

        # Zip code пропускаем

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='city']"
        ).send_keys("Москва")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='country']"
        ).send_keys("Россия")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']"
        ).send_keys("QA")

        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='company']"
        ).send_keys("SkyPro")

        # Прокрутка и нажатие кнопки
        submit = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        # Ждем результатов валидации
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "alert-danger")
        ))

        # Проверка Zip code (должен быть с ошибкой)
        zip_code = self.driver.find_element(
            By.CSS_SELECTOR, "input[name='zip-code']"
        )
        assert "error" in zip_code.get_attribute("class")

        # Проверка остальных полей
        fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        for field in fields:
            element = self.driver.find_element(
                By.CSS_SELECTOR, f"input[name='{field}']"
            )
            assert "success" in element.get_attribute("class")
            