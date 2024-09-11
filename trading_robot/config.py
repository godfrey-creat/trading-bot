# config.py

# API Configuration
API_KEYS = {
    'alpha_vantage': 'your_alpha_vantage_api_key',
    'binance': 'your_binance_api_key',
    'broker': 'your_broker_api_key'
}

# Trading Configurations
TRADING_CONFIG = {
    'symbol': 'AAPL',  # Default trading symbol
    'trade_amount': 1000,  # Amount to trade in USD
    'trade_frequency': 'daily',  # Could be 'minute', 'hourly', 'daily', etc.
    'backtest_start': '2024-09-01',  # Backtesting start date
    'backtest_end': '2024-09-01'  # Backtesting end date
}

# Machine Learning Model Parameters
ML_MODEL_CONFIG = {
    'model_type': 'RandomForestRegressor',  # Model to use for predictions
    'train_test_split': 0.8,  # Train-test split ratio
    'n_estimators': 100,  # Number of trees in the random forest
    'random_state': 42  # Random seed for reproducibility
}

# Data Configuration
DATA_CONFIG = {
    'historical_data_file': 'data/historical_data.csv',  # Path to historical data file
    'live_data_api': 'alpha_vantage',  # Default API for live data
    'data_fetch_interval': '1min'  # Time interval for fetching live data (1min, 5min, daily, etc.)
}

# Logging Configuration
LOGGING_CONFIG = {
    'log_file': 'logs/trading_bot.log',  # Log file path
    'log_level': 'INFO'  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
}

# Trading Strategy Parameters
STRATEGY_CONFIG = {
    'sma': {
        'short_window': 40,  # Short window for Simple Moving Average
        'long_window': 100  # Long window for Simple Moving Average
    },
    'rsi': {
        'rsi_buy_threshold': 30,  # RSI buy threshold
        'rsi_sell_threshold': 70  # RSI sell threshold
    }
}
