import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_shopping_cart(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_form("Иван", "Петров", "123456")
        total = checkout_page.get_total()

        assert total == "Total: $58.29"
        