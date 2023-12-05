import numpy as np
from statsmodels.tsa.arima_process import ArmaProcess, arma_generate_sample
from math import cos, pi, sqrt

## parameters 
f_1 = 0.2
f_2 = 0.4
r_1 = 0.90
r_2 = 0.97
sigma_squared = 1
N = 100

## Parameters inside iteration; found using 
phi_1 = 2 * r_1 * cos(2*pi*f_1) + 2 * r_2 * cos(2*pi*f_2)
phi_2 = -(r_1**2 + r_2**2 + 4 * r_1 * r_2 * cos(2*pi*f_1) * cos(2*pi*f_2))
phi_3 = 2 * r_1 * r_2 * (r_1 * cos(2*pi*f_2) + r_2 * cos(2*pi*f_1))
phi_4 = -((r_1*r_2)** 2)

## Implementation
phi = np.array([phi_1, phi_2, phi_3, phi_4])
X_t = np.array([0,0,0,0])
eps_t = np.random.normal(0, sqrt(sigma_squared), size=N+1000)

t = 0
while t < N+1000:
    X_tplus1 = np.dot(X_t[-4:], phi) + eps_t[t]
    X_t = np.concatenate((X_t, np.array([X_tplus1])))
    t = t+1
    
X_t_final = np.delete(X_t, range(1004)) ## Remove X_-3, X_-2, X_-1, X_0 and the first 1000 observations

## Plot
plt.figure(figsize=(10, 5))
plt.plot(X_t_final)
plt.xlabel("t")
plt.ylabel("X_t")
plt.title("AR(4) process with removal of first 1000 samples")
plt.show()
