# 🛒 Daraz Product Automater (Selenium + POM)

A complete automation tool that interacts with the **Daraz e-commerce website** to perform tasks like product search, filtering, and simulated interactions — using a **real browser with Selenium** and a clean **Page Object Model (POM)** architecture.

> Ideal for testing, automation demos, or streamlining repetitive product workflows.

---

## 🚀 Features

- ✅ Automated product search & navigation
- ✅ Filters products by category, price, etc.
- ✅ Interacts with dynamic elements (sliders, dropdowns)
- ✅ Logs product names, prices, ratings
- ✅ Fully modular using **Page Object Model (POM)**
- ✅ Easy to extend (add to cart, login, wishlist, etc.)
- ✅ Headless mode support for background runs

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Automation**: Selenium WebDriver
- **Browser**: Chrome (Headless & UI mode)
- **Architecture**: Page Object Model (POM)

---

## 📁 Project Structure



daraz-automater/
│
├── main.py # Entry point script
│
├── pages/
│ ├── home_page.py # Search bar and categories
│ ├── results_page.py # Handles product listings and filters
│ └── product_page.py # (Optional) Single product details
│
├── utils/
│ └── helpers.py # Waits, scrolls, etc.
│
├── config.json # Search terms and filters
├── requirements.txt # Dependencies
└── README.md # This file


## ▶️ How to Use

1. **Install dependencies**

pip install -r requirements.txt
Update config.json

{
  "search_term": "smartphones",
  "min_price": 10000,
  "max_price": 50000,
  "sort_by": "popularity"
}
Run automation
python main.py
💡 Use Cases
Automated product research

Pricing comparison tools

E-commerce workflow demos

Data collection (limited scraping)

🤝 Hire Me
Need to automate real e-commerce workflows with Selenium & Python?
Let me build your bots, testers, or scrapers.

📩 Upwork Profile : https://www.upwork.com/freelancers/~018b0354b85575ecd2

📜 License
MIT – Free to use and modify with credit.

