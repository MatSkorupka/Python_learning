import pandas as pd
import os

# Read the CSV file
df = pd.read_csv('stock-analysis-project/data/raw/all_cloud_providers.csv')

# Ensure the processed directory exists
os.makedirs('stock-analysis-project/data/processed', exist_ok=True)

# Print the first few rows to understand the structure
print("First few rows of the original data:")
print(df.head())
print("\nColumn names:", df.columns.tolist())

# Find the date column
# First, check if there's a column named 'Date'
if 'Date' in df.columns:
    date_column = 'Date'
# Otherwise, try the first column which is often a date
elif df.columns[0].lower() in ['date', 'unnamed: 0']:
    date_column = df.columns[0]
else:
    # Look for a column that has date-like values
    date_column = None
    for col in df.columns:
        try:
            # Check a few values to see if they're dates
            sample_values = df[col].dropna().head(5)
            if sample_values.empty:
                continue
            
            # Try to convert to datetime
            dates = pd.to_datetime(sample_values, errors='coerce')
            if not dates.isna().all():
                date_column = col
                print(f"Found date column: {col}")
                break
        except:
            continue

if date_column:
    print(f"Using {date_column} as the date source")
    
    # Create a new DataFrame with the correct structure
    cleaned_df = pd.DataFrame(columns=['Date', 'Company', 'Close', 'High', 'Low', 'Open', 'Volume'])
    
    # Convert date column to datetime, handling errors
    df['proper_date'] = pd.to_datetime(df[date_column], errors='coerce')
    
    # Remove rows with invalid dates
    valid_dates_df = df[~df['proper_date'].isna()].copy()
    print(f"Found {len(valid_dates_df)} rows with valid dates")
    
    # Define company tickers
    tickers = ['AMZN', 'MSFT', 'GOOGL', 'IBM', 'ORCL', 'CRM', 'AVGO', 'SAP', 
               'BABA', 'TCEHY', 'BIDU', 'DOCN', 'NET', 'FSLY', 'AKAM', 
               'RXT', 'SNOW', 'WDAY', 'MDB', 'TWLO']
    
    # List to store rows that will be added to the cleaned_df
    rows_to_add = []
    
    # Process each row with a valid date
    for idx, row in valid_dates_df.iterrows():
        date = row['proper_date']
        
        # Find columns for each company's financial data
        for i, ticker in enumerate(tickers):
            company_data = {'Date': date, 'Company': ticker}
            has_data = False
            
            # Look for financial data columns for this company
            for metric in ['Close', 'High', 'Low', 'Open', 'Volume']:
                # Try both naming patterns: "Close" and "Close.1", "Close.2", etc.
                col_name = f"{metric}" if i == 0 else f"{metric}.{i}"
                
                if col_name in df.columns and pd.notna(row[col_name]):
                    value = row[col_name]
                    # Skip if the value is a string that matches a ticker
                    if not isinstance(value, str) or value not in tickers:
                        # Convert to numeric if possible
                        try:
                            value = pd.to_numeric(value)
                        except:
                            pass
                        
                        company_data[metric] = value
                        has_data = True
            
            # Only add rows that have at least some financial data
            if has_data:
                rows_to_add.append(company_data)
    
    # Use concat 
    if rows_to_add:
        cleaned_df = pd.concat([cleaned_df, pd.DataFrame(rows_to_add)], ignore_index=True)
    
    # Add an ID column
    cleaned_df.insert(0, 'ID', range(len(cleaned_df)))
    
    # Sort by date and company
    cleaned_df = cleaned_df.sort_values(['Date', 'Company']).reset_index(drop=True)
    
    # Save to CSV
    output_path = 'stock-analysis-project/data/processed/stock_data_with_real_dates.csv'
    cleaned_df.to_csv(output_path, index=False)
    print(f"\nData with real dates saved to {output_path}")
    print(f"Shape: {cleaned_df.shape}")
    print("\nFirst few rows:")
    print(cleaned_df.head())
else:
    print("Could not find a suitable date column in the data.")