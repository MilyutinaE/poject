import allure
from pages_and_components.components.header_component import HeaderComponent
from pages_and_components.pages.registration_page import RegistrationPage
from models.fake_user import fake_first_name, fake_last_name, fake_email, fake_phone, fake_password
from pages_and_components.pages.my_account_page import MyAccountPage


@allure.severity(allure.severity_level.NORMAL)
def test_check_fields_on_reg_page(browser):
    "Проверяем поле имя, фамилия, емейл, телефон, чекбокс на странице реги"
    header = HeaderComponent(browser)
    header.click_on_my_account_registration()
    register = RegistrationPage(browser)
    assert register.check_fields()


@allure.severity(allure.severity_level.CRITICAL)
def test_register_new_user(browser):
    "Регаемся и проверяем линки и кнопку логаута на странице аккаунта"
    header = HeaderComponent(browser)
    header.click_on_my_account_registration()
    register = RegistrationPage(browser)
    register.registration_new_user(fake_first_name(), fake_last_name(), fake_email(), fake_phone(), fake_password())
    my_account = MyAccountPage(browser)
    assert my_account.check_links_visible()
    assert my_account.check_logout_button_right_menu()
