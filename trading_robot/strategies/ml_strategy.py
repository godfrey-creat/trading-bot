from models.ml_model import load_model

def ml_based_strategy(data, model_file='models/model_weights/trading_model.pkl'):
    model = load_model(model_file)
    
    X = data[['Open', 'High', 'Low', 'Volume']]
    predictions = model.predict(X)
    
    # Generate buy/sell signals based on predicted prices
    data['Prediction'] = predictions
    data['Signal'] = 0
    data['Signal'][data['Prediction'] > data['Close']] = 1  # Buy
    data['Signal'][data['Prediction'] < data['Close']] = -1  # Sell
    
    return data

# Example usage
# ml_signals = ml_based_strategy(historical_data)
