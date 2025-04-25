# Options Pricing Simulator

A Python package for options pricing and analysis using the Black-Scholes model. This simulator provides tools for calculating option prices, Greeks, and visualizing payoff diagrams.

## Features

- Black-Scholes option pricing for calls and puts
- Calculation of option Greeks (Delta, Gamma, Theta, Vega, Rho)
- Payoff diagram visualization
- Sensitivity analysis tools
- Jupyter notebook examples

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/options_simulator.git
cd options_simulator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Option Pricing

```python
from src.black_scholes import black_scholes_call, black_scholes_put

# Define parameters
S = 100  # Current stock price
K = 100  # Strike price
T = 1.0  # Time to expiration (1 year)
r = 0.05  # Risk-free rate (5%)
sigma = 0.2  # Volatility (20%)

# Calculate option prices
call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)
```

### Calculating Greeks

```python
from src.greeks import delta_call, delta_put, gamma, theta_call, theta_put, vega, rho_call, rho_put

# Calculate Greeks for call option
call_delta = delta_call(S, K, T, r, sigma)
option_gamma = gamma(S, K, T, r, sigma)
call_theta = theta_call(S, K, T, r, sigma)
option_vega = vega(S, K, T, r, sigma)
call_rho = rho_call(S, K, T, r, sigma)
```

### Visualizing Payoffs

```python
from src.payoff_visualizer import plot_payoff, plot_combined_payoff
import numpy as np

# Create range of underlying prices
S_range = np.linspace(50, 150, 100)

# Plot call option payoff
plt = plot_payoff(S_range, K, call_price, option_type='call')
plt.show()

# Plot combined payoff
plt = plot_combined_payoff(S_range, K, call_price, put_price)
plt.show()
```

## Project Structure

```
options_simulator/
├── src/
│   ├── black_scholes.py    # Core pricing functions
│   ├── greeks.py           # Greeks calculations
│   └── payoff_visualizer.py # Payoff visualization
├── notebooks/
│   └── main.ipynb          # Example usage
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Dependencies

- numpy >= 1.21.0
- scipy >= 1.7.0
- matplotlib >= 3.4.0
- pandas >= 1.3.0
- jupyter >= 1.0.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 