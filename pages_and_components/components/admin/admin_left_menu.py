from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminLeftMenu(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.CATALOG = (By.XPATH, "//*[text()=' Catalog']")
        self.PRODUCTS = (By.XPATH, "//a[text()='Products']")

    @allure.step("Select catalog - products")
    def select_products(self):
        self.click(self.CATALOG)
        self.click(self.PRODUCTS)
