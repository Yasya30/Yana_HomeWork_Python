"""
Тест 3. Покупка - отладочная версия
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_shop():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        driver.save_screenshot("01_login_page.png")
        print("✅ Страница логина открыта")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.save_screenshot("02_after_login.png")
        print("✅ Авторизация выполнена")

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        driver.save_screenshot("03_products_page.png")
        print("✅ Страница товаров загружена")

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        print("✅ Товары добавлены")

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        driver.save_screenshot("04_cart_page.png")
        print("✅ Корзина открыта")

        # Проверим, какие кнопки есть на странице
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Найдено кнопок: {len(buttons)}")
        for btn in buttons:
            print(f"  - {btn.get_attribute('id')}: {btn.text}")

        # Нажимаем Checkout
        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()
        time.sleep(2)
        driver.save_screenshot("05_after_checkout.png")
        print("✅ Нажата кнопка Checkout")

        # Проверим URL
        print(f"Текущий URL: {driver.current_url}")

        # Проверим заголовок
        print(f"Заголовок: {driver.title}")

        # Поищем поле first-name
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.save_screenshot("06_form_filled.png")
        print("✅ Форма заполнена")

        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        driver.save_screenshot("07_after_continue.png")
        print("✅ Нажата кнопка Continue")

        total = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total.text
        print(f"Итоговая сумма: {total_text}")

        assert "$58.29" in total_text
        print("✅ Тест покупки пройден")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        driver.save_screenshot("error_final.png")
        raise

    finally:
        time.sleep(3)
        driver.quit()
