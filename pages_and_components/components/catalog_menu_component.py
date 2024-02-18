from pages_and_components.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CatalogMenuComponent(BasePage):
    def __init__(self, browser):
        self.driver = browser
        self.MP3_PLAYERS = (By.XPATH, "//*[text()='MP3 Players']")
        self.SHOW_ALL_MP3_PLAYERS = (By.XPATH, "//*[text()='Show All MP3 Players']")

    @allure.step("Click 'mp3 players'")
    def click_mp3_players(self):
        self.get_element_by_locator(self.MP3_PLAYERS).click()

    @allure.step("Click 'show all mp3 players'")
    def show_all_mp3_players(self):
        self.get_element_by_locator(self.SHOW_ALL_MP3_PLAYERS).click()
