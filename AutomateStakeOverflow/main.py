from login_page import Login
from homepage import HomePage
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stackoverflow.com/users/login")

login_ = Login(driver)

# Let user manually complete captcha
input("Please log in manually and complete captcha, then press Enter...")

# Optionally save screenshot
driver.save_screenshot('after_login.png')

home = HomePage(driver)
l = input(":")
driver.save_screenshot("test.png")
home.homeScrape()

driver.save_screenshot('after_scraping.png')
