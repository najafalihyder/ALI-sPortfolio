import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime



#-- Func for Units of numbers 
def unit_numbers(number):
    for unit in ["", "K", "M", "B", "T"]:
        if abs(number) < 1000:
            return f"{number:.2f}{unit}"
        
        number /= 1000
    return f"{number:,.2f}E+"


# -- Func for highlighted coins
def highlight_change(val):
    if val > 5:
        return f"🟢 +{val:.2f}%"
    elif val < -5:
        return f"🔴 {val:.2f}%"
    else:
        return f"⚪️ {val:.2f}%"




def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print("Error:", response.status_code)


st.set_page_config("Crypto Analiser Dashboard", layout="wide")
currency = st.sidebar.selectbox("Select Currency", ["usd", "eur", "gbp", "inr", "pkr"])


# Fetch coin list
with st.spinner("Fetching coin list..."):
    data = fetch_data()


data['display'] = data['name'] + "(" + data['symbol'] + ")"
selected_coins = st.sidebar.multiselect(
    "Select Coins",
    data['display'].tolist(),
    default=["Bitcoin(btc)", "Ethereum(eth)"])
selected_ids = data[data['display'].isin(selected_coins)]['id'].tolist()




def fetch_global_market_data(top_n=100):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency":  currency,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error(f"Failed to fetch global market data: {response.status_code}")
        return pd.DataFrame


# Fetch global market data (top 100 coins)
with st.spinner("Fetching global market data..."):
    global_df = fetch_global_market_data(top_n=100)


tab1, tab2, tab3 = st.tabs(["🌍 Global Overview", "📊 My Coins", "📥 Download"])    

# ---------------- Tab 1: Global Overview ----------------
with tab1:

        # --- KPI CARDS ---
    st.subheader("🌍 Global Market Highlights (Top 100)")

    col1, col2 = st.columns(2)
    with col1:
        sorted_global = global_df.sort_values(by="price_change_percentage_24h", ascending=False)
        top_3_gainers = sorted_global.head(3)
        st.subheader("🚀 Top 3 Gainers (24h)")
        for index, row in top_3_gainers.iterrows():
            st.metric(label=row['name'], value=f"{row['price_change_percentage_24h']:.2f}%")


    with col2:
        top_3_losers = sorted_global.tail(3).sort_values(by="price_change_percentage_24h", ascending=True)
        st.subheader("🔻 Top 3 Losers (24h)")
        for index, row in top_3_losers.iterrows():
            st.metric(label=row['name'], value=f"{row['price_change_percentage_24h']:.2f}%")



# ---------------- Tab 2: My Coins ----------------
with tab2:
    st.subheader("📊 My Selected Coins")

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": currency,
        "ids": ",".join(selected_ids)
    }
    # Fetch selected coins' market data
    with st.spinner("Fetching market data..."):
        response = requests.get(url, params)

    if response.status_code == 200:
        selected_data = response.json()
        df = pd.DataFrame(selected_data)
        df = df.sort_values(by="market_cap", ascending=False)

        df_copy = df.copy()
        df_copy['market_cap'] = df_copy['market_cap'].apply(unit_numbers)
        df_copy['total_volume'] = df_copy['total_volume'].apply(unit_numbers)
        df_copy['price_change_percentage_24h'] = df_copy['price_change_percentage_24h'].apply(highlight_change)

        st.subheader("Market Data")

        selected_columns = ["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
        st.dataframe(df_copy[selected_columns])

        
        # 24h Price Change Chart
        st.subheader("24h Price Change Chart (%)")
        fig_change = px.bar(
            df,
            x="name",
            y="price_change_percentage_24h",
            color="price_change_percentage_24h",
            title="24h Price Change (%)",
            labels={"price_change_percentage_24h": "% Change"}
        )


        st.plotly_chart(fig_change, use_container_width=True)


        # Total Volume Chart
        st.subheader("Total Volume ")
        fig_volume = px.bar(
            df,
            x="name",
            y="total_volume",
            color="total_volume",
            title="Total Volume",
            labels={"total_volume": "Total Volume"}
        )
        st.plotly_chart(fig_volume, use_container_width=True)


        # Market Cap Chart
        st.subheader("Market Capitalization")
        fig_market_cap = px.bar(
            df,
            x='name',
            y='market_cap',
            color='market_cap',
            title="Market Capitalization",
            labels={"market_cap": "Market Cap"}
        )
        st.plotly_chart(fig_market_cap, use_container_width=True)

    else:
        st.error(f"Load to fetch data {response.status_code}")



# ---------------- Tab 3: Download ----------------
with tab3:
    st.subheader("📥 Download Your Data")

    if 'df' in locals() and not df.empty:
        csv = df[selected_columns].to_csv(index=False)
        st.download_button("Download CSV", csv, "crypto_data.csv", "text/csv")
    else:
        st.warning("No data available to download. Please select coins first.")

    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")