from strategies.simple_moving_average import simple_moving_average
from strategies.rsi_strategy import rsi_strategy

class TradingBot:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        signals = self.strategy(data)
        return signals['Signal'].iloc[-1]

    def buy(self):
        print("Buying asset")

    def sell(self):
        print("Selling asset")

# Example usage:
# bot = TradingBot(simple_moving_average)
# signal = bot.execute(data)
# if signal == 1:
#     bot.buy()
# elif signal == -1:
#     bot.sell()
