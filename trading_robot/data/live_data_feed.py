import requests
import pandas as pd

def get_live_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if 'Time Series (1min)' not in data:
        raise ValueError(f"Error fetching data for {symbol}: {data}")
    
    df = pd.DataFrame.from_dict(data['Time Series (1min)'], orient='index', dtype=float)
    df.index = pd.to_datetime(df.index)
    return df

# Example usage
# live_data = get_live_data('AAPL', 'your_api_key')
# print(live_data.head())

