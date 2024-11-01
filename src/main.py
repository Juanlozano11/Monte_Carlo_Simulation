## run the file : python3 src/main.py

# main.py

from data_fetcher import fetch_stock_data_av, calculate_initial_conditions
from MonteCarlo import MonteCarloSimulator
import matplotlib.pyplot as plt

def main():
    api_key = 'CQGKZTRMUJP5O4AC'  # Your Alpha Vantage API Key
    closing_prices = fetch_stock_data_av('AAPL', api_key, 2020, 2021)
    S0, sigma = calculate_initial_conditions(closing_prices)
    
    mc_simulator = MonteCarloSimulator(S0=S0, K=100, T=1, r=0.05, sigma=sigma, M=50, I=10000)
    simulated_prices = mc_simulator.simulate_asset_paths()
    estimated_price = mc_simulator.calculate_option_price(simulated_prices)
    
    print(f"Estimated option price: {estimated_price}")
    
    # Optional: Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(simulated_prices[:, :100])  # Plot the first 100 simulation paths
    plt.title('Monte Carlo Simulation of Asset Price Paths')
    plt.xlabel('Time Steps')
    plt.ylabel('Asset Price')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
