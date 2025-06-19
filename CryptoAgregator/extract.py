import requests
import json
import os
from datetime import datetime

def extract_crypto_data(save_raw=True) -> dict:

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,binancecoin",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            print("✅ Data fetched successfully")
        else:
            print("❌ API Error:", response.text)
            return {}



        if save_raw:
            os.makedirs("data/raw", exist_ok=True)
            filename = f"data/raw/crypto_raw_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"📝 Raw data saved to: {filename}")
        
        return data
    except Exception as e:
        print("❌ Exception occurred while fetching data:", e)
        return {}






