from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm:
    def setup_method(self):
        # Настройки для обхода защиты от автоматизации
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_form_validation(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        wait = WebDriverWait(self.driver, 10)

        # Заполняем поля через aria-label
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[aria-label='Имя']")
        )).send_keys("Иван")

        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Фамилия']").send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Address']").send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='E-mail']").send_keys("test@skypro.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Phone number']").send_keys("+7985899998787")
        # Zip code пропускаем
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='City']").send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Country']").send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Job position']").send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Company']").send_keys("SkyPro")

        # Прокручиваем и нажимаем Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        submit_btn.click()

        # Ожидаем появления сообщений об ошибках
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-danger")))

        # Находим Zip code по aria-label
        zip_code = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Почтовый индекс']")
        assert "error" in zip_code.get_attribute("class")

        # Проверяем остальные поля на зелёный цвет
        success_fields = [
            "Имя", "Фамилия", "Address", "E-mail",
            "Phone number", "City", "Country", "Job position", "Company"
        ]
        for field in success_fields:
            element = self.driver.find_element(By.CSS_SELECTOR, f"input[aria-label='{field}']")
            assert "success" in element.get_attribute("class")
            