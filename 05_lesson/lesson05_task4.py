"""
Упражнение 4. Форма авторизации
Открыть браузер FireFox.
Перейти на страницу http://the-internet.herokuapp.com/login.
В поле username ввести значение tomsmith.
В поле password ввести значение SuperSecretPassword!.
Нажать кнопку Login.
Вывести текст с зеленой плашки в консоль.
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
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)
    
    # Находим поле username и вводим значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("✅ Введен username: tomsmith")
    
    # Находим поле password и вводим значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("✅ Введен password: SuperSecretPassword!")
    
    # Находим кнопку Login и нажимаем
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("✅ Нажата кнопка Login")
    
    time.sleep(2)
    
    # Находим зеленую плашку с сообщением
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    
    # Выводим текст из плашки в консоль
    print(f"\n📢 Сообщение об успешной авторизации:")
    print(f"{'=' * 50}")
    print(f"{success_message.text.strip()}")
    print(f"{'=' * 50}")
    
    time.sleep(2)
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    
finally:
    # Закрываем браузер
    driver.quit()
    print("\n✅ Браузер закрыт")