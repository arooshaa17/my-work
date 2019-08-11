from constants import SEARCH_BOX, SEARCH_BUTTON, SEARCH_RESULT_SELECTOR
from pages.base_page import BasePage


class SearchPage(BasePage):

    def search_by_value(self, search_text):
        self.wait_for_element(SEARCH_BOX)
        search_box = self.driver.find_element_by_css_selector(SEARCH_BOX)
        search_box.click()
        search_box.send_keys(search_text)
        self.driver.find_element_by_css_selector(SEARCH_BUTTON).click()
        self.wait_for_ajax()

    def verify_result_count(self):
        result_count_list = []
        results = self.driver.find_element_by_css_selector(SEARCH_RESULT_SELECTOR).text
        result_count_list.append(results)
        return result_count_list



