from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import json
from base_page import BasePage



class Products(BasePage):

    def get_products(self):
        self.products = self.find_wait_and_send_keys((By.CSS_SELECTOR, "div.Bm3ON"), many=True)
        # BasePage.wait_find_element_for_products((By.CSS_SELECTOR, "div.Bm3ON"), By.CSS_SELECTOR, "div.Bm3ON")


    def get_each_product_details(self):
        self.product_details = []
        for product in self.products:
            title = product.find_element(By.CSS_SELECTOR, "div > a").text
            price = product.find_element(By.CSS_SELECTOR, "div > span").text
            self.product_details.append({
                "Title": title,
                "Price": price
            })

    def save_json(self):
        with open("DarazProducts", "w", encoding="utf-8") as file:
            json.dump(self.product_details, file, ensure_ascii=False, indent=4)
    








