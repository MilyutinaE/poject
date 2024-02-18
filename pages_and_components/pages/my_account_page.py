from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class MyAccountPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.TITLE = "My Account"
        self.EDIT_INFO_LINK = (By.XPATH, '//a[text()="Edit your account information"]')
        self.CHANGE_PASSWORD_LINK = (By.XPATH, '//a[text()="Change your password"]')
        self.YOUR_TRANSACTIONS_LINK = (By.XPATH, '//a[text()="Your Transactions"]')
        self.LOGOUT_BUTTON_RIGHT_MENU = (By.XPATH, '//*[@class="list-group"]//*[text()="Logout"]')
        self.check_my_account_page()

    @allure.step("Wait title change")
    def check_my_account_page(self):
        self.wait_title_change(self.TITLE)

    @allure.step("Check links is visible: edit info, change password, your transactions")
    def check_links_visible(self):
        try:
            self.is_element_visible(self.EDIT_INFO_LINK)
            self.is_element_visible(self.CHANGE_PASSWORD_LINK)
            self.is_element_visible(self.YOUR_TRANSACTIONS_LINK)
            return True
        except TimeoutException:
            return False

    @allure.step("Check logout button in right menu")
    def check_logout_button_right_menu(self):
        try:
            self.is_element_visible(self.LOGOUT_BUTTON_RIGHT_MENU)
            return True
        except TimeoutException:
            return False
