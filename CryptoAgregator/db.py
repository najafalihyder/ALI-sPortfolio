import sqlite3
from pathlib import Path
import pandas as pd


def save_to_db(df: pd.DataFrame, db_path="data/crypto_data.db", table_name="crypto_prices"):


        # ensuring if the data folder exists if not then create it
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        # connecting to the database and creating with the db_path if not already created 
    conn = sqlite3.connect(db_path)

        # save dataframe to sql database (append if table exists and create automatically if table is absent )
    df.to_sql(table_name, conn, if_exists="append", index=False)

    conn.close()
    print(f"✅ Data saved to database: {db_path} → Table: {table_name}")



