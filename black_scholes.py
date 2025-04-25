import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    """
    Calculate d1 parameter for Black-Scholes formula.
    
    Parameters:
    -----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    
    Returns:
    --------
    float
        d1 parameter
    """
    return (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))

def d2(S, K, T, r, sigma):
    """
    Calculate d2 parameter for Black-Scholes formula.
    
    Parameters:
    -----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    
    Returns:
    --------
    float
        d2 parameter
    """
    return d1(S, K, T, r, sigma) - sigma*np.sqrt(T)

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate Black-Scholes call option price.
    
    Parameters:
    -----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    
    Returns:
    --------
    float
        Call option price
    """
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return S*norm.cdf(d1_val) - K*np.exp(-r*T)*norm.cdf(d2_val)

def black_scholes_put(S, K, T, r, sigma):
    """
    Calculate Black-Scholes put option price.
    
    Parameters:
    -----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    
    Returns:
    --------
    float
        Put option price
    """
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return K*np.exp(-r*T)*norm.cdf(-d2_val) - S*norm.cdf(-d1_val) 