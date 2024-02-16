from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminLoginPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.USERNAME = (By.XPATH, "//input[@name='username']")
        self.PASSWORD = (By.XPATH, "//input[@name='password']")
        self.LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
        self.FORGOT_PASSWORD = (By.XPATH, "//*[@class='help-block']/a")
        self.ALERT = (By.CSS_SELECTOR, ".alert-danger")

    @allure.step("Success login")
    def login(self, username, password):
        with allure.step("Enter username"):
            self.click(self.USERNAME)
            self.send_keys(self.USERNAME, username)
        with allure.step("Enter password"):
            self.click(self.PASSWORD)
            self.send_keys(self.PASSWORD, password)
        with allure.step("Click login button"):
            self.click(self.LOGIN_BUTTON)

    @allure.step("Failed Login")
    def failed_login(self, username, password):
        with allure.step("Enter username"):
            self.click(self.USERNAME)
            self.send_keys(self.USERNAME, f"{username}999")
        with allure.step("Enter password"):
            self.click(self.PASSWORD)
            self.send_keys(self.PASSWORD, password)
        with allure.step("Click login button"):
            self.click(self.LOGIN_BUTTON)
        result = self.is_element_visible(self.ALERT)
        return result
