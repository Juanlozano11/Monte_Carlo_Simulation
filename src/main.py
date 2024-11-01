## run the file : python3 src/main.py

from MonteCarlo import MonteCarloSimulator
import matplotlib.pyplot as plt

def main():
    mc_simulator = MonteCarloSimulator(S0=100, K=100, T=1.0, r=0.05, sigma=0.2, M=50, I=10000)
    S = mc_simulator.simulate_asset_paths()

    # Calculate option price
    price = mc_simulator.calculate_option_price(S)
    print(f"Estimated price of the European option: {price:.2f}")

    # Optional: Plot the first 100 asset price paths
    plt.figure(figsize=(10, 6))
    plt.plot(S[:, :100])  # Only plot the first 100 simulation paths
    plt.title('Monte Carlo Simulation of Asset Price Paths')
    plt.xlabel('Time Steps')
    plt.ylabel('Asset Price')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
