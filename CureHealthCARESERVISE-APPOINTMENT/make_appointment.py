# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from base_page import BasePage
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging
# from datetime import datetime
# import csv


# class MakeAppoinment(BasePage):
#     def login_site(self, username, password):
#         """
#         Logs into the CURA Healthcare Service portal using provided credentials.
#         """
#         try:
#             self.find_scrape((By.ID, "btn-make-appointment"), click=True)
#             self.find_scrape((By.ID, "txt-username"), keys=username)
#             self.find_scrape((By.ID, "txt-password"), keys=password)
#             self.find_scrape((By.ID, "btn-login"), click=True)

#             heading = self.find_scrape((By.XPATH, "//h2[text()='Make Appointment']"), condition="visibility")
#             assert heading is not None, "[ERROR] Login failed or appointment page not loaded!"
#             logging.info("Login successful.")
#         except Exception as e:
#             logging.error(f"Login failed: {e}")

#     def set_logging_file(self):
#         """
#         Sets up the logging configuration with timestamped log filename and format.
#         """
#         log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

#         logging.basicConfig(
#             filename = log_filename,
#             filemode = "w",
#             format='[%(asctime)s] [%(levelname)s] %(message)s', 
#             datefmt='%d-%m-%Y %H:%M:%S',
#             level=logging.INFO
#         )
#         logging.getLogger('urllib3').setLevel(logging.WARNING) 

#     def select_dropdown(self):
#         """
#         Selects the facility from the dropdown menu by selected index.
#         """
#         try:
#             select = Select(self.find_scrape((By.NAME, 'facility')))
#             select.select_by_index(2)
#             logging.info("Facility selected.")
#         except Exception as e:
#             logging.error(f"Dropdown selection failed: {e}")

#     def click_checkbox(self):
#         """
#         Clicks on the hospital readmission checkbox .
#         """
#         try:
#             self.find_scrape((By.XPATH, "//input[@type='checkbox']"), click=True)
#             logging.info("Checkbox clicked.")
#         except Exception as e:
#             logging.error(f"Checkbox click failed: {e}")

#     def radio_selection(self):
#         """
#         Selects the options of 'Medicaid' program radio button.
#         """
#         try:
#             radio = self.find_scrape((By.XPATH, "//input[@type='radio' and @id='radio_program_medicaid']"))
#             if not radio.is_selected():
#                 radio.click()
#             logging.info("Medicaid radio button selected.")
#         except Exception as e:
#             logging.error(f"Radio selection failed: {e}")

#     # def filling_calendar(self):
#     #     """
#     #     Fills in the visit date using inherited calendar function from BasePage.
#     #     """
#     #     try:
#     #         self.date_calendar  # Assumes it's handled in the BasePage
#     #         logging.info("Calendar filled.")
#     #     except Exception as e:
#     #         logging.error(f"Calendar filling failed: {e}")
#     def date_calendar(self):   
#         self.find_scrape((By.ID, "txt_visit_date"), click=True)
#         time.sleep(1)

#         for _ in range(2):
#             # Wait for new label to appear (fresh DOM state)
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "th.datepicker-switch"))
#             )

#             #  Grab latest text AFTER DOM is updated
#             label_element = self.find_scrape((By.CSS_SELECTOR, "th.datepicker-switch"))


#             #  Click it using JS for extra safety
#             self.driver.execute_script("arguments[0].click();", label_element)
#             time.sleep(1)

#         # go back to the admired year
#         prev = self.find_scrape((By.CSS_SELECTOR, "th.prev"))
#         self.driver.execute_script("arguments[0].click();", prev)
#         time.sleep(1)
#         prev = self.find_scrape((By.CSS_SELECTOR, "th.prev"))
#         self.driver.execute_script("arguments[0].click();", prev)

#             # Select year, month, day
#         self.find_scrape((By.XPATH, "//span[@class='year' and text()='2008']"), click=True)
#         self.find_scrape((By.XPATH, "//span[@class='month' and text()='Aug']"), click=True)
#         self.find_scrape((By.XPATH, "//td[@class='day' and text()='18']"), click=True)
#         logging.info("Calender is handled")


#     def fill_form(self, comment_text="That is my favourite year ever!"):
#         """
#         Posts a comment and submits the form of my preferred year.
#         Allows submitting with or without a comment.
#         """
#         try:
#             comment_field = self.find_scrape((By.NAME, "comment"), click=True)
#             if comment_text:
#                 comment_field.send_keys(comment_text)
#                 logging.info("Comment entered.")
#             else:
#                 logging.info("Comment field left empty.")
            
#             self.find_scrape((By.XPATH, "//button[@type='submit']"), click=True)
#             logging.info("Form submitted.")
#         except Exception as e:
#             logging.error(f"Form submission failed: {e}")


#     def take_screenshot(self):
#         """
#         Captures a screenshot of the confirmation page.
#         """
#         try:
#             self.driver.save_screenshot("confirmShot.png")
#             logging.info("Screenshot captured.")
#         except Exception as e:
#             logging.error(f"Screenshot failed: {e}")

#     def logout(self):
#         """
#         Logs out of the application using JavaScript click .
#         """
#         try:
#             self.find_scrape((By.ID, "menu-toggle"), click=True)
#             logout = self.find_scrape((By.XPATH, "//a[text()='Logout']"))
#             self.driver.execute_script("arguments[0].click();", logout)
#             logging.info("User logged out successfully.")
#         except Exception as e:
#             logging.error(f"Logout failed: {e}")

#     def save_csv(self):
#         """
#         Saves the appointment data into a CSV file.
#         """
#         try:
#             appointment_data = {
#                 "Facility": "Hongkong CURA",
#                 "Program": "Medicaid",
#                 "Visit Date": "18/08/2008",
#                 "Comment": "That is my favourite year ever!"
#             }

#             with open("appointment_data.csv", mode='w', newline='', encoding='utf-8') as file:
#                 writer = csv.DictWriter(file, fieldnames=appointment_data.keys())
#                 writer.writeheader()
#                 writer.writerow(appointment_data)

#             logging.info("Data saved to CSV successfully.")
#         except Exception as e:
#             logging.error(f"CSV saving failed: {e}")

#     def makeappointment(self, comment_text="That is my favourite year ever!"):
#         """
#         main function where all the methods will called 


#         """
#         self.set_logging_file()
#         self.select_dropdown()
#         self.click_checkbox()
#         self.radio_selection()
#         # self.filling_calendar()
#         self.date_calendar()
#         self.fill_form(comment_text=comment_text)
#         self.take_screenshot()
#         self.logout()
#         self.save_csv()
#         print("[] Appointment process completed.")




name = 'ALi'
print("Hello %s" % name)





