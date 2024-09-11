def backtest_strategy(strategy, historical_data):
    initial_cash = 10000
    cash = initial_cash
    holdings = 0
    
    for index, row in historical_data.iterrows():
        signal = strategy(row)
        
        if signal == 1 and cash > row['Close']:
            holdings += cash // row['Close']
            cash -= holdings * row['Close']
        
        elif signal == -1 and holdings > 0:
            cash += holdings * row['Close']
            holdings = 0
    
    final_value = cash + holdings * historical_data.iloc[-1]['Close']
    return final_value - initial_cash

# Example usage
# profit = backtest_strategy(simple_moving_average, historical_data)
# print(f"Profit from backtesting: {profit}")
