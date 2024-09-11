import pandas as pd
import numpy as np

def simple_moving_average(data, short_window=40, long_window=100):
    """
    Calculate simple moving averages (SMA) and determine buy/sell signals.
    
    Args:
        data (pd.DataFrame): Stock data with 'Close' price column
        short_window (int): Window for the short-term moving average
        long_window (int): Window for the long-term moving average
    Returns:
        signal (int): 1 for buy, -1 for sell, 0 for hold
    """
    # Ensure 'Close' column exists
    if 'Close' not in data.columns:
        raise KeyError("Data does not contain 'Close' column.")
    
    # Calculate short-term and long-term moving averages
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Generate signals
    data['Signal'] = 0  # Default signal: hold
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, -1)

    # Return the last signal (buy, sell, or hold)
    return data['Signal'].iloc[-1]

