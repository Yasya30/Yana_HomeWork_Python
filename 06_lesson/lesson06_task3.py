import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShop:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_shopping_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(self.driver, 10)

        username = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

        add_buttons = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".btn_inventory")
            )
        )
        add_buttons[0].click()
        add_buttons[1].click()

        cart = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )
        cart.click()

        cart_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "cart_item")
            )
        )
        assert len(cart_items) == 2