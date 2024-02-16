import time

from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure
import re


class MainPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.TITLE = "Your Store"
        self.FEATURED = (By.XPATH, "//*[text()='Featured']")
        self.COMPANY_CAROUSEL = (By.XPATH, "//*[@class='carousel swiper-viewport']")
        self.CONTENT = (By.ID, "content")
        self.NAVIGATION_BAR = (By.CSS_SELECTOR, ".nav.navbar-nav")   # class="nav navbar-nav"
        self.FEATURED_1_PRODUCT_PRICE = (By.XPATH, "(//*[@class='product-thumb transition'])[1]//*[@class='price']")
        self.FEATURED_1_PRODUCT_ADD = (By.XPATH, "(//*[@class='product-thumb transition'])[1]//*[text()='Add to Cart']")
        self.ADD_TO_CART_TEXT = (By.XPATH, "//*[contains(text(), 'Add to cart')]")
        self.LOGO = (By.XPATH, "//*[@alt='Your Store']")

    @allure.step("Check content on main page")
    def check_content_visible(self):
        try:
            self.is_element_visible(self.FEATURED)
            self.is_element_visible(self.COMPANY_CAROUSEL)
            self.is_element_visible(self.CONTENT)
            self.is_element_visible(self.NAVIGATION_BAR)
            return True
        except TimeoutException:
            return False

    @allure.step("Click on logo")
    def click_on_logo(self):
        self.get_element_by_locator(self.LOGO).click()

    @allure.step("Check price on first featured product ")
    def check_price_first_product(self):
        first_product_price = self.get_element_by_locator(self.FEATURED_1_PRODUCT_PRICE)
        first_product_price_text = first_product_price.text
        #  регулярное выражение \$\([\d.,]+) ищет последовательность цифр, запятых и точек, следующих после символа
        #  доллара. re.search() для поиска первого совпадения в тексте, далее извлечение значения с помощью .group(1)
        price_value = re.search(r'\$([\d.,]+)', first_product_price_text).group(1)
        return price_value

    @allure.step("Add to cart first featured product ")
    def add_first_product(self):
        self.get_element_by_locator(self.FEATURED_1_PRODUCT_ADD).click()
