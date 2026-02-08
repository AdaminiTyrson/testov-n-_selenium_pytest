
from app_pages import LoginPage, InventoryPage, CartPage
from app_pages import LoginPage, InventoryPage, CartPage, driver

def test_successful_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()


def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in cart.get_cart_items()