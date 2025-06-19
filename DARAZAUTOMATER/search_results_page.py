from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class Search_results(BasePage):


    
    def get_search_query(self):
        self.find_wait_and_send_keys((By.ID, "q"), keys="smartphones", pres_enter=True)
        # self.wait_and_send_keys((By.ID, "q"), (By.ID, "q"), "smartphones")

