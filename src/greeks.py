import numpy as np
from scipy.stats import norm
from .black_scholes import d1, d2

def delta_call(S, K, T, r, sigma):
    """
    Calculate call option delta.
    
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
        Call option delta
    """
    return norm.cdf(d1(S, K, T, r, sigma))

def delta_put(S, K, T, r, sigma):
    """
    Calculate put option delta.
    
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
        Put option delta
    """
    return norm.cdf(d1(S, K, T, r, sigma)) - 1

def gamma(S, K, T, r, sigma):
    """
    Calculate option gamma (same for calls and puts).
    
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
        Option gamma
    """
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * np.sqrt(T))

def theta_call(S, K, T, r, sigma):
    """
    Calculate call option theta.
    
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
        Call option theta
    """
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    term1 = -S * norm.pdf(d1_val) * sigma / (2 * np.sqrt(T))
    term2 = -r * K * np.exp(-r * T) * norm.cdf(d2_val)
    return term1 + term2

def theta_put(S, K, T, r, sigma):
    """
    Calculate put option theta.
    
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
        Put option theta
    """
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    term1 = -S * norm.pdf(d1_val) * sigma / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T) * norm.cdf(-d2_val)
    return term1 + term2

def vega(S, K, T, r, sigma):
    """
    Calculate option vega (same for calls and puts).
    
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
        Option vega
    """
    return S * np.sqrt(T) * norm.pdf(d1(S, K, T, r, sigma))

def rho_call(S, K, T, r, sigma):
    """
    Calculate call option rho.
    
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
        Call option rho
    """
    return K * T * np.exp(-r * T) * norm.cdf(d2(S, K, T, r, sigma))

def rho_put(S, K, T, r, sigma):
    """
    Calculate put option rho.
    
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
        Put option rho
    """
    return -K * T * np.exp(-r * T) * norm.cdf(-d2(S, K, T, r, sigma)) 