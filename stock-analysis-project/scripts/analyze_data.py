# analyze_data.py
import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime
from config import CLOUD_PROVIDERS, TICKERS, PROCESSED_DATA_PATH

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def calculate_technical_indicators(df):
    """Calculate technical indicators for each company."""
    # Group by company to calculate indicators separately for each
    grouped = df.groupby('Company')
    
    # Create a list to store DataFrames with indicators
    dfs_with_indicators = []
    
    for company, company_data in grouped:
        # Sort by date to ensure correct calculations
        company_data = company_data.sort_values('Date')
        
        # Add company name and service name if not already in data
        if 'CompanyName' not in company_data.columns:
            company_info = CLOUD_PROVIDERS.get(company, {'company': company, 'service': company})
            company_data['CompanyName'] = company_info['company']
            company_data['ServiceName'] = company_info['service']
        
        # Calculate moving averages
        company_data['SMA_20'] = company_data['Close'].rolling(window=20).mean()
        company_data['SMA_50'] = company_data['Close'].rolling(window=50).mean()
        company_data['SMA_200'] = company_data['Close'].rolling(window=200).mean()
        
        # Calculate exponential moving averages
        company_data['EMA_20'] = company_data['Close'].ewm(span=20, adjust=False).mean()
        
        # Calculate daily returns
        company_data['Daily_Return'] = company_data['Close'].pct_change() * 100
        
        # Calculate volatility (20-day rolling standard deviation of returns)
        company_data['Volatility_20d'] = company_data['Daily_Return'].rolling(window=20).std()
        
        # Calculate RSI (Relative Strength Index)
        delta = company_data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        
        rs = avg_gain / avg_loss
        company_data['RSI'] = 100 - (100 / (1 + rs))
        
        # Calculate MACD
        company_data['EMA_12'] = company_data['Close'].ewm(span=12, adjust=False).mean()
        company_data['EMA_26'] = company_data['Close'].ewm(span=26, adjust=False).mean()
        company_data['MACD'] = company_data['EMA_12'] - company_data['EMA_26']
        company_data['MACD_Signal'] = company_data['MACD'].ewm(span=9, adjust=False).mean()
        company_data['MACD_Histogram'] = company_data['MACD'] - company_data['MACD_Signal']
        
        # Add the DataFrame with indicators to our list
        dfs_with_indicators.append(company_data)
    
    # Combine all DataFrames
    result = pd.concat(dfs_with_indicators)
    return result

def calculate_performance_metrics(df):
    """Calculate performance metrics for each company."""
    # Group by company
    grouped = df.groupby('Company')
    
    # Initialize a dictionary to store performance results
    performance = {}
    
    for company, company_data in grouped:
        # Sort by date
        company_data = company_data.sort_values('Date')
        
        # Get company and service names
        company_name = company_data['CompanyName'].iloc[0] if 'CompanyName' in company_data else company
        service_name = company_data['ServiceName'].iloc[0] if 'ServiceName' in company_data else company
        
        # Calculate metrics only if we have enough data
        if len(company_data) > 20:
            # Get the most recent closing price
            latest_close = company_data['Close'].iloc[-1]
            
            # Calculate returns for different periods
            try:
                # 1-month return (approximately 21 trading days)
                month_ago_idx = -21 if len(company_data) >= 21 else 0
                month_ago_price = company_data['Close'].iloc[month_ago_idx]
                month_return = ((latest_close / month_ago_price) - 1) * 100
                
                # 3-month return (approximately 63 trading days)
                three_month_ago_idx = -63 if len(company_data) >= 63 else 0
                three_month_ago_price = company_data['Close'].iloc[three_month_ago_idx]
                three_month_return = ((latest_close / three_month_ago_price) - 1) * 100
                
                # 6-month return (approximately 126 trading days)
                six_month_ago_idx = -126 if len(company_data) >= 126 else 0
                six_month_ago_price = company_data['Close'].iloc[six_month_ago_idx]
                six_month_return = ((latest_close / six_month_ago_price) - 1) * 100
                
                # Volatility (standard deviation of daily returns)
                volatility = company_data['Daily_Return'].std()
                
                # Maximum drawdown
                cum_returns = (1 + company_data['Daily_Return'] / 100).cumprod()
                running_max = cum_returns.cummax()
                drawdown = ((cum_returns) / running_max - 1) * 100
                max_drawdown = drawdown.min()
                
                # Store the results
                performance[company] = {
                    'company_name': company_name,
                    'service_name': service_name,
                    'latest_close': latest_close,
                    'month_return': month_return,
                    'three_month_return': three_month_return,
                    'six_month_return': six_month_return,
                    'volatility': volatility,
                    'max_drawdown': max_drawdown,
                    'data_points': len(company_data)
                }
            except Exception as e:
                print(f"Error calculating performance for {service_name}: {e}")
                performance[company] = {
                    'company_name': company_name,
                    'service_name': service_name,
                    'error': str(e)
                }
    
    # Convert to DataFrame
    performance_df = pd.DataFrame.from_dict(performance, orient='index')
    return performance_df

def analyze_correlations(df):
    """Analyze correlations between different companies' close prices."""
    # Pivot the data to get closing prices for each company across dates
    pivot_df = df.pivot_table(index='Date', columns='Company', values='Close')
    
    # Calculate correlation matrix
    correlation_matrix = pivot_df.corr()
    
    # Create a version with service names for display
    service_name_map = {}
    for ticker in correlation_matrix.columns:
        info = CLOUD_PROVIDERS.get(ticker, {'company': ticker, 'service': ticker})
        service_name_map[ticker] = info['service']
    
    display_corr = correlation_matrix.copy()
    display_corr.columns = [service_name_map.get(col, col) for col in display_corr.columns]
    display_corr.index = [service_name_map.get(idx, idx) for idx in display_corr.index]
    
    return correlation_matrix, display_corr

