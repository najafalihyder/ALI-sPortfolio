from selenium.webdriver.common.by import By
from base_page import BasePage

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.find_scrape((By.ID, "email"), keys=email)
        self.find_scrape((By.ID, "password"), keys=password)
        self.find_scrape((By.ID, "submit-button"), click=True)
