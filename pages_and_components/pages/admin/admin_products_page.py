from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminProductsPage(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.ADD_NEW = (By.XPATH, "//*[@data-original-title='Add New']")
        self.NAME_IPHONE = (By.XPATH, "//*[@class='text-left' and text()='iPhone']")
        self.IPHONE_EDIT_BUTTON = (By.XPATH, "//*[@class='text-left' and text()='iPhone']/following-sibling::td/a")
        self.DELETE = (By.XPATH, "//*[@data-original-title='Delete']")
        self.IPHONE_CHECKBOX = (By.XPATH, "//*[@class='text-left' and text()='iPhone']/preceding-sibling::td//*"
                                          "[@type='checkbox']")

    @allure.step("Click 'add new'")
    def click_add_new(self):
        self.click(self.ADD_NEW)

    @allure.step("Check Product Title")
    def check_product_title(self, name):
        result = self.is_element_visible((By.XPATH, f"//*[text()='{name}']"))
        return result

    @allure.step("Click edit iPhone")
    def click_edit_iphone(self):
        self.click(self.IPHONE_EDIT_BUTTON)

    @allure.step("Select product {name_product}")
    def select_product(self, name_product):
        self.click((By.XPATH, f"//*[@class='text-left' and text()='{name_product}']/preceding-sibling::td//*"
                              f"[@type='checkbox']"))

    @allure.step("Click Delete")
    def click_delete(self,):
        self.click(self.DELETE)
        self.accept_alert()


# @allure.step("Delete iPhone")
#     def click_delete(self):
#         self.click(self.DELETE)
#         self.accept_alert()