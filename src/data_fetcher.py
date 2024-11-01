# data_fetcher.py

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

def fetch_stock_data_av(symbol, api_key, start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    data = web.DataReader(symbol, "av-daily", start, end, api_key=api_key)
    return data['close']

def calculate_initial_conditions(closing_prices):
    S0 = closing_prices.mean()  # Calculate the average closing price as initial stock price
    sigma = closing_prices.std()  # Standard deviation of closing prices as volatility estimate
    return S0, sigma
