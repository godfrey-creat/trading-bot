import pandas as pd
from .ml_model import train_model, save_model
from utils.data_preprocessing import preprocess_data

def load_data(filepath):
    return pd.read_csv(filepath)

def train_and_save_model(data_file, model_file):
    data = load_data(data_file)
    X, y = data.drop(columns=['Close']), data['Close']
    X_preprocessed = preprocess_data(X)
    
    model = train_model(X_preprocessed, y)
    save_model(model, model_file)

# Example usage
# train_and_save_model('data/historical_data.csv', 'models/model_weights/trading_model.pkl')
