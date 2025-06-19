import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
#--modules
from api import fetch_coins_list
from api import fetch_global_market_data
from api import fetch_selected_coins_data
from api import fetch_coin_market_chart
from utils import unit_numbers 
from utils import highlight_change 


# -- Streamlit Setup --
st.set_page_config("Crypto Analyzer Dashboard", layout="wide")
currency = st.sidebar.selectbox("Select Currency", ["usd", "gbp", "eur", "inr", "pkr"])


# -- Fetch coin list from sidebar selection
with st.spinner("Fetching coin list..."):
    coin_list_df = fetch_coins_list()

coin_list_df['display'] = coin_list_df['name'] + " (" + coin_list_df['symbol'] + ")"
selected_coins = st.sidebar.multiselect(
    "Select Coins (10)", 
    coin_list_df['display'].tolist(),
    default=['Bitcoin (btc)', "Ethereum (eth)"]
)

selected_ids = coin_list_df[coin_list_df["display"].isin(selected_coins)]['id'].tolist()


# --- Tabs Layout ---
tab1, tab2, tab3, tab4 = st.tabs(["🌍 Global Overview", "📊 My Coins", "📈 Price Trends", "📥 Download"])


# --------------- Tab 1: Global Overview ----------
with tab1:
    st.subheader("🌍 Global Market Highlights (100)")

    with st.spinner("Fetching global market data..."):
        global_df = fetch_global_market_data(vs_currency=currency)

    col1, col2 = st.columns(2)
    with col1:
        top_10_gainers = global_df.sort_values(by="price_change_percentage_24h", ascending=False).head(10)
        st.subheader("🚀 Top 10 Gainers (24h)")
        for index, row in top_10_gainers.iterrows():
            st.metric(label=row['name'], value=f"{row['price_change_percentage_24h']:.2f}%")

        
    with col2:
        top_10_losers = global_df.sort_values(by="price_change_percentage_24h", ascending=True).tail(10)
        st.subheader("🔻 Top 10 Losers (24h)")
        for index, row in top_10_losers.iterrows():
            st.metric(label=row['name'], value=f"{row['price_change_percentage_24h']:.2f}%")


# ------- Tab 2: My Coins ----------
with tab2:
    st.subheader("📊 My Selected Coins")
    if selected_ids:
        with st.spinner("Fetching market data..."):
            df = fetch_selected_coins_data(vs_currency=currency, coin_ids=selected_ids)
        st.session_state['selected_ids'] = selected_ids
        st.session_state['df'] = df


        if not df.empty:
            df_copy = df.copy()
            df_copy['market_cap'] = df_copy['market_cap'].apply(unit_numbers)
            df_copy['total_volume'] = df_copy['total_volume'].apply(unit_numbers)
            df_copy['price_change_percentage_24h'] = df_copy['price_change_percentage_24h'].apply(highlight_change)

            selected_columns = ["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
            st.dataframe(df_copy[selected_columns])


            # -- Charts --
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

            st.subheader("Total Volume")
            fig_volume = px.bar(
                df,
                x="name",
                y="total_volume",
                color='total_volume',
                title="Total Volume",
                labels={"total_volume": "Total Volume"}
            )
            st.plotly_chart(fig_volume, use_container_width=True)



            st.subheader("Market Capitalization")
            fig_market_cap = px.bar(
                df,
                x="name",
                y="market_cap",
                color='market_cap',
                title="Market Capitalization",
                labels={"market_cap": "Market Cap"}
            )
            st.plotly_chart(fig_market_cap, use_container_width=True)

        else:
            st.warning("Could not fetch market data for selected coins.")
    else:
        st.info("Please selected atleast one coin from the sidebar.")



# ---------- Tab 3: Price Trends ----------
with tab3:
    st.subheader("📈 Multi-Coin Price Trends")

    days = st.select_slider("Select date range:", options=[7, 14, 30, 90], value=30)

    if "selected_ids" in st.session_state:
        coin_ids = st.session_state['selected_ids']
        currency = st.session_state.get("currency", currency)
        prices_data = {}

        for coin_id in coin_ids:
            with st.spinner(f"Fetching {days}-day chart for {coin_id}..."):
                try:
                    prices = fetch_coin_market_chart(coin_id, currency, days)
                    if not prices:
                        st.warning(f"⚠️ No data found for {coin_id}. Skipping...")
                        continue
                    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                    df.set_index('timestamp', inplace=True)
                    prices_data[coin_id] = df['price']
                except Exception as e:
                    st.error(f"❌ Error fetching {coin_id}: {str(e)}")
                    continue

        if prices_data:
            combined_df = pd.concat(prices_data.values(), axis=1)
            combined_df.columns = list(prices_data.keys())
            combined_df.sort_index(inplace=True)

            # Fill any missing timestamps for uniformity
            if combined_df.isna().any().any():
                combined_df.fillna(method="ffill", inplace=True)
                combined_df.fillna(method="bfill", inplace=True)
                st.info("ℹ️ Missing values detected and filled for smoother charting.")

            combined_df.reset_index(inplace=True)

            fig = px.line(
                combined_df,
                x='timestamp',
                y=combined_df.columns[1:],
                title=f"{days}-Day Price Trend Comparison",
                labels={"value": "Price", "timestamp": "Date"},
            )
            fig.update_layout(hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("No valid price data available to display.")


        
    
# ------ Tab 4: Download -------
with tab4:
    st.subheader("📥 Download Your Data")


    if 'df' in st.session_state and not st.session_state['df'].empty:
        df = st.session_state['df']
        selected_columns = ["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
        csv = df[selected_columns].to_csv(index=False)
        st.download_button("Download CSV", csv, "crypto_data.csv", "text/csv")
    else:
        st.warning("No data available to download. Please select coins first.")

    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}")


