# 🧠 Crypto Data Aggregator – ETL Pipeline + Streamlit Dashboard

A Python-based end-to-end data aggregator that extracts real-time cryptocurrency data using the CoinGecko API, processes it through a modular ETL pipeline, and visualizes it using a clean Streamlit dashboard.

---

## 🚀 Features

- ✅ Extract real-time crypto data using CoinGecko API
- ✅ Clean and modular ETL architecture (Extract → Transform → Load)
- ✅ Data transformation and formatting with Pandas
- ✅ Email reporting system (daily reports via email)
- ✅ Streamlit dashboard for live crypto insights
- ✅ JSON config system for dynamic coin selection
- ✅ Clean codebase, reusable functions, easy to scale

---

## 📁 Project Structure

All files are organized in a single root directory:

- `main.py` – Entry point to trigger the entire ETL process
- `extract.py` – Handles API data fetching from CoinGecko
- `transform.py` – Cleans and structures the raw data
- `load.py` – Saves the final dataset to CSV / DB
- `db.py` – Functions for database interaction (SQLite or other)
- `email_report.py` – Sends summary email with key data stats
- `coins_config.json` – User-defined coin list and settings
- `streamlit_app.py` – Streamlit dashboard to visualize crypto stats

> 🔧 Modular code = Easy to maintain, scale, and repurpose for other data sources.

---

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**: `requests`, `pandas`, `streamlit`, `smtplib`, `json`, `datetime`
- **API**: [CoinGecko API](https://www.coingecko.com/en/api)
- **Dashboard**: Streamlit
- **Automation**: Config-driven + Email report system

---

## 🧪 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/najafalihyder/ALI-sPortfolio/tree/main/CryptoAgregator.git
   cd crypto-etl-dashboard


Install dependencies:
pip install -r requirements.txt


Run the ETL Pipeline:
python main.py

Launch the Streamlit dashboard:
streamlit run streamlit_app.py



📬 Email Report Setup (Optional)
To enable email reporting:

Update SMTP details in email_report.py

Configure your sender email and credentials

Run the pipeline and get auto email with latest data

🤝 Hire Me
This project is part of my portfolio to showcase my skills in:

Web Scraping & APIs

ETL pipelines

Data Automation & Reporting

Interactive Dashboards (Streamlit)

📩 Let’s build your next data automation project!
Contact me on Upwork
[-- PROFILE --]: https://www.upwork.com/freelancers/~018b0354b85575ecd2

📜 License
This project is open-source and free to use under the MIT License.
