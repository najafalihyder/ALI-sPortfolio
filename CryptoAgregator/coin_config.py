import requests
import pandas as pd


def fetch_all_coin_ids():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        coins = response.json()
        df = pd.DataFrame(coins)
        return df #  id, symbol, name
    else:
        raise Exception("Failed to fetch coin list")

df = fetch_all_coin_ids()
print(df.head())