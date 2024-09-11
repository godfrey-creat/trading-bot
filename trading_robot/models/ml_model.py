from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def build_model():
    return RandomForestRegressor(n_estimators=100)

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_model()
    model.fit(X_train, y_train)
    
    # Model evaluation
    score = model.score(X_test, y_test)
    print(f"Model Accuracy: {score:.2f}")
    
    return model

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)

# Example usage
# model = train_model(X, y)
# save_model(model, "models/model_weights/random_forest_model.pkl")
