import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestShop:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Тест оформления заказа в интернет-магазине")
    @allure.description("Проверка добавления товаров в корзину и итоговой суммы")
    def test_shopping_cart(self):
        with allure.step("Открыть страницу авторизации"):
            login_page = LoginPage(self.driver)
            login_page.open()

        with allure.step("Выполнить авторизацию под пользователем standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page = InventoryPage(self.driver)
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
            inventory_page.add_item_to_cart("Sauce Labs Onesie")
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page = CartPage(self.driver)
            cart_page.checkout()

        with allure.step("Заполнить форму заказа данными покупателя"):
            checkout_page = CheckoutPage(self.driver)
            checkout_page.fill_form("Иван", "Петров", "123456")

        with allure.step("Проверить итоговую сумму заказа"):
            total = checkout_page.get_total()
            assert total == "Total: $58.29", f"Ожидалось Total: $58.29, получено {total}"
            