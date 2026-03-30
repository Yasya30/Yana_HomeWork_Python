"""
Тест 1. Форма
Проверка валидации полей формы
Браузер: Google Chrome
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_form_validation():
    """Тест проверки подсветки полей формы"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # Заполняем форму
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем Submit
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        driver.execute_script("arguments[0].click();", submit_button)

        # Ждем появления классов валидации
        time.sleep(1)

        # Проверяем Zip code
        zip_code = driver.find_element(By.ID, "zip-code")
        zip_class = zip_code.get_attribute("class")
        error_msg = "Zip code поле должно быть подсвечено красным"
        assert "alert-danger" in zip_class.lower() or "error" in zip_class.lower(), error_msg

        # Проверяем остальные поля
        success_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        for field_name in success_fields:
            field = driver.find_element(By.ID, field_name)
            field_class = field.get_attribute("class")
            success_msg = f"Поле {field_name} должно быть подсвечено зеленым"
            assert "is-valid" in field_class.lower() or "success" in field_class.lower(), success_msg

        print("✅ Тест формы пройден")

    finally:
        driver.quit()
        

