import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes_call, black_scholes_put

def plot_payoff(S_range, K, premium, option_type='call', show_breakeven=True):
    """
    Plot option payoff diagram.
    
    Parameters:
    -----------
    S_range : numpy.ndarray
        Range of underlying prices to plot
    K : float
        Strike price
    premium : float
        Option premium
    option_type : str
        'call' or 'put'
    show_breakeven : bool
        Whether to show breakeven points
    """
    if option_type.lower() == 'call':
        payoff = np.maximum(S_range - K, 0) - premium
        breakeven = K + premium
    else:
        payoff = np.maximum(K - S_range, 0) - premium
        breakeven = K - premium
    
    plt.figure(figsize=(10, 6))
    plt.plot(S_range, payoff, label=f'{option_type.title()} Payoff')
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=K, color='r', linestyle='--', alpha=0.3, label='Strike Price')
    
    if show_breakeven:
        plt.axvline(x=breakeven, color='g', linestyle='--', alpha=0.3, label='Breakeven')
    
    plt.title(f'{option_type.title()} Option Payoff Diagram')
    plt.xlabel('Underlying Price')
    plt.ylabel('Profit/Loss')
    plt.grid(True)
    plt.legend()
    return plt

def plot_combined_payoff(S_range, K, call_premium, put_premium, show_breakeven=True):
    """
    Plot combined call and put payoff diagram.
    
    Parameters:
    -----------
    S_range : numpy.ndarray
        Range of underlying prices to plot
    K : float
        Strike price
    call_premium : float
        Call option premium
    put_premium : float
        Put option premium
    show_breakeven : bool
        Whether to show breakeven points
    """
    call_payoff = np.maximum(S_range - K, 0) - call_premium
    put_payoff = np.maximum(K - S_range, 0) - put_premium
    combined_payoff = call_payoff + put_payoff
    
    call_breakeven = K + call_premium
    put_breakeven = K - put_premium
    
    plt.figure(figsize=(10, 6))
    plt.plot(S_range, call_payoff, label='Call Payoff', alpha=0.5)
    plt.plot(S_range, put_payoff, label='Put Payoff', alpha=0.5)
    plt.plot(S_range, combined_payoff, label='Combined Payoff', linewidth=2)
    
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=K, color='r', linestyle='--', alpha=0.3, label='Strike Price')
    
    if show_breakeven:
        plt.axvline(x=call_breakeven, color='g', linestyle='--', alpha=0.3, label='Call Breakeven')
        plt.axvline(x=put_breakeven, color='g', linestyle='--', alpha=0.3, label='Put Breakeven')
    
    plt.title('Combined Call and Put Payoff Diagram')
    plt.xlabel('Underlying Price')
    plt.ylabel('Profit/Loss')
    plt.grid(True)
    plt.legend()
    return plt 