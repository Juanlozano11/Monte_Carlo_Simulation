import numpy as np

def geometric_brownian_motion(S0, r, sigma, T, M, I):
    """
    Generate asset price paths following a geometric Brownian motion model.

    Parameters:
    S0 : float
        Initial asset price
    r : float
        Risk-free interest rate
    sigma : float
        Volatility of the asset
    T : float
        Time to maturity in years
    M : int
        Number of time steps
    I : int
        Number of simulations

    Returns:
    numpy.ndarray
        Simulated asset price paths
    """
    dt = T / M  # Time step size
    Z = np.random.standard_normal((M + 1, I))  # Standard normally distributed random variables
    S = np.zeros_like(Z)
    S[0] = S0
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[t])
    return S

def calculate_european_option_price(S, K, r, T):
    """
    Calculate the price of a European call option using Monte Carlo simulation.

    Parameters:
    S : numpy.ndarray
        Simulated asset price paths
    K : float
        Strike price of the option
    r : float
        Risk-free interest rate
    T : float
        Time to maturity in years

    Returns:
    float
        Estimated price of the European option
    """
    payoff = np.maximum(S[-1] - K, 0)
    C0 = np.exp(-r * T) * np.sum(payoff) / len(payoff)
    return C0
