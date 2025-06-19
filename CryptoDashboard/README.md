# 📊 Crypto Dashboard – Real-Time Market Insights with Streamlit

A modern, interactive crypto dashboard built with **Python** and **Streamlit**, powered by the **CoinGecko API**. This tool fetches live market data and presents it through **KPI cards, interactive charts, and customizable inputs** — all within a clean tabbed interface.

---

## 🚀 Key Features

- ✅ **Live Market Data** via CoinGecko API
- ✅ **Top 10 Coins** by Market Cap shown as real-time KPI Cards
- ✅ **User Search**: Enter any coin + currency to get detailed insights
- ✅ **Dynamic Charts**: Line, bar, and pie visualizations
- ✅ **Tabbed Interface** for clean UI/UX
- ✅ **Downloadable Data** in CSV format
- ✅ Modular code structure (easy to extend/maintain)

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **API**: [CoinGecko API](https://www.coingecko.com/en/api)
- **Core Tools**: `pandas`, `requests`, `json`, `plotly`, `streamlit`
- **Output**: KPI Cards, Charts, Tables, CSV

---

## 📁 Project Structure



crypto-dashboard/
│
├── app.py # Main Streamlit app with tabs + layout
├── fetch_data.py # API data fetching logic
├── kpi.py # Top 10 coin KPI card generator
├── chart_utils.py # Chart functions (line, bar, pie)
├── config.json # Default coins/currencies
├── requirements.txt # Python dependencies
├── README.md # You're here



> 📌 All modules are clean and reusable.

---

## ▶️ How to Run the Dashboard Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/najafalihyder/ALI-sPortfolio/tree/main/CryptoDashboard.git
   cd crypto-dashboard


Install dependencies:
pip install -r requirements.txt


Launch the Streamlit app:
streamlit run app.py (verify file -> app name)


🧑‍💼 Use Cases
Cryptocurrency market research

Investor dashboards

Portfolio insights

Educational visualizations

API demo for data projects


🤝 Hire Me
This dashboard is part of my portfolio to showcase my skills in:

Real-time data visualization

API integration & automation

Python dashboarding (Streamlit)

Custom tool development

📩 Let’s build your custom data dashboard or automation system.
Contact me on Upwork
[ == PROFILE == }: https://www.upwork.com/freelancers/~018b0354b85575ecd2

📜 License
Free to use under the MIT License.
