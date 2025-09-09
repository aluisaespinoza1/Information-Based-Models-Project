import numpy as np
from scipy.integrate import quad
import math
from scipy.optimize import minimize

# Función distribución Erlang
def erlang_pdf(x, lambda_, k):
    return np.where(x < 0, 0, (lambda_**k * x**(k-1) * np.exp(-lambda_*x)) / math.factorial(k-1))

#Liquidity functions buy and sell

#liquidity buy
def p_LB(S):
    return max(0, min(0.5, 0.5 - 0.08 * (S))) #S= (A-S0)

#liquidity sell
def p_LS(S):
    return max(0, min(0.5, 0.5 - 0.08 * (S))) #S= (S0-B)

#Utility function Copeland & Galai

def utility(params, S0, lambda_, k, price_min=10, price_max=33):
   
    B, A = params
    
    # Compute probabilities
    prob_LS_spread = p_LS(S0 - B)
    prob_LB_spread = p_LB(A - S0) 
    prob_LS_bid = p_LS(B)
    prob_LB_ask = p_LB(A)
    
    # Expected gain
    gain = prob_LS_spread * (S0 - B) + prob_LB_spread * (A - S0)
    
    # Expected losses  
    el_sell, _ = quad(lambda P: (B - P) * erlang_pdf(P, lambda_, k), 
                      price_min, B) #integral from 10 to bid price
    el_buy, _ = quad(lambda P: (P - A) * erlang_pdf(P, lambda_, k), 
                     A, price_max) #integral from ask price to 33
    
    loss = prob_LS_bid * el_sell + prob_LB_ask * el_buy
    
    return -(gain - loss) #min(-(gain - loss)) = max(gain - loss)




