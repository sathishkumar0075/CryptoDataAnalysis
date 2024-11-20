import requests
import pandas as pd
import streamlit as st
import time

# -------------------------
# Fetch Cryptocurrency Data
# -------------------------
def fetch_crypto_data():
    """
    Fetches live data for the top 50 cryptocurrencies by market cap from the CoinGecko API.
    Returns:
        pandas.DataFrame: A dataframe containing cryptocurrency data.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return pd.DataFrame(data)[
        ["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
    ]

# -----------------
# Analyze the Data
# -----------------
def analyze_data(df):
    """
    Performs analysis on the cryptocurrency data.
    Args:
        df (pandas.DataFrame): The cryptocurrency data.
    Returns:
        tuple: Top 5 by market cap, average price, highest 24h change, lowest 24h change.
    """
    top_5 = df.nlargest(5, "market_cap")[["name", "market_cap"]]
    avg_price = df["current_price"].mean()
    highest_change = df.nlargest(1, "price_change_percentage_24h")[["name", "price_change_percentage_24h"]]
    lowest_change = df.nsmallest(1, "price_change_percentage_24h")[["name", "price_change_percentage_24h"]]
    return top_5, avg_price, highest_change, lowest_change

# --------------------------
# Streamlit App - Dashboard
# --------------------------
st.set_page_config(
    page_title="Live Cryptocurrency Dashboard",
    page_icon="📈",
    layout="wide",
)

# Page Title and Description
st.title("📈 Live Cryptocurrency Dashboard")
st.markdown("""
Stay updated with live cryptocurrency prices and insights!  
This dashboard fetches real-time data for the top 50 cryptocurrencies by market capitalization.
""")

# Sidebar Configuration
st.sidebar.header("⚙️ Dashboard Settings")
refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", min_value=30, max_value=600, value=300, step=30)
st.sidebar.markdown("---")
st.sidebar.markdown("💾 *Data Export*: The latest data is saved to Crypto_Live_Data.xlsx on every refresh.")

# Live Data Display
placeholder = st.empty()

while True:
    # Fetch and Analyze Data
    crypto_data = fetch_crypto_data()
    top_5, avg_price, highest_change, lowest_change = analyze_data(crypto_data)

    # Dynamic Dashboard Layout
    with placeholder.container():
        st.markdown("### 🔄 *Live Cryptocurrency Data*")
        st.dataframe(crypto_data.style.format({
            "current_price": "${:,.2f}",
            "market_cap": "${:,.2f}",
            "total_volume": "${:,.2f}",
            "price_change_percentage_24h": "{:+.2f}%"
        }))

        # Summary and Insights Section
        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🏆 Top 5 by Market Cap")
            st.dataframe(top_5.style.format({"market_cap": "${:,.2f}"}))

        with col2:
            st.subheader("💰 Average Price")
            st.metric("Average Price (USD)", f"${avg_price:,.2f}")

        with col3:
            st.subheader("📊 Price Changes (24h)")
            st.metric("Highest Change", f"{highest_change.iloc[0]['price_change_percentage_24h']:.2f}%", 
                      help=highest_change.iloc[0]['name'])
            st.metric("Lowest Change", f"{lowest_change.iloc[0]['price_change_percentage_24h']:.2f}%", 
                      help=lowest_change.iloc[0]['name'])

    # Export Data to Excel
    crypto_data.to_excel("Crypto_Live_Data.xlsx", index=False)

    # Footer Message
    st.sidebar.success(f"✅ Data updated! Next refresh in {refresh_rate} seconds.")
    time.sleep(refresh_rate)