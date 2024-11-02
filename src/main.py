## run the file : python3 src/main.py CQGKZTRMUJP5O4AC

# main.py

import numpy as np
import matplotlib.pyplot as plt
from data_fetcher import fetch_exchange_rate_data, calculate_initial_conditions
from MonteCarlo import MonteCarloSimulator

def main():
    api_key = 'CQGKZTRMUJP5O4AC'  # Replace with your actual API key
    closing_rates = fetch_exchange_rate_data('USD', 'EUR', api_key, start_year=2020, end_year=2021)
    S0, sigma = calculate_initial_conditions(closing_rates)

    # Run the Monte Carlo simulation for the USD/EUR exchange rate
    mc_simulator = MonteCarloSimulator(S0=S0, K=S0 * 1.05, T=1, r=0.02, sigma=sigma, M=50, I=10000)
    simulated_rates = mc_simulator.simulate_asset_paths()

    # Calculate the average path across all simulations
    average_path = np.mean(simulated_rates, axis=1)  # Average over all simulations for each time step

    # Plot each simulated path with a unique color and higher transparency
    plt.figure(figsize=(10, 6))
    for i in range(100):  # Plot only the first 100 paths for readability
        plt.plot(simulated_rates[:, i], linewidth=0.8, alpha=0.3)  # Each path is more transparent

    # Plot the expected path in red with a bolder line
    plt.plot(average_path, color='red', linewidth=2, label="Expected Path")
    
    # Adding title and labels
    plt.title('Monte Carlo Simulation of USD/EUR Exchange Rate Paths')
    plt.xlabel('Time Steps')
    plt.ylabel('Exchange Rate (USD/EUR)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
