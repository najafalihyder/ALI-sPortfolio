import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from make_appointment import MakeAppoinment

@pytest.fixture(scope="function")
def setup_driver():
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    yield driver
    driver.quit()


def test_login_valid(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    heading = setup_driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
    assert heading is not None
    print("fs")


def test_login_invalid(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("WrongUser", "WrongPass")
    assert "Make Appointment" not in setup_driver.page_source


def test_facility_dropdown(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.select_dropdown()
    selected = setup_driver.find_element(By.NAME, "facility")
    assert selected.get_attribute("value") != ""


def test_hospital_checkbox(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.click_checkbox()
    checkbox = setup_driver.find_element(By.XPATH, "//input[@type='checkbox']")
    assert checkbox.is_selected()


def test_healthcare_program_radio(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.radio_selection()
    radio = setup_driver.find_element(By.ID, "radio_program_medicaid")
    assert radio.is_selected()


def test_visit_date_input(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.filling_calendar()
    date_input = setup_driver.find_element(By.ID, "txt_visit_date")
    assert date_input.get_attribute("value") != ""


def test_empty_comment_submission(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.select_dropdown()
    app.click_checkbox()
    app.radio_selection()
    app.filling_calendar()
    app.find_scrape((By.NAME, "comment"), click=True, keys="")
    app.find_scrape((By.XPATH, "//button[@type='submit']"), click=True)
    confirmation = app.find_scrape((By.XPATH, "//h2[text()='Appointment Confirmation']"), condition="visibility")
    assert confirmation is not None


def test_successful_appointment(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.makeappointment()
    heading = setup_driver.find_element(By.XPATH, "//h2[text()='Appointment Confirmation']")
    assert heading is not None


def test_screenshot_created(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.take_screenshot()
    assert os.path.exists("confirmShot.png")
    os.remove("confirmShot.png")


def test_csv_created(setup_driver):
    app = MakeAppoinment(setup_driver)
    app.login_site("John Doe", "ThisIsNotAPassword")
    app.save_csv()
    assert os.path.exists("appointment_data.csv")
    os.remove("appointment_data.csv")
