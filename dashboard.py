import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)

    return delta, gamma, theta, vega


def calculate_profit_loss(S, K, premium):
    return max(S - K, 0) - premium


st.title("📈 Options Trading Strategy")

S = st.number_input("Stock Price", value=150.0)
K = st.number_input("Strike Price", value=155.0)
T = st.number_input("Days to Expiry", value=30) / 365
r = st.number_input("Risk-Free Rate", value=0.05)
sigma = st.number_input("Volatility", value=0.2)
premium = st.number_input("Option Premium", value=5.0)

delta, gamma, theta, vega = calculate_greeks(S, K, T, r, sigma)

st.subheader("📊 Option Greeks")
st.write(f"**Delta:** {delta:.4f}")
st.write(f"**Gamma:** {gamma:.4f}")
st.write(f"**Theta:** {theta:.4f}")
st.write(f"**Vega:** {vega:.4f}")

profit_loss = calculate_profit_loss(S, K, premium)
st.subheader("💰 Potential Profit/Loss")
st.write(f"Profit/Loss: ${profit_loss:.2f}")

st.subheader("📉 Greeks Visualization")
fig, ax = plt.subplots()
labels = ["Delta", "Gamma", "Theta", "Vega"]
values = [delta, gamma, theta, vega]
ax.bar(labels, values, color=['blue', 'red', 'green', 'orange'])
st.pyplot(fig)
