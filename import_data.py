import pandas as pd

# File Paths
file_1 = r"C:\Users\Preeti\stock project\aapl_2016_2020.csv"
file_2 = r"C:\Users\Preeti\stock project\aapl_2021_2023.csv"

# Define Correct Data Types
dtype_dict = {
    "C_DELTA": "float64",
    "C_GAMMA": "float64",
    "C_VEGA": "float64",
    "C_THETA": "float64",
    "C_RHO": "float64",
    "C_IV": "float64",
    "C_VOLUME": "float64",
    "C_LAST": "float64",
    "C_BID": "float64",
    "C_ASK": "float64",
    "P_BID": "float64",
    "P_ASK": "float64",
    "P_LAST": "float64",
    "P_DELTA": "float64",
    "P_GAMMA": "float64",
    "P_VEGA": "float64",
    "P_THETA": "float64",
    "P_RHO": "float64",
    "P_IV": "float64",
    "P_VOLUME": "float64",
}

# Read CSV with dtype and low_memory=False
df1 = pd.read_csv(file_1, dtype=dtype_dict, low_memory=False)
df2 = pd.read_csv(file_2, dtype=dtype_dict, low_memory=False)

# Combine Both DataFrames
df = pd.concat([df1, df2], ignore_index=True)

# Check Data
print(df.head())
print(df.info())


import numpy as np
import scipy.stats as si

def calculate_greeks(S, K, T, r, sigma):
    """
    Calculate option Greeks: Delta, Gamma, Theta, Vega using Black-Scholes Model.
    S: Current stock price
    K: Strike price
    T: Time to expiry (in years)
    r: Risk-free interest rate
    sigma: Volatility
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = si.norm.cdf(d1)  # N(d1)
    gamma = si.norm.pdf(d1) / (S * sigma * np.sqrt(T))  # N'(d1)
    vega = S * si.norm.pdf(d1) * np.sqrt(T)  # Vega
    theta = (-S * si.norm.pdf(d1) * sigma / (2 * np.sqrt(T)))  # Theta

    return delta, gamma, theta, vega


def trading_strategy(S, K, T, r, sigma):
    """
    Define an options trading strategy based on Greeks.
    """
    delta, gamma, theta, vega = calculate_greeks(S, K, T, r, sigma)

    if delta > 0.5 and vega > 20:
        return "BUY CALL OPTION"
    elif delta < -0.5 and vega > 20:
        return "BUY PUT OPTION"
    else:
        return "NO TRADE"

    # Example Test


decision = trading_strategy(150, 155, 30 / 365, 0.05, 0.2)
print("Trading Decision:", decision)
