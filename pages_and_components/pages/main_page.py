from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class MainPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.TITLE = "Your Store"
        self.check_main_page()
        self.FEATURED = (By.XPATH, "//*[text()='Featured']")
        self.COMPANY_CAROUSEL = (By.XPATH, "//*[@class='carousel swiper-viewport']")
        self.CONTENT = (By.ID, "content")
        self.NAVIGATION_BAR = (By.CSS_SELECTOR, ".nav.navbar-nav")   # class="nav navbar-nav"
        self.FEATURED_FIRST_PRODUCT = (By.XPATH, "(//*[@class='product-thumb transition'])[1]")

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

    def check_main_page(self):
        self.wait_title_change(self.TITLE)

    @allure.step("Check price")
    