def identify_trends(df):
    """Identify trends for each company based on moving averages."""
    # Create a copy to avoid modifying the original
    trend_df = df.copy()
    
    # Create trend column
    conditions = [
        (trend_df['Close'] > trend_df['SMA_50']) & (trend_df['SMA_50'] > trend_df['SMA_200']),
        (trend_df['Close'] < trend_df['SMA_50']) & (trend_df['SMA_50'] < trend_df['SMA_200']),
    ]
    choices = ['Uptrend', 'Downtrend']
    trend_df['Trend'] = np.select(conditions, choices, default='Sideways')
    
    # Count trends by company
    trend_counts = trend_df.groupby(['Company', 'Trend']).size().unstack(fill_value=0)
    
    # Add company name and service name columns
    trend_counts_with_names = trend_counts.reset_index()
    trend_counts_with_names['CompanyName'] = trend_counts_with_names['Company'].apply(
        lambda x: CLOUD_PROVIDERS.get(x, {'company': x})['company']
    )
    trend_counts_with_names['ServiceName'] = trend_counts_with_names['Company'].apply(
        lambda x: CLOUD_PROVIDERS.get(x, {'service': x})['service']
    )
    trend_counts_with_names = trend_counts_with_names.set_index('Company')
    
    # Calculate the percentage of each trend
    for trend in trend_counts.columns:
        trend_counts_with_names[f'{trend}_pct'] = (trend_counts[trend] / trend_counts.sum(axis=1) * 100).round(2)
    
    return trend_df, trend_counts_with_names

def main():
    try:
        # Load the processed data
        print(f"Loading data from {PROCESSED_DATA_PATH}")
        df = pd.read_csv(PROCESSED_DATA_PATH)
        
        # Convert Date to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        print(f"Loaded data with shape: {df.shape}")
        
        # Ensure results directories exist
        ensure_directory_exists('stock-analysis-project/data/analyzed')
        ensure_directory_exists('stock-analysis-project/results/reports')
        
        # Calculate technical indicators
        print("Calculating technical indicators...")
        df_with_indicators = calculate_technical_indicators(df)
        
        # Save the data with indicators
        indicators_path = 'stock-analysis-project/data/analyzed/data_with_indicators.csv'
        df_with_indicators.to_csv(indicators_path, index=False)
        print(f"Data with indicators saved to {indicators_path}")
        
        # Calculate performance metrics
        print("Calculating performance metrics...")
        performance_df = calculate_performance_metrics(df_with_indicators)
        
        # Save performance metrics
        performance_path = 'stock-analysis-project/data/analyzed/performance_metrics.csv'
        performance_df.to_csv(performance_path)
        print(f"Performance metrics saved to {performance_path}")
        
        # Calculate correlations
        print("Analyzing correlations...")
        correlation_matrix, display_corr = analyze_correlations(df)
        
        # Save correlation matrices
        correlation_path = 'stock-analysis-project/data/analyzed/correlation_matrix.csv'
        display_correlation_path = 'stock-analysis-project/data/analyzed/display_correlation_matrix.csv'
        correlation_matrix.to_csv(correlation_path)
        display_corr.to_csv(display_correlation_path)
        print(f"Correlation matrices saved to {correlation_path} and {display_correlation_path}")
        
        # Identify trends
        print("Identifying trends...")
        trend_df, trend_counts = identify_trends(df_with_indicators)
        
        # Save trend analysis
        trends_path = 'stock-analysis-project/data/analyzed/trend_analysis.csv'
        trend_counts.to_csv(trends_path)
        print(f"Trend analysis saved to {trends_path}")
        
        # Generate a summary report
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get top 5 performers by 3-month return
        top_performers = performance_df.sort_values('three_month_return', ascending=False).head(5)
        
        # Format top performers with service names
        top_performers_str = "\n".join([
            f"- {row['service_name']} ({index}): {row['three_month_return']:.2f}%" 
            for index, row in top_performers.iterrows() if 'three_month_return' in row
        ])
        
        # Format trend analysis with service names
        trend_analysis_str = "\n".join([
            f"- {row['ServiceName']} ({company}): " +
            f"{row['Uptrend']} uptrend days, {row['Downtrend']} downtrend days, {row['Sideways']} sideways days"
            for company, row in trend_counts.iterrows()
        ])
        
        report = f"""
        # Cloud Provider Stock Market Analysis Report
        
        Generated on: {timestamp}
        
        ## Dataset Summary
        - Total cloud providers analyzed: {df['Company'].nunique()}
        - Date range: {df['Date'].min()} to {df['Date'].max()}
        - Total data points: {len(df)}
        
        ## Performance Summary (Top 5 by 3-Month Return)
        
        {top_performers_str}
        
        ## Correlation Analysis
        
        A correlation matrix has been saved to {display_correlation_path}
        
        ## Trend Analysis
        
        {trend_analysis_str}
        
        ## Next Steps
        
        For more detailed analysis, check the visualization results in the 'results/figures' folder.
        """
        
        # Save the report
        report_path = 'stock-analysis-project/results/reports/analysis_summary.md'
        with open(report_path, 'w') as f:
            f.write(report)
        print(f"Analysis report saved to {report_path}")
        
        print("Analysis completed successfully!")
        return df_with_indicators, performance_df, correlation_matrix, trend_counts
        
    except Exception as e:
        print(f"Error in analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()