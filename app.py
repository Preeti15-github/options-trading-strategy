from flask import Flask, request, jsonify
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)

    return {"Delta": delta, "Gamma": gamma, "Theta": theta, "Vega": vega}

@app.route('/trade', methods=['GET'])
def trade():
    S = float(request.args.get('S', 150))
    K = float(request.args.get('K', 155))
    T = float(request.args.get('T', 30)) / 365
    r = float(request.args.get('r', 0.05))
    sigma = float(request.args.get('sigma', 0.2))

    greeks = calculate_greeks(S, K, T, r, sigma)
    return jsonify(greeks)

if __name__ == '__main__':
    app.run(debug=True)
