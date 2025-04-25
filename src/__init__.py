"""
Options Pricing Simulator

A Python package for options pricing and analysis using the Black-Scholes model.
"""

from .black_scholes import (
    black_scholes_call,
    black_scholes_put,
    d1,
    d2
)

from .greeks import (
    delta_call,
    delta_put,
    gamma,
    theta_call,
    theta_put,
    vega,
    rho_call,
    rho_put
)

from .payoff_visualizer import (
    plot_payoff,
    plot_combined_payoff
)

__version__ = "0.1.0" 