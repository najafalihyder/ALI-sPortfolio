from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json

def setup_driver():
    options = webdriver.ChromeOptions
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def search_products(driver, query):
    url = "https://www.amazon.com"
    driver.get(url)
    wait = WebDriverWait(driver, 10) # dirver=who is waiting , and, 10 means waiting in seconds
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def extract_products(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_elements_located((By.CSS_SELECTOR, "div.s-main-slot")))
    product_elements = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
    for product in product_elements:
        title = product.find_element(By.CSS_SELECTOR, "h2 span").text
        whole_price = int(product.find_element(By.CSS_SELECTOR, ".a-price-whole").text)
        friction_price = int(product.find_element(By.CSS_SELECTOR, ".a-price-fraction").text)
        price = float(f"{whole_price}.{friction_price}")
        rating = product.find_element(By.CSS_SELECTOR, ".span.a-icon-alt").text
   






