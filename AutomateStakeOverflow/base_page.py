from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_scrape(self, locator, many=False, click=False, keys=None, time=10, condition="presence"):
        if condition == "presence":
            cond_func = EC.presence_of_element_located if not many else EC.presence_of_all_elements_located
        elif condition == "visibility":
            cond_func = EC.visibility_of_element_located if not many else EC.visibility_of_all_elements_located
        elif condition == "clickable":
            cond_func = EC.element_to_be_clickable
        else:
            raise ValueError("Invalid condition. Choose from 'presence', 'visibility', or 'clickable'")

        WebDriverWait(self.driver, time).until(cond_func(locator))

        if many:
            elements = self.driver.find_elements(*locator)
            if keys:
                for elem in elements:
                    elem.send_keys(keys)
                    elem.send_keys(Keys.RETURN)
            if click:
                for elem in elements:
                    self.scroll_and_click(elem)
            return elements  # 🛠 FIXED: Always return
        else:
            element = self.driver.find_element(*locator)
            if keys:
                element.send_keys(keys)
                element.send_keys(Keys.RETURN)
            if click:
                self.scroll_and_click(element)
            return element  # 🛠 FIXED: Always return

    def scroll_and_click(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.3)
            element.click()
        except:
            ActionChains(self.driver).move_to_element(element).click().perform()
