# Downloading data from Yahoo Finance

import yfinance as yf
import pandas as pd


tickers = yf.Tickers('AMZN MSFT GOOGL IBM ORCL CRM AVGO SAP BABA TCEHY BIDU DOCN NET FSLY AKAM RXT SNOW WDAY MDB TWLO')

ticker_string = 'AMZN MSFT GOOGL IBM ORCL CRM AVGO SAP BABA TCEHY BIDU DOCN NET FSLY AKAM RXT SNOW WDAY MDB TWLO'
data = yf.download(ticker_string.split(), period='1y')


data.to_csv('stock-analysis-project/data/raw/all_cloud_providers.csv')

