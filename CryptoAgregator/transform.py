import pandas as pd
from datetime import datetime


def transform_crypto_data(raw_data: dict) -> pd.DataFrame:
    if not raw_data:
        print("❌ No data to transform")
        return pd.DataFrame()
    
    transfromed_data = []

    for coin, metrics in raw_data.items():
        transfromed_data.append({
            "coin": coin,
            "price_usd": metrics.get("usd"),
            "market_cap": metrics.get("usd_market_cap"),
            "volume_24h": metrics.get("usd_24h_vol"),
            "change_24h_pct": metrics.get("usd_24h_change"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        

    df = pd.DataFrame(transfromed_data)
    print("✅ Data transformed successfully")
    return df




