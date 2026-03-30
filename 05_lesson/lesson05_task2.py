"""
Упражнение 2. Клик по кнопке без ID
Открыть браузер Google Chrome.
Перейти на страницу: http://uitestingplayground.com/dynamicid.
Кликнуть на синюю кнопку.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)

    # Находим синюю кнопку (она одна на странице)
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    # Кликаем на кнопку
    blue_button.click()
    print("✅ Клик по синей кнопке выполнен")

    time.sleep(2)

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()
