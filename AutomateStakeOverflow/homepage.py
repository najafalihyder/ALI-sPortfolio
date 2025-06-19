from base_page import BasePage
from selenium.webdriver.common.by import By
import json

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def homeScrape(self):
        # Click on the first post summary (e.g. first question box)
        self.find_scrape((By.ID, "question-summary-75018953"), click=True)

        # Get all comments
        answer = self.find_scrape((By.CSS_SELECTOR, "div.s-prose p"), condition="presence", time=15).text
        print(answer)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # user_answer = []
        # for ans in answer:
        #     try:
        #         text = ans.find_element(By.CSS_SELECTOR, "span.comment-copy").text
        #     except:
        #         text = "no text"

        #     try:
        #         date = ans.find_element(By.CSS_SELECTOR, "span.relativetime-clean").text
        #     except:
        #         date = "no date"

        #     try:
        #         user = ans.find_element(By.CSS_SELECTOR, "a.comment-user").text
        #     except:
        #         user = "no user"

        #     user_answer.append({
        #         "Text": text,
        #         "Date": date,
        #         "User": user
        #     })

        # with open("StakeoverflowComments.json", "w", encoding="utf-8") as file:
        #     json.dump(user_answer, file, ensure_ascii=False, indent=4)
