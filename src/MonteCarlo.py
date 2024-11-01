import numpy as np

class MonteCarloSimulator:
    def __init__(self, S0, K, T, r, sigma, M, I):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.M = M
        self.I = I
        self.dt = T / M

    def simulate_asset_paths(self):
        Z = np.random.standard_normal((self.M + 1, self.I))
        S = np.zeros_like(Z)
        S[0] = self.S0
        for t in range(1, self.M + 1):
            S[t] = S[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + 
                                     self.sigma * np.sqrt(self.dt) * Z[t])
        return S

    def calculate_option_price(self, S):
        payoff = np.maximum(S[-1] - self.K, 0)
        option_price = np.exp(-self.r * self.T) * np.mean(payoff)
        return option_price
