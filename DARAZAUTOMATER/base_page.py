from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        

    def find_wait_and_send_keys(self, locator, many=False, keys=None, time=10, condition=EC.presence_of_element_located, pres_enter=False):

        if condition == "presense":
            condition = EC.presence_of_element_located if not many else EC.presence_of_all_elements_located
        elif condition == "visibility":
            condition = EC.visibility_of_all_elements_located if many else EC.visibility_of_element_located
        elif condition == "clickable":
            condition = EC.element_to_be_clickable
        else:
            raise ValueError("Invalid condition! Choose from: 'presence', 'visibility', 'clickable'.")

        WebDriverWait(self.driver, time).until(condition(locator))

        if many:
            elements = self.driver.find_elements(*locator)
            if keys:
                if pres_enter:
                    for elem in elements:
                        elem.send_keys(keys)
                        elem.send_keys(Keys.RETURN)
                else:
                    for elem in elements:
                        elem.send_keys(keys)
                    return elements
            return elements
        else:
            element = self.driver.find_element(*locator)
            if keys:
                if pres_enter:
                    element.send_keys(keys)
                    element.send_keys(Keys.RETURN)
                else:
                    element.send_keys(keys)
                    return element

            return element
        

   


      


