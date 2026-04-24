from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
time.sleep(3)  # Даем странице полностью загрузиться

# Находим все поля ввода
inputs = driver.find_elements(By.TAG_NAME, "input")
for inp in inputs:
    print(f"ID: {inp.get_attribute('id')}, NAME: {inp.get_attribute('name')}, TYPE: {inp.get_attribute('type')}")

driver.quit()