# data_fetcher.py

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

def fetch_exchange_rate_data(from_currency, to_currency, api_key, start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    symbol = f"{from_currency}/{to_currency}"
    data = web.DataReader(symbol, "av-forex-daily", start=start, end=end, api_key=api_key)
    return data['close']

def calculate_initial_conditions(closing_rates):
    S0 = closing_rates.mean()  # Initial exchange rate (average closing rate)
    sigma = closing_rates.std()  # Volatility estimate based on historical data
    return S0, sigma
