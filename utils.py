import numpy as np
from scipy.integrate import quad
import math

# Función distribución Erlang
def erlang_pdf(x, lambda_, k):
    return np.where(x < 0, 0, (lambda_**k * x**(k-1) * np.exp(-lambda_*x)) / math.factorial(k-1))
