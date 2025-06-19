import requests
import pandas as pd
from config import API_BASE_URL

def fetch_coins_list() -> pd.DataFrame:
    """Fetch the list of available coins from CoinGecko"""
    url = f"{API_BASE_URL}/coins/list"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"[ERROR] fetch_coins_list: {e}")
        return pd.DataFrame()



def fetch_global_market_data(vs_currency: str = "usd", top_n: int = 100) -> pd.DataFrame:
    """Fetch top N coins' market data sorted by market cap"""
    url = f"{API_BASE_URL}/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "sparkline": "false"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        print(f"[ERROR] fetch_global_market_data: {e}")
        return pd.DataFrame()



def fetch_selected_coins_data(vs_currency: str, coin_ids: list) -> pd.DataFrame:
    """Fetch market data for selected coin IDs"""
    url = f"{API_BASE_URL}/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        print(f"[ERROR] fetch_selected_coins_data: {e}")
        return pd.DataFrame()



def fetch_coin_market_chart(coin_id, vs_currency="usd", days=30):
    """Fetch historical price data for a single coin"""
    url = f"{API_BASE_URL}/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "prices" in data:
            return data["prices"]
        else:
            raise ValueError(f"No 'prices' key in API response for {coin_id}")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            raise RuntimeError(f"API rate limit hit (429) for {coin_id}")
        raise RuntimeError(f"HTTP error {response.status_code} for {coin_id}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error for {coin_id}: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error for {coin_id}: {str(e)}")
