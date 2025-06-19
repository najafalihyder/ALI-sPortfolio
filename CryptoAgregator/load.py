import os
import pandas as pd
from datetime import datetime

def load_to_csv(df: pd.DataFrame, folder: str = "data/processed") -> str:
    if df.empty:
        print("⚠️ Empty DataFrame — not saving.")
        return ""

    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/crypto_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    df.to_csv(filename, index=False)

    print(f"✅ Data saved to CSV: {filename}")
    return filename






