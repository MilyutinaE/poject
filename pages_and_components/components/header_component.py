import time

from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class HeaderComponent(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.MY_ACCOUNT_BUTTON = (By.XPATH, '//span[text()="My Account"]')
        self.REGISTER_IN_MY_ACCOUNT_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu dropdown-menu-right"]'
                                                          '//*[text()="Register"]')
        self.SHOPPING_CART = (By.XPATH, "//*[@class='list-inline']//*[@class='fa fa-shopping-cart']")

    @allure.step("Click 'my account' button")
    def click_on_my_account_registration(self):
        el = self.get_element_by_locator(self.MY_ACCOUNT_BUTTON)
        el.click()
        self.get_element_by_locator(self.REGISTER_IN_MY_ACCOUNT_DROPDOWN).click()

    @allure.step("Click 'Shopping Cart'")
    def click_shopping_cart(self):
        self.is_element_visible(self.SHOPPING_CART)
        cart = self.get_element_by_locator(self.SHOPPING_CART)
        cart.click()
