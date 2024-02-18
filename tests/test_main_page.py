import allure
from pages_and_components.components.header_component import HeaderComponent
from pages_and_components.pages.shopping_cart import ShoppingCartPage
from pages_and_components.pages.main_page import MainPage
from pages_and_components.components.currency_component import CurrencyComponent


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
    main_page.click_on_logo()
    price = main_page.check_price_first_product()
    main_page.add_first_product()
    header = HeaderComponent(browser)
    header.click_shopping_cart()
    shopping_cart = ShoppingCartPage(browser)
    price_total = shopping_cart.check_total_price()
    assert price == price_total
