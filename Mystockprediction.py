import yfinance as yf
import boto3
import pandas as pd
from datetime import datetime
import io

# ---- CONFIG ----
TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
BUCKET  = "stockprediction-datalake-fjose"
PERIOD  = "5y"
# ----------------

s3 = boto3.client("s3", region_name="eu-west-2", verify=False)

for ticker in TICKERS:
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, period=PERIOD, interval="1d")
    df.reset_index(inplace=True)
    
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    key = f"raw/{ticker}/{datetime.today().strftime('%Y-%m-%d')}.csv"
    s3.put_object(Bucket=BUCKET, Key=key, Body=csv_buffer.getvalue())
    print(f"  ✅ {ticker} uploaded to s3://{BUCKET}/{key}")

print("\nAll done!")


