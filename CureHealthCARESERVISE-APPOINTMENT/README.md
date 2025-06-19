# 🏥 Cure Health Care Center – Appointment Booking Automation

A full end-to-end automation system that handles **appointment scheduling** on behalf of users for **Cure Health Care Center**, using real browser control with **Selenium**. This tool simulates human interaction to search for slots, fill out forms, solve captchas, and complete appointments — without manual effort.

---

## 🚀 Key Features

- ✅ Automates the entire patient appointment booking workflow
- ✅ Searches for available slots based on user needs
- ✅ Automatically fills out all required fields
- ✅ Handles captchas / OTP / browser delays (if applicable)
- ✅ Can run in the background (headless mode)
- ✅ Fast and repeatable for multiple patients
- ✅ Logs results / confirmations

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Automation**: Selenium WebDriver
- **Browser**: Chrome (Headless support enabled)
- **Tools Used**: `selenium`, `time`, `json`, `logging`, `os`

---

## 📁 Project Structure

re-health-automation/
│
├── main.py # Main automation script
├── form_filler.py # Handles dynamic form entries
├── slot_checker.py # Slot search and availability logic
├── config.json # Patient/config data
├── utils.py # Helpers for captchas, delays
├── requirements.txt # Dependencies
├── README.md # This file


---

## ▶️ How to Use

1. **Install ChromeDriver**  
   Download from: https://chromedriver.chromium.org/downloads  
   Make sure it matches your Chrome version and is in PATH.

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt

   Edit config.json with patient details:

   {
  "name": "John Doe",
  "phone": "1234567890",
  "center": "Cure Health Center",
  "preferred_date": "2025-06-20"
}

Run the automation:
python main.py

💡 Example Use Cases
Auto-booking for clinics or diagnostic centers

Saving time for medical staff or admins

Running scheduled bookings for multiple patients

Automating repetitive web interactions in healthcare

⚠️ Disclaimer
This tool is intended for educational and automation showcase purposes only. Always respect the website's terms of service. Do not overload or spam booking systems.


🤝 Hire Me
I specialize in real-world automation using Python + Selenium. If you need to automate forms, appointments, scraping, or data workflows — I can build custom, scalable systems.

📩 Hire me on Upwork [ PROFILE ] https://www.upwork.com/freelancers/~018b0354b85575ecd2

📜 License
MIT – Free to use, extend, or modify.
