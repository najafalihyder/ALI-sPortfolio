import schedule
import time

from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_to_csv
from db import save_to_db
from email_report import send_email_report


def run_pipeline():
    raw_data = extract_crypto_data()
    df = transform_crypto_data(raw_data)
    load_to_csv(df)
    save_to_db(df)
    send_email_report()
   

run_pipeline()


schedule.every().hour.do(run_pipeline)
print("🔁 Scheduler started. Pipeline will run every hour.")

while True:
    schedule.run_pending()
    time.sleep(1)