import streamlit as st
import pandas as pd
from datetime import date
import sqlite3
import yagmail
import tempfile
from config import EMAIL_PASSWORD, EMAIL_SENDER




st.set_page_config(
    page_title = "Crypto Dashboard",
    page_icon = "📊",
    layout = "wide"
)   # setted the page appearance (page title , page icon , layout) they are all about window 


# injecting css (for better appearance)
st.markdown("""
            
        <style>
    .main { background-color: #f7f9fc; }
    .block-container { padding-top: 2rem; }
    .css-18e3th9 { padding: 2rem; }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: #888;
        text-align: center;
        padding: 10px;
        font-size: 0.85rem;
    }
    </style>

    """, unsafe_allow_html=True) # use unsafe_allow_html when want to inject htmkl or css without it we can not use them in streamlit

# page title and description
st.title("📊 Crypto Price Dashboard")
st.markdown("Track live prices, 24h changes, and volumes for top cryptocurrencies.")


conn = sqlite3.connect("data/crypto_data.db")
query = "SELECT * FROM crypto_prices ORDER BY timestamp DESC"
df = pd.read_sql(query, conn)
df['timestamp'] = pd.to_datetime(df['timestamp']) # making stringified timestamp into real datetime object to perfrom actions (math)



# sidebar
st.sidebar.header("🔎 Filter Data")


coins = df['coin'].unique().tolist()
selected_coins = st.sidebar.multiselect("Select Coins", coins, default=coins)# filter by coins


min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)


filtered_df =  df[
    (df['coin'].isin(selected_coins)) & 
    (df['timestamp'].dt.date >= (start_date)) & 
    (df['timestamp'].dt.date <= (end_date)) 
]



# KPI cards
st.subheader("📊 Key Metrics")

if not filtered_df.empty:
    latest_timestamp = filtered_df['timestamp'].max()
    latest_data = filtered_df[filtered_df['timestamp'] == latest_timestamp]
    
    for coin in selected_coins:
        coin_data = latest_data[latest_data['coin'] == coin]
        if not coin_data.empty:
            price = coin_data['price_usd'].values[0]
            change = coin_data['change_24h_pct'].values[0]
            volume = coin_data['volume_24h'].values[0]


            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(f"💰 {coin.title()} Price", f"${price:,.2f}")

            with col2:
                st.metric(f"📈 24h Change (%)", f"{change:+.2f}%")
            
            with col3:
                st.metric(f"🔁 24h Volume", f"${volume/1e6:.2f}M")


# Price Table
st.subheader("🧾 Latest Prices")
st.dataframe(filtered_df.head(50), use_container_width=True)

# Download CSV
st.subheader("⬇️ Download Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='crypto_prices_filtered.csv',
    mime='text/csv'
)


st.subheader("📧 Send Report via Email")

email = st.text_input("Enter your email to receive the filtered report:")

if st.button("Send Email Report"):
    if not email:
        st.warning("Please enter a valid email.")
    elif filtered_df.empty:
        st.warning("No data to send. Please adjust your filters.")
    else:
        # Save temp CSV
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            filtered_df.to_csv(tmp.name, index=False)
            csv_path = tmp.name

        try:
            yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)
            yag.send(
                to=email,
                subject="Your Crypto Report",
                contents="Attached is your requested crypto price report.",
                attachments=csv_path
            )
            st.success(f"✅ Report sent to {email}!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")




# Price Trend Chart
st.subheader("📉 Price Trend Over Time")
if not filtered_df.empty:
    chart_data = filtered_df.pivot(index='timestamp', columns='coin', values='price_usd')
    st.line_chart(chart_data, use_container_width=True)

else:
    st.info("No data available for selected filters.")


# ----------------- Footer -------------------
st.markdown(f"""
<div class='footer'>
    🚀 Built with ❤️ by <b>You</b> | © {date.today().year} | <a href="https://github.com" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

# ----------------- Close Connection -------------------
conn.close()

