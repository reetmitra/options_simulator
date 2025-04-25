"""
Options Pricing Simulator - Test Suite
This script provides comprehensive testing of the options pricing library.
"""

import numpy as np
from black_scholes import black_scholes_call, black_scholes_put
from greeks import (
    delta_call, delta_put, gamma, theta_call, theta_put,
    vega, rho_call, rho_put
)
from payoff_visualizer import plot_payoff, plot_combined_payoff

def test_basic_pricing():
    """Test basic option pricing with standard market conditions."""
    print("\n=== Basic Option Pricing Tests ===")
    
    test_cases = [
        # (S, K, T, r, sigma) - At the money
        (100, 100, 1.0, 0.05, 0.2),
        # In the money calls, out of money puts
        (120, 100, 1.0, 0.05, 0.2),
        (150, 100, 1.0, 0.05, 0.2),
        # Out of money calls, in the money puts
        (80, 100, 1.0, 0.05, 0.2),
        (50, 100, 1.0, 0.05, 0.2),
    ]
    
    for i, (S, K, T, r, sigma) in enumerate(test_cases, 1):
        call_price = black_scholes_call(S, K, T, r, sigma)
        put_price = black_scholes_put(S, K, T, r, sigma)
        print(f"\nTest Case {i}:")
        print(f"Parameters: S=${S}, K=${K}, T={T}yr, r={r*100}%, σ={sigma*100}%")
        print(f"Call Price: ${call_price:.2f}")
        print(f"Put Price: ${put_price:.2f}")
        # Put-Call Parity Check
        parity_diff = abs((call_price + K * np.exp(-r * T)) - (put_price + S))
        print(f"Put-Call Parity Check (should be close to 0): {parity_diff:.6f}")

def test_time_effects():
    """Test option pricing with different time to expiration."""
    print("\n=== Time Effect Tests ===")
    
    S = 100
    K = 100
    r = 0.05
    sigma = 0.2
    times = [0.1, 0.25, 0.5, 1.0, 2.0]  # Different times to expiration
    
    print("\nTesting time decay effects:")
    for T in times:
        call_price = black_scholes_call(S, K, T, r, sigma)
        put_price = black_scholes_put(S, K, T, r, sigma)
        call_theta = theta_call(S, K, T, r, sigma)
        put_theta = theta_put(S, K, T, r, sigma)
        print(f"\nTime to Expiration: {T} years")
        print(f"Call Price: ${call_price:.2f}, Theta: {call_theta:.4f}")
        print(f"Put Price: ${put_price:.2f}, Theta: {put_theta:.4f}")

def test_volatility_effects():
    """Test option pricing with different volatility levels."""
    print("\n=== Volatility Effect Tests ===")
    
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    volatilities = [0.1, 0.2, 0.3, 0.5, 0.8]  # Different volatility levels
    
    print("\nTesting volatility effects:")
    for sigma in volatilities:
        call_price = black_scholes_call(S, K, T, r, sigma)
        put_price = black_scholes_put(S, K, T, r, sigma)
        option_vega = vega(S, K, T, r, sigma)
        print(f"\nVolatility: {sigma*100}%")
        print(f"Call Price: ${call_price:.2f}")
        print(f"Put Price: ${put_price:.2f}")
        print(f"Vega: {option_vega:.4f}")

def test_interest_rate_effects():
    """Test option pricing with different interest rates."""
    print("\n=== Interest Rate Effect Tests ===")
    
    S = 100
    K = 100
    T = 1.0
    sigma = 0.2
    rates = [0.01, 0.02, 0.05, 0.08, 0.1]  # Different interest rates
    
    print("\nTesting interest rate effects:")
    for r in rates:
        call_price = black_scholes_call(S, K, T, r, sigma)
        put_price = black_scholes_put(S, K, T, r, sigma)
        call_rho = rho_call(S, K, T, r, sigma)
        put_rho = rho_put(S, K, T, r, sigma)
        print(f"\nInterest Rate: {r*100}%")
        print(f"Call Price: ${call_price:.2f}, Rho: {call_rho:.4f}")
        print(f"Put Price: ${put_price:.2f}, Rho: {put_rho:.4f}")

def test_edge_cases():
    """Test option pricing with edge cases."""
    print("\n=== Edge Case Tests ===")
    
    edge_cases = [
        # (S, K, T, r, sigma) - Description
        (100, 100, 0.01, 0.05, 0.2),  # Very short time to expiration
        (100, 100, 10.0, 0.05, 0.2),  # Very long time to expiration
        (100, 100, 1.0, 0.05, 0.01),  # Very low volatility
        (100, 100, 1.0, 0.05, 1.0),   # Very high volatility
        (1, 100, 1.0, 0.05, 0.2),     # Very low stock price
        (1000, 100, 1.0, 0.05, 0.2),  # Very high stock price
    ]
    
    for i, (S, K, T, r, sigma) in enumerate(edge_cases, 1):
        try:
            call_price = black_scholes_call(S, K, T, r, sigma)
            put_price = black_scholes_put(S, K, T, r, sigma)
            print(f"\nEdge Case {i}:")
            print(f"Parameters: S=${S}, K=${K}, T={T}yr, r={r*100}%, σ={sigma*100}%")
            print(f"Call Price: ${call_price:.2f}")
            print(f"Put Price: ${put_price:.2f}")
        except Exception as e:
            print(f"\nEdge Case {i} failed:")
            print(f"Parameters: S=${S}, K=${K}, T={T}yr, r={r*100}%, σ={sigma*100}%")
            print(f"Error: {str(e)}")

def generate_payoff_diagrams():
    """Generate payoff diagrams for different scenarios."""
    print("\n=== Generating Payoff Diagrams ===")
    
    # Standard case
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2
    S_range = np.linspace(50, 150, 100)
    
    scenarios = [
        (100, "ATM"),  # At the money
        (80, "ITM_Call"),  # In the money call
        (120, "OTM_Call"),  # Out of the money call
    ]
    
    for strike, scenario in scenarios:
        call_price = black_scholes_call(S, strike, T, r, sigma)
        put_price = black_scholes_put(S, strike, T, r, sigma)
        
        # Call option payoff
        plt = plot_payoff(S_range, strike, call_price, option_type='call')
        plt.savefig(f'plots/call_payoff_{scenario}.png')
        plt.close()
        
        # Put option payoff
        plt = plot_payoff(S_range, strike, put_price, option_type='put')
        plt.savefig(f'plots/put_payoff_{scenario}.png')
        plt.close()
        
        # Combined payoff
        plt = plot_combined_payoff(S_range, strike, call_price, put_price)
        plt.savefig(f'plots/combined_payoff_{scenario}.png')
        plt.close()
        
        print(f"✓ Payoff diagrams for {scenario} scenario saved to plots/ directory")

def main():
    """Run all tests."""
    print("Starting Options Pricing Tests...")
    
    # Run all test categories
    test_basic_pricing()
    test_time_effects()
    test_volatility_effects()
    test_interest_rate_effects()
    test_edge_cases()
    generate_payoff_diagrams()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    main() 