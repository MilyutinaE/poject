import allure
from pages_and_components.pages.main_page import MainPage

@pytest.mark.skip("Skipped test")
@allure.severity(allure.severity_level.NORMAL)
def test1_main_page(browser):
    "Проверяем контент на мейн пейдже"
    main_page = MainPage(browser)
    assert main_page.check_content_visible()