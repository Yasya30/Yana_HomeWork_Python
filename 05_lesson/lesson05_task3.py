"""
Упражнение 3. Поле ввода
Открыть браузер FireFox.
Перейти на страницу: http://the-internet.herokuapp.com/inputs.
Ввести в поле текст 12345.
Очистить это поле (метод clear()).
Ввести в поле текст 54321.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Настройка драйвера Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)
    
    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Вводим текст 12345
    input_field.send_keys("12345")
    print("✅ Введен текст: 12345")
    time.sleep(1)
    
    # Очищаем поле
    input_field.clear()
    print("✅ Поле очищено")
    time.sleep(1)
    
    # Вводим текст 54321
    input_field.send_keys("54321")
    print("✅ Введен текст: 54321")
    
    time.sleep(2)
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    
finally:
    # Закрываем браузер
    driver.quit()
    print("✅ Браузер закрыт")