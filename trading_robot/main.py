# main.py

from bot.trader_bot import TradingBot
from strategies.simple_moving_average import simple_moving_average
from data.live_data_feed import get_live_data
from config import API_KEYS, TRADING_CONFIG

def main():
    symbol = TRADING_CONFIG['symbol']
    api_key = API_KEYS['alpha_vantage']
    
    # Fetch live data
    try:
        live_data = get_live_data(symbol, api_key)
    except ValueError as e:
        print(f"Error fetching live data: {e}")
        return
    
    # Initialize and execute the bot with the chosen strategy (e.g., SMA)
    bot = TradingBot(simple_moving_average)
    signal = bot.execute(live_data)
    print(live_data.head())  # To see if 'Close' column exists

    
    if signal == 1:
        bot.buy()
    elif signal == -1:
        bot.sell()
    else:
        print("No signal to trade.")

if __name__ == "__main__":
    main()
