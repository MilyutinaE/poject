from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import re


class ShoppingCartPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        # self.AVAILABILITY = (By.XPATH, "//*[@class='list-unstyled']//*[contains(text(), 'Availability:')]")
        # self.PRODUCT_CODE = (By.XPATH,  "//*[@class='list-unstyled']//*[contains(text(),'Product Code:')]")
        # self.BRAND = (By.XPATH, "//*[@class='list-unstyled']//*[contains(text(), 'Brand:')]")
        # self.ADD_TO_CART = (By.XPATH, "//*[text()='Add to Cart']")
        # self.DESCRIPTION = (By.XPATH, "//*[text()='Description']")
        self.TOTAL_PRICE = (By.XPATH, "(//*[@class='table table-bordered'])[3]/tbody/tr[4]/td[2]")

    @allure.step("Check total price")
    def check_total_price(self):
        total_price = self.get_element_by_locator(self.TOTAL_PRICE)
        total_price_text = total_price.text
        # Используем регулярное выражение для извлечения только цифр и точек
        price = re.sub(r'[^0-9.]', '', total_price_text)
        return price
