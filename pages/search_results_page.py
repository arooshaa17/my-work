import time

from constants import MAIN_PAGE_TITLE, LOWEST_PRICE, SORT_DROP_DOWN, MEMORY, CONDITION, BUY_NOW
from pages.base_page import BasePage


class SearchResultPage(BasePage):

    def sort_by_price(self):
        """
        Input sent text to sent field
        """
        self.driver.find_element_by_css_selector(SORT_DROP_DOWN).click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(LOWEST_PRICE).click()

    def select_filters(self):
        """
        Input sent text to sent field
        """
        self.driver.find_element_by_css_selector(MEMORY).click()
        self.driver.find_element_by_css_selector(CONDITION).click()
        self.driver.find_element_by_css_selector(BUY_NOW).click()

    def buy_an_item(self):
        """
        Input sent text to sent field
        """
        self.driver.find_element_by_css_selector(BUY_NOW).click()
