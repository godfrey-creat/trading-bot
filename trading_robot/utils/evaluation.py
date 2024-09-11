import numpy as np

def evaluate_strategy(data):
    data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
    data['Strategy'] = data['Signal'].shift(1) * data['Returns']
    
    cumulative_return = data[['Returns', 'Strategy']].cumsum().apply(np.exp)
    
    # Return final cumulative returns
    return cumulative_return

# Example usage
# evaluation = evaluate_strategy(trading_signals)
