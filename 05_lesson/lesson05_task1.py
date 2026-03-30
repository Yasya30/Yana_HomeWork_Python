"""
Упражнение 1. Клик по кнопке с CSS-классом
Открыть браузер Google Chrome.
Перейти на страницу: http://uitestingplayground.com/classattr.
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
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)
    
    # Находим синюю кнопку по CSS классу (btn-primary)
    # Используем contains для надежности
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    
    # Кликаем на кнопку
    blue_button.click()
    print("✅ Клик по синей кнопке выполнен")
    
    # Небольшая пауза, чтобы увидеть результат
    time.sleep(2)
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    
finally:
    # Закрываем браузер
    driver.quit()