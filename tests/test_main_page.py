import allure
from models.admin import username, passwod
from pages_and_components.components.header_component import HeaderComponent
from pages_and_components.pages.admin.admin_login_page import AdminLoginPage
from pages_and_components.pages.catalog_page import CatalogPage
from pages_and_components.pages.product_page import ProductPage
from pages_and_components.pages.registration_page import RegistrationPage
from pages_and_components.pages.main_page import MainPage
from pages_and_components.components.catalog_menu_component import CatalogMenuComponent
import pytest
from pages_and_components.components.currency_component import CurrencyComponent
#pytest tests\test_main_page.py


@pytest.mark.skip("Skipped test")
@allure.severity(allure.severity_level.NORMAL)
def test_ckeck_content_on_main_page(browser):
    "Проверяем контент на мейн пейдже"
    main_page = MainPage(browser)
    assert main_page.check_content_visible()


@allure.severity(allure.severity_level.NORMAL)
def test_change_currency(browser):
    "Меняем валюту в хедере и проверяем, что она поменялась"
    currency = CurrencyComponent(browser)
    currency.open_currency_dropdown()
    assert currency.change_random_currency()

@allure.severity(allure.severity_level.CRITICAL)
def test_check_price(browser):
    "Добавляем товар в корзину и проверяем, что цена не изменилась"
    main_page = MainPage(browser)
