def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def rsi_strategy(data, rsi_buy=30, rsi_sell=70):
    data['RSI'] = calculate_rsi(data)
    
    # Generate buy/sell signals
    data['Signal'] = 0
    data['Signal'][data['RSI'] < rsi_buy] = 1  # Buy
    data['Signal'][data['RSI'] > rsi_sell] = -1  # Sell

    data['Position'] = data['Signal'].diff()
    return data

# Example usage
# rsi_signals = rsi_strategy(historical_data)
