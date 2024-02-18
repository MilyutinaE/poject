import allure
from pages_and_components.pages.catalog_page import CatalogPage
from pages_and_components.components.catalog_menu_component import CatalogMenuComponent


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
