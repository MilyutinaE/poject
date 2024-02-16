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
def test_catalog_page_mp3_players(browser):
    "В синем меню сверху выбираем MP3 Players и открываем каталог с плеерами"
    catalog_menu = CatalogMenuComponent(browser)
    catalog_menu.click_mp3_players()
    catalog_menu.show_all_mp3_players()
    catalog_page = CatalogPage(browser)
    catalog_page.check_content_visible()
    catalog_page.wait_title("MP3 Players")
    assert catalog_page.check_selected_category("MP3 Players")