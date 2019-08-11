import unittest

from selenium import webdriver
from constants import BASE_URL, SEARCH_INPUT_INTEL, RESULTS_PAGE_TITLE, MAIN_PAGE_TITLE
from pages.search_page import SearchPage
from pages.search_results_page import SearchResultPage


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\geckodriver\geckodriver')
        self.driver.get(BASE_URL)
        self.search_page = SearchPage(self.driver)
        self.results_page = SearchResultPage(self.driver)

    def test_search_working(self):
        self.assertTrue('Not on the correct page', self.search_page.is_browser_on_page(MAIN_PAGE_TITLE))
        self.search_page.search_by_value(SEARCH_INPUT_INTEL)
        self.assertTrue('Not on the correct page', self.search_page.is_browser_on_page(RESULTS_PAGE_TITLE))
        list1 = self.search_page.verify_result_count()
        self.assertEqual('List 1 does not match', ['560 results for Intel NUC'], list1)
        self.results_page.sort_by_price()
        self.results_page.select_filters()
        list2 = self.search_page.verify_result_count()
        self.assertEqual('List 1 does not match', ['207 results for Intel NUC'], list2)
        print(list1 + list2)

    def tearDown(self):
        self.driver.close()
