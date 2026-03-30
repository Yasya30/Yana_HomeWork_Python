"""
Упражнение 2. Переименовать кнопку
Перейти на сайт http://uitestingplayground.com/textinput
Указать в поле ввода текст SkyPro
Нажать на синюю кнопку
Получить текст кнопки и вывести в консоль
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
wait = WebDriverWait(driver, 10)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Ждем загрузки поля ввода
    wait.until(EC.presence_of_element_located((By.ID, "newButtonName")))

    # Находим поле ввода и вводим текст SkyPro
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")
    print("Введен текст: SkyPro")

    # Находим и нажимаем синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    print("Кнопка нажата")

    # Ждем изменения текста кнопки
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Получаем текст кнопки и выводим в консоль
    new_button_text = button.text
    print(new_button_text)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
