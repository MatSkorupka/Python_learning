# download_data.py
# Downloading data from Yahoo Finance

import yfinance as yf
import pandas as pd
import sys
import os
from config import TICKERS, TIME_PERIOD, RAW_DATA_PATH, CLOUD_PROVIDERS

def ensure_directory_exists(file_path):
    """Create directory for file if it doesn't exist."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def main():
    # Convert ticker list to string for yfinance
    ticker_string = ' '.join(TICKERS)
    
    try:
        print(f"Attempting to download data for {len(TICKERS)} cloud providers...")
        print("Cloud providers to download:")
        for ticker in TICKERS:
            company_info = CLOUD_PROVIDERS.get(ticker, {'company': ticker, 'service': ticker})
            print(f"  - {ticker}: {company_info['service']} ({company_info['company']})")
        
        data = yf.download(ticker_string.split(), period=TIME_PERIOD)
        
        if data.empty:
            print("Error: No data was downloaded. The API returned an empty dataset.")
            sys.exit(1)
            
        print(f"Successfully downloaded data with shape: {data.shape}")
        
        # Ensure directory exists
        ensure_directory_exists(RAW_DATA_PATH)
        
        # Save the data
        try:
            data.to_csv(RAW_DATA_PATH)
            print(f"Data successfully saved to '{RAW_DATA_PATH}'")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
            sys.exit(1)
        
        return data
            
    except Exception as e:
        print(f"Error downloading data from Yahoo Finance: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()