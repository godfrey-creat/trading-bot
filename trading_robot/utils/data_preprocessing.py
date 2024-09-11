from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def preprocess_data(df):
    df.fillna(method='ffill', inplace=True)
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)
    
    return scaled_df

# Example usage
# preprocessed_data = preprocess_data(historical_data)
