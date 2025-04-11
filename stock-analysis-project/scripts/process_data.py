# process_data.py
import pandas as pd
import numpy as np
import os
import sys
from config import CLOUD_PROVIDERS, TICKERS, RAW_DATA_PATH, PROCESSED_DATA_PATH

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def process_raw_data():
    """Process and clean the raw stock data."""
    try:
        # Read the raw CSV file without header
        print(f"Reading raw data from {RAW_DATA_PATH}")
        raw_df = pd.read_csv(RAW_DATA_PATH, header=None)
        
        print(f"Raw data shape: {raw_df.shape}")
        
        # First row contains column headers
        headers = raw_df.iloc[0].tolist()
        
        # Second row contains ticker symbols
        tickers_row = raw_df.iloc[1].tolist()
        
        # Create a mapping of column indices to (metric, ticker) pairs
        column_mapping = {}
        for col_idx, header in enumerate(headers):
            if col_idx == 0:  # Skip the first column which contains "Price"
                continue
                
            ticker = tickers_row[col_idx]
            if ticker in TICKERS:  # Only include tickers we're interested in
                column_mapping[col_idx] = (header, ticker)
        
        # Create a list to hold the processed data
        processed_data = []
        
        # Process each data row starting from row 4 (index 3)
        for row_idx in range(3, len(raw_df)):
            row = raw_df.iloc[row_idx]
            
            # Get the date from the first column
            date_str = row[0]
            if not isinstance(date_str, str) or not date_str:
                continue  # Skip rows without a date
                
            try:
                # Convert to datetime
                date = pd.to_datetime(date_str)
                
                # Create a dict to group data by ticker
                ticker_data = {ticker: {} for ticker in TICKERS}
                
                # Extract data for each column
                for col_idx, (metric, ticker) in column_mapping.items():
                    if ticker in ticker_data:
                        value = row[col_idx]
                        if pd.notna(value) and value != "":
                            # Try to convert to float
                            try:
                                ticker_data[ticker][metric] = float(value)
                            except:
                                pass  # Skip if conversion fails
                
                # Create a record for each ticker with data
                for ticker, metrics in ticker_data.items():
                    # Skip tickers with no data for this date
                    if not metrics:
                        continue
                        
                    # Get company and service names
                    company_info = CLOUD_PROVIDERS.get(ticker, {'company': ticker, 'service': ticker})
                    
                    # Create the basic record
                    record = {
                        'Date': date,
                        'Company': ticker,
                        'CompanyName': company_info['company'],
                        'ServiceName': company_info['service']
                    }
                    
                    # Add each metric
                    for metric, value in metrics.items():
                        record[metric] = value
                    
                    # Add to the processed data list
                    processed_data.append(record)
                    
            except Exception as e:
                print(f"Error processing row {row_idx}: {e}")
                continue
        
        # Create DataFrame from processed data
        result_df = pd.DataFrame(processed_data)
        
        # Check if we have any data
        if result_df.empty:
            print("ERROR: No data was extracted. Check the file format.")
            return None
        
        # Add ID column
        result_df.reset_index(inplace=True)
        result_df.rename(columns={'index': 'ID'}, inplace=True)
        
        # Sort by date and company
        result_df = result_df.sort_values(['Date', 'Company']).reset_index(drop=True)
        
        # Print summary
        print("\nProcessed data summary:")
        print(f"Date range: {result_df['Date'].min()} to {result_df['Date'].max()}")
        print(f"Number of companies: {result_df['Company'].nunique()}")
        print(f"Total records: {len(result_df)}")
        
        # Save to CSV
        result_df.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"\nProcessed data saved to {PROCESSED_DATA_PATH}")
        print("\nFirst few rows of processed data:")
        print(result_df.head())
        
        return result_df
        
    except Exception as e:
        print(f"Error processing data: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    processed_data = process_raw_data()
    if processed_data is not None:
        print("Data processing completed successfully!")
        return processed_data
    else:
        print("Data processing failed.")
        return None

if __name__ == "__main__":
    main()