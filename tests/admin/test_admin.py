import allure
from models.admin import username, passwod
from pages_and_components.pages.admin.admin_login_page import AdminLoginPage
from pages_and_components.pages.admin.admin_add_product_page import AdminAddProductPage
from models.product import name_product, meta_tag, model
from pages_and_components.components.admin.admin_left_menu import AdminLeftMenu
from pages_and_components.pages.admin.admin_products_page import AdminProductsPage
# pytest tests\admin\test_admin.py


@allure.severity(allure.severity_level.CRITICAL)
def test_failed_admin_login(browser, base_url):
    "Проверяем неуспешный логин администратора"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    assert admin_login.failed_login(username, passwod)


@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_product_fail(browser, base_url):
    "Неуспешно добавляем новый продукт в админке"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    admin_login.login(username, passwod)
    admin_left_menu = AdminLeftMenu(browser)
    admin_left_menu.select_products()
    admin_products_page = AdminProductsPage(browser)
    admin_products_page.click_add_new()
    add_product = AdminAddProductPage(browser)
    assert add_product.add_new_product_fail(name_product, meta_tag)


def test_add_new_product_and_delete(browser, base_url):
    "Успешно добавляем новый продукт в админке и удаляем его"
    browser.get(f"{base_url}/admin")
    admin_login = AdminLoginPage(browser)
    admin_login.login(username, passwod)
    admin_left_menu = AdminLeftMenu(browser)
    admin_left_menu.select_products()
    admin_products_page = AdminProductsPage(browser)
    admin_products_page.click_add_new()
    add_product = AdminAddProductPage(browser)
    assert add_product.add_new_product_success(name_product, meta_tag, model)
    assert admin_products_page.check_product_title(name_product)
    admin_products_page.select_product(name_product)
    admin_products_page.click_delete()
    assert admin_products_page.check_product_title(name=f"{name_product}") is False
