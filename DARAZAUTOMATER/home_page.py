from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage


class HomePage(BasePage):

    def getting_daraz_home_page(self):
        self.driver.get("https://www.bing.com/")
        self.find_wait_and_send_keys((By.NAME, 'q'), keys="daraz", pres_enter=True)
        # self.wait_and_send_keys((By.NAME, 'q'), (By.NAME, 'q'), "daraz")
        self.find_wait_and_send_keys((By.CSS_SELECTOR, "li.b_algo h2 > a")).click()
        # self.wait_find_element_for_product((By.CSS_SELECTOR, "a span"), (By.CSS_SELECTOR, "li.b_algo h2 > a")).click()
  