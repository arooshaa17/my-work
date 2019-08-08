import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    title = ''

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_page(self, selector):
        """
        Is browser on sent page
        """
        time.sleep(1)
        return selector in self.driver.title

    def wait_for_ajax(self):
        """
        Wait for jQuery to be loaded and for all ajax requests to finish
        """
        return self.driver.execute_script(
            "return typeof(jQuery)!='undefined' && jQuery.active==0")

    def wait_for_element(self, wait_selector):
        """
        Wait for element
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, wait_selector))
        )