# Downloading data from Yahoo Finance

import yfinance as yf
import pandas as pd
import sys

# tickers = yf.Tickers('AMZN MSFT GOOGL IBM ORCL CRM AVGO SAP BABA TCEHY BIDU DOCN NET FSLY AKAM RXT SNOW WDAY MDB TWLO')

# Choosing only cloud providers
ticker_string = 'AMZN MSFT GOOGL IBM ORCL CRM AVGO SAP BABA TCEHY BIDU DOCN NET FSLY AKAM RXT SNOW WDAY MDB TWLO'


try:
    print(f"Attempting to download data for {len(ticker_string.split())} tickers...")
    data = yf.download(ticker_string.split(), period='25y')
    
    if data.empty:
        print("Error: No data was downloaded. The API returned an empty dataset.")
        sys.exit(1)
        
    print(f"Successfully downloaded data with shape: {data.shape}")
    
    # Save the data
    try:
        data.to_csv('stock-analysis-project/data/raw/all_cloud_providers.csv')
        print("Data successfully saved to 'stock-analysis-project/data/raw/all_cloud_providers.csv'")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        sys.exit(1)
        
except Exception as e:
    print(f"Error downloading data from Yahoo Finance: {e}")
    sys.exit(1)
