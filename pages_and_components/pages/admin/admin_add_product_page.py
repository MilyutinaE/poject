from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminAddProductPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.NAME = (By.XPATH, "//*[@id='input-name1']")
        self.META_TAG = (By.XPATH, "//*[@id='input-meta-title1']")
        self.SUBMIT = (By.XPATH, "//*[@type='submit']")
        self.WARNING = (By.XPATH, "//*[contains(text(),'Warning')]")
        self.DATA = (By.XPATH, "//*[text()='Data']")
        self.MODEL_IN_DATA = (By.XPATH, "//*[@id='input-model']")
        self.SUCCESS = (By.XPATH, "//*[contains(text(),'Success')]")

    @allure.step("Add new product (result=Fail)")
    def add_new_product_fail(self, name, meta_tag):
        with allure.step("Enter name"):
            self.get_element_by_locator(self.NAME).send_keys(name)
        with allure.step("Enter meta tag"):
            self.get_element_by_locator(self.META_TAG).send_keys(meta_tag)
        with allure.step("Click Submit"):
            self.get_element_by_locator(self.SUBMIT).click()
        result = self.is_element_visible(self.WARNING)
        return result

    @allure.step("Add new product (result=Success)")
    def add_new_product_success(self, name, meta_tag, model):
        with allure.step("Enter name"):
            self.get_element_by_locator(self.NAME).send_keys(name)
        with allure.step("Enter meta tag"):
            self.get_element_by_locator(self.META_TAG).send_keys(meta_tag)
        with allure.step("Click Data"):
            self.get_element_by_locator(self.DATA).click()
        with allure.step("Enter Model"):
            self.get_element_by_locator(self.MODEL_IN_DATA).send_keys(model)
        with allure.step("Click Submit"):
            self.get_element_by_locator(self.SUBMIT).click()
        with allure.step("Check 'Success: You have modified products!'"):
            result = self.is_element_visible(self.SUCCESS)
        return result
