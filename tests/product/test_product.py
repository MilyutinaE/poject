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


@allure.severity(allure.severity_level.NORMAL)
def test_product_page(browser):
    "Открываем страницу первого мп3 плеера из каталога и проверяем контент"
    catalog_menu = CatalogMenuComponent(browser)
    catalog_menu.click_mp3_players()
    catalog_menu.show_all_mp3_players()
    catalog_page = CatalogPage(browser)
    catalog_page.click_first_product()
    product_page = ProductPage(browser)
    assert product_page.check_content_visible()
