import requests

class BrokerAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def place_order(self, symbol, quantity, order_type='buy'):
        # Placeholder for API request to broker
        print(f"Placing {order_type} order for {quantity} shares of {symbol}")

# Example usage
# api = BrokerAPI('your_api_key')
# api.place_order('AAPL', 10, 'buy')
