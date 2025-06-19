from home_page import HomePage
from search_results_page import Search_results
from product_page import Products
from selenium import webdriver


driver = webdriver.Chrome()

home_page = HomePage(driver)
home_page.getting_daraz_home_page()
search_results = Search_results(driver)
search_results.get_search_query()
products = Products(driver)
products.get_products()
products.get_each_product_details()
products.save_json()
