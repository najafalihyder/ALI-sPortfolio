from make_appointment import MakeAppoinment
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




options = Options()

# 🔒 Disable Chrome's built-in password manager completely
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2
}
options.add_experimental_option("prefs", prefs)

# ✅ Optional: Start in incognito mode
options.add_argument("--incognito")

# ✅ Optional: Disable browser extensions
options.add_argument("--disable-extensions")

# ✅ Optional: Use a fresh profile every time
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-infobars")
options.add_argument("--disable-save-password-bubble")

driver = webdriver.Chrome(options=options)
driver.get("https://katalon-demo-cura.herokuapp.com/")


automate = MakeAppoinment(driver)
automate.login_site("John Doe", "ThisIsNotAPassword")
automate.makeappointment()














