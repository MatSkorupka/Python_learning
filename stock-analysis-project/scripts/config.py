# config.py
# Configuration for the stock market analysis project

# Cloud provider mapping: ticker symbol -> company and service names
CLOUD_PROVIDERS = {
    'AMZN': {'company': 'Amazon', 'service': 'Amazon Web Services (AWS)'},
    'MSFT': {'company': 'Microsoft', 'service': 'Microsoft Azure'},
    'GOOGL': {'company': 'Alphabet', 'service': 'Google Cloud Platform (GCP)'},
    'IBM': {'company': 'IBM', 'service': 'IBM Cloud'},
    'ORCL': {'company': 'Oracle', 'service': 'Oracle Cloud'},
    'CRM': {'company': 'Salesforce', 'service': 'Salesforce Cloud'},
    'AVGO': {'company': 'Broadcom', 'service': 'VMware Cloud'},
    'SAP': {'company': 'SAP', 'service': 'SAP Cloud Platform'},
    'BABA': {'company': 'Alibaba', 'service': 'Alibaba Cloud'},
    'TCEHY': {'company': 'Tencent', 'service': 'Tencent Cloud'},
    'BIDU': {'company': 'Baidu', 'service': 'Baidu AI Cloud'},
    'DOCN': {'company': 'DigitalOcean', 'service': 'DigitalOcean'},
    'NET': {'company': 'Cloudflare', 'service': 'Cloudflare'},
    'FSLY': {'company': 'Fastly', 'service': 'Fastly Edge Cloud'},
    'AKAM': {'company': 'Akamai', 'service': 'Akamai Cloud Computing'},
    'RXT': {'company': 'Rackspace', 'service': 'Rackspace Technology'},
    'SNOW': {'company': 'Snowflake', 'service': 'Snowflake Data Cloud'},
    'WDAY': {'company': 'Workday', 'service': 'Workday Cloud Platform'},
    'MDB': {'company': 'MongoDB', 'service': 'MongoDB Atlas'},
    'TWLO': {'company': 'Twilio', 'service': 'Twilio Cloud Communications'}
}

# List of ticker symbols for cloud providers to analyze
TICKERS = list(CLOUD_PROVIDERS.keys())

# Time period to download data for
TIME_PERIOD = '30y'  # 30 years of data

# Paths for data storage
RAW_DATA_PATH = 'stock-analysis-project/data/raw/all_cloud_providers.csv'
PROCESSED_DATA_PATH = 'stock-analysis-project/data/processed/stock_data_with_real_dates.csv'
ANALYZED_DATA_PATH = 'stock-analysis-project/data/analyzed/data_with_indicators.csv'

# Technical analysis parameters
MOVING_AVERAGE_PERIODS = [20, 50, 200]
RSI_PERIOD = 14
MACD_PARAMS = {
    'fast_period': 12,
    'slow_period': 26,
    'signal_period': 9
}