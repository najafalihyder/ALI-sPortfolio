import sqlite3
import pandas as pd



def query_db(sql_query, db_path="data/crypto_data.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df
