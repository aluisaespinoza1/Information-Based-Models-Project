import numpy as np
from scipy.integrate import quad
import math
import matplotlib.pyplot as plt
from scipy.stats import erlang
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


