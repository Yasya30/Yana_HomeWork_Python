"""
Упражнение 3. Дождаться картинки
Перейти на сайт:
https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
Дождаться загрузки всех картинок
Получить значение атрибута src у 3-й картинки
Вывести значение в консоль
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
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    # Ждем, пока загрузится контейнер с картинками
    wait.until(EC.presence_of_element_located((By.ID, "image-container")))

    # Ждем, пока появится хотя бы 3 картинки
    wait.until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img"))
        >= 3
    )

    # Находим все картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    print(f"Найдено картинок: {len(images)}")

    # Получаем 3-ю картинку (индекс 2, т.к. нумерация с 0)
    third_image = images[2]

    # Получаем значение атрибута src
    src_value = third_image.get_attribute("src")

    # Выводим в консоль
    print(src_value)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
