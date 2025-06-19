
# 🛍️ Amazon Product Scraper using Selenium (Python)

A robust and browser-automated scraper built with **Python** and **Selenium** to extract real-time product data from **Amazon**. Designed to handle dynamic content and avoid basic anti-scraping blocks.

---

## 🚀 Features

- ✅ Extract key product details:
  - Product Title
  - Price (deal/discount/original)
  - Rating & Number of Reviews
  - Availability (in stock / out of stock)
  - ASIN, Seller, Delivery Info
- ✅ Works for both:
  - Product Detail Pages
  - Search Results Pages (multiple products)
- ✅ Built with Selenium WebDriver (real browser scraping)
- ✅ Headless mode supported (runs without UI)
- ✅ CSV/JSON export for scraped data
- ✅ Easy to customize and extend

---

## 🛡️ Anti-Bot Handling

- Uses **real browser simulation** (Selenium)
- Custom **User-Agent headers**
- Can integrate with **proxies** or **VPNs**
- Adjustable **waits**, **timeouts**, and **scrolling**
- Option to randomize actions to simulate human behavior

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**:
  - `selenium`
  - `pandas`
  - `time`, `json`, `csv`, `os`, etc.
- **Browser Driver**: ChromeDriver (or GeckoDriver for Firefox)

---

## 📁 Project Structure



amazon-scraper-selenium/
│
├── scraper.py # Main script to scrape products
├── config.json # (Optional) product URLs or search terms
├── utils.py # Utility functions (scrolling, delays)
├── output.csv # Output file (generated)
├── requirements.txt # Python dependencies
├── README.md # This file

---

## ▶️ How to Run

1. **Install ChromeDriver**  
   Download it from: https://chromedriver.chromium.org/downloads  
   Make sure it's added to your system PATH.

2. **Clone the repo**:
   ```bash
   git clone https://github.com/najafalihyder/ALI-sPortfolio/tree/main/AmazonScraper.git
   cd amazon-scraper-selenium
Install dependencies:

pip install -r requirements.txt
Run the scraper:


python scraper.py
💡 Example Use Cases
Track competitor pricing and listings

Monitor price changes over time

Collect product leads for e-commerce strategy

Analyze review trends and product ratings

⚠️ Legal Disclaimer
This tool is intended for educational and personal use only. Scraping Amazon may violate their Terms of Service. Use responsibly and avoid overloading their servers.

🤝 Hire Me
I specialize in scraping complex websites using Selenium, anti-blocking techniques, and data automation.

📩 Hire me on Upwork  [ -- PROFILE -- ]: https://www.upwork.com/freelancers/~018b0354b85575ecd2
Let’s build a custom scraper for your project.

📜 License
MIT License – Free to use, modify, and distribute.
