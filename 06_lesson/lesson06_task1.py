"""
Упражнение 1. Нажать на кнопку с AJAX запросом
Перейти на страницу http://uitestingplayground.com/ajax
Нажать на синюю кнопку
Получить текст из зеленой плашки
Вывести его в консоль
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Ждем загрузки страницы и кнопки
    wait.until(EC.presence_of_element_located((By.ID, "ajaxButton")))

    # Находим и нажимаем синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()
    print("Кнопка нажата")

    # Ждем появления зеленой плашки с текстом
    green_label = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # Получаем текст и выводим в консоль
    text = green_label.text
    print(text)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
