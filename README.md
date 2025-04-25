# Options Pricing Simulator

A Python library for options pricing and analysis using the Black-Scholes model. This library provides tools for calculating option prices, Greeks, and visualizing option payoffs.

## Features

- Black-Scholes option pricing for calls and puts
- Greeks calculations (Delta, Gamma, Theta, Vega, Rho)
- Payoff visualization for individual options and combined positions
- Clear and documented code with type hints and docstrings

## Installation

1. Clone the repository:
```bash
git clone https://github.com/reetmitra/options_simulator.git
cd options_simulator
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the test script to see the library in action:
```bash
python test_options.py
```

This will:
1. Calculate call and put option prices
2. Compute all Greeks for both options
3. Generate payoff diagrams (saved as PNG files)

### Example Code

```python
from black_scholes import black_scholes_call, black_scholes_put
from greeks import delta_call, gamma
from payoff_visualizer import plot_payoff

# Parameters
S = 100  # Stock price
K = 100  # Strike price
T = 1.0  # Time to expiration (years)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

# Calculate option price
call_price = black_scholes_call(S, K, T, r, sigma)
print(f"Call Option Price: ${call_price:.2f}")

# Calculate Greeks
delta = delta_call(S, K, T, r, sigma)
gamma = gamma(S, K, T, r, sigma)
print(f"Delta: {delta:.4f}")
print(f"Gamma: {gamma:.4f}")
```

## Project Structure

- `black_scholes.py`: Core Black-Scholes pricing functions
- `greeks.py`: Functions for calculating option Greeks
- `payoff_visualizer.py`: Tools for visualizing option payoffs
- `test_options.py`: Comprehensive test script with examples

## Dependencies

- NumPy
- SciPy
- Matplotlib

## License

This project is licensed under the MIT License - see the LICENSE file for details. 