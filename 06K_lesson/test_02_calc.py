"""
Тест 2. Калькулятор
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 60)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        print("✅ Тест калькулятора пройден")
    finally:
        driver.quit()


