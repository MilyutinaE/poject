from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class RegistrationPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.INPUT_FIRSTNAME = (By.ID, 'input-firstname')
        self.INPUT_LASTNAME = (By.ID, 'input-lastname')
        self.INPUT_EMAIL = (By.ID, "input-email")
        self.INPUT_TELEPHONE = (By.ID, "input-telephone")
        self.INPUT_PASSWORD = (By.ID, 'input-password')
        self.INPUT_PASSWORD_CONFIRM = (By.ID, 'input-confirm')
        self.PRIVACY_POLICY = (By.NAME, 'agree')
        self.CONTINUE_BUTTON = (By.XPATH, "//input[@type='submit']")
        self.CONTINUE_SECOND_BUTTON = (By.XPATH, "//a[text()='Continue']")
        self.TITLE = "Register Account"
        self.TITLE_SUCCESSFUL = "Your Account Has Been Created!"
        self.check_registration_page()

    @allure.step("Registration new user")
    def registration_new_user(self, firstname, lastname, email, telephone, password):
        with allure.step("Enter firstname"):
            self.get_element_by_locator(self.INPUT_FIRSTNAME).send_keys(firstname)
        with allure.step("Enter lastname"):
            self.get_element_by_locator(self.INPUT_LASTNAME).send_keys(lastname)
        with allure.step("Enter email"):
            self.get_element_by_locator(self.INPUT_EMAIL).send_keys(email)
        with allure.step("Enter telephone"):
            self.get_element_by_locator(self.INPUT_TELEPHONE).send_keys(telephone)
        with allure.step("Enter password"):
            self.get_element_by_locator(self.INPUT_PASSWORD).send_keys(password)
        with allure.step("Enter confirm password"):
            self.get_element_by_locator(self.INPUT_PASSWORD_CONFIRM).send_keys(password)
        with allure.step("Click Privacy Policy"):
            self.get_element_by_locator(self.PRIVACY_POLICY).click()
        with allure.step("Click Continue Button"):
            self.get_element_by_locator(self.CONTINUE_BUTTON).click()
        self.check_registration_successful()
        with allure.step("Click Continue second Button"):
            self.get_element_by_locator(self.CONTINUE_SECOND_BUTTON).click()

    @allure.step("Wait title change")
    def check_registration_page(self):
        assert self.wait_title_change(self.TITLE)

    @allure.step("Check content on registration page")
    def check_fields(self):
        try:
            self.get_element_by_locator(self.INPUT_FIRSTNAME)
            self.get_element_by_locator(self.INPUT_LASTNAME)
            self.get_element_by_locator(self.INPUT_EMAIL)
            self.get_element_by_locator(self.INPUT_TELEPHONE)
            self.get_element_by_locator(self.PRIVACY_POLICY)
            return True
        except TimeoutException:
            return False

    @allure.step("Check registration successful")
    def check_registration_successful(self):
        self.wait_title_change(self.TITLE_SUCCESSFUL)
