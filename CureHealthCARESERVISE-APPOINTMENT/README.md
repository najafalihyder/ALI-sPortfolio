# 🏥 Cure Health Care Center – Appointment Booking Automation (Selenium + POM)

A full end-to-end automation system that handles **appointment scheduling** on behalf of users for **Cure Health Care Center**, using real browser control with **Selenium**. This tool simulates human interaction to search for slots, fill out forms, and complete appointments — all without manual effort.

> Now built using the **Page Object Model (POM)** for professional code structure, easy maintenance, and scalability.

---

## 🚀 Key Features

- ✅ Automates the entire patient appointment booking workflow
- ✅ Searches for available slots based on user preferences
- ✅ Automatically fills out all required fields
- ✅ Handles slow pages / timeouts (can be extended to support captcha/OTP)
- ✅ Runs in both normal and **headless** browser mode
- ✅ Fast and repeatable for multiple patients
- ✅ Modular **POM architecture** for clean and reusable code
- ✅ Logs success/failure results for each run

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Automation**: Selenium WebDriver
- **Architecture**: Page Object Model (POM)
- **Browser**: Chrome (Headless & Visible mode)
- **Tools Used**: `selenium`, `time`, `json`, `logging`, `os`

---

## 🧠 Project Structure (POM-Based)


cure-health-automation/
│
├── main.py # Entry point: runs the automation using page classes
│
├── pages/ # POM: Page-wise Selenium handlers
│ ├── home_page.py # Handles initial home screen interactions
│ ├── slot_page.py # Searches and selects slots
│ ├── form_page.py # Fills and submits patient form
│ └── confirmation_page.py # Verifies success and captures result
│
├── utils/ # Utilities & support functions
│ └── helpers.py # Waits, logs, captchas (if needed)
│
├── config.json # Patient and appointment configuration
├── requirements.txt # Python package dependencies
└── README.md # This file

---

## ▶️ How to Use

### 1. Install ChromeDriver  
Download from: https://chromedriver.chromium.org/downloads  
Make sure it matches your Chrome version and is in your system PATH.

---

### 2. Install Python dependencies  
```bash
pip install -r requirements.txt

Customize your booking preferences:


{
  "name": "John Doe",
  "phone": "1234567890",
  "center": "Cure Health Center",
  "preferred_date": "2025-06-20"
}


4. Run the Automation
python main.py


💡 Use Cases
Auto-booking for diagnostic labs or medical clinics

Time-saving automation for admins and receptionists

Bulk/scheduled bookings for patients

Healthcare workflow automation with real browser control

📦 Future Scope
 OTP or captcha solving (can be integrated)

 Email/SMS confirmations

 CI/CD integration for daily scheduled runs

 Multi-patient automation via config loop

⚠️ Disclaimer
This tool is for educational and personal automation showcase purposes only. Always respect website Terms of Service. Do not use for spamming or overloading live medical systems.

🤝 Hire Me
I specialize in real-world automation using Python + Selenium + POM.
If you want to automate healthcare forms, scrape medical data, or streamline admin workflows — I can build it.

📩 Upwork: My Profile : https://www.upwork.com/freelancers/~018b0354b85575ecd2

📜 License
MIT – Free to use, extend, or modify. Attribution appreciated ❤️
