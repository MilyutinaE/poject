import allure
from pages_and_components.pages.catalog_page import CatalogPage
from pages_and_components.pages.product_page import ProductPage
from pages_and_components.components.catalog_menu_component import CatalogMenuComponent


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
