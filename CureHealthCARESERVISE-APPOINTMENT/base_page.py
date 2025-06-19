from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import logging
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_scrape(self, locator, many=False, click=False, keys=None, time=10, condition="presence", pres_enter=False):
        try:
            # Condition logic...
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
                        if pres_enter:
                            elem.send_keys(Keys.RETURN)
                    return elements

                if click:
                    for elem in elements:
                        elem.click()
                return elements

            else:
                element = self.driver.find_element(*locator)
                if keys:
                    element.send_keys(keys)
                    if pres_enter:
                        element.send_keys(Keys.RETURN)
                    return element

                if click:
                    try:
                        element.click()
                    except ElementClickInterceptedException:
                        self.driver.execute_script("arguments[0].click();", element)
                return element
        
        except (TimeoutException, NoSuchElementException) as e:
            print(f"[ERROR] Couldn't find element {locator}: {str(e)}")
            return None



    # this method is specially designed for @CURA HEALTHCARE SERVICE SITE
    def date_calendar(self):   
        self.find_scrape((By.ID, "txt_visit_date"), click=True)
        time.sleep(1)

        for _ in range(2):
            # Wait for new label to appear (fresh DOM state)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "th.datepicker-switch"))
            )

            #  Grab latest text AFTER DOM is updated
            label_element = self.find_scrape((By.CSS_SELECTOR, "th.datepicker-switch"))


            #  Click it using JS for extra safety
            self.driver.execute_script("arguments[0].click();", label_element)
            time.sleep(1)

        # go back to the admired year
        prev = self.find_scrape((By.CSS_SELECTOR, "th.prev"))
        self.driver.execute_script("arguments[0].click();", prev)
        time.sleep(1)
        prev = self.find_scrape((By.CSS_SELECTOR, "th.prev"))
        self.driver.execute_script("arguments[0].click();", prev)

         # Select year, month, day
        self.find_scrape((By.XPATH, "//span[@class='year' and text()='2008']"), click=True)
        self.find_scrape((By.XPATH, "//span[@class='month' and text()='Aug']"), click=True)
        self.find_scrape((By.XPATH, "//td[@class='day' and text()='18']"), click=True)
        logging.info("Calender is handled")

