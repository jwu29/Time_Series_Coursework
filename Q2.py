import pandas as pd
import numpy as np
from math import floor, pi, cos, sqrt
from cmath import rect
import matplotlib.pyplot as plt

## Loading data (remember to uplaod your own data)
df = pd.read_csv(r"C:\Users\Programming\Downloads\0313.csv", header=None)

p = 0.25
N = df.shape[0]
q = floor(p*N) ## equals to |_ pN _|

## Generate tapering sequence h_t
taper1 = lambda t: (1/2) * (1 - cos((2*pi*t)/(q+1)))
taper2 = lambda t: 1
taper3 = lambda t: (1/2) * (1 - cos((2*pi*(N+1-t))/(q+1)))

Taper_1 = np.vectorize(taper1)
Taper_2 = np.vectorize(taper2)
Taper_3 = np.vectorize(taper3)

H_t1 = Taper_1(np.arange(1,(q/2)+1))
H_t2 = Taper_2(np.arange((q/2)+1,N+1-(q/2)))
H_t3 = Taper_3(np.arange(N+1-(q/2),N+1))

H_t = np.concatenate((H_t1,H_t2,H_t3))
mag = H_t.dot(H_t)

C = 1/sqrt(mag)
h_t = C * H_t

## Centering Data
def CenterData(DF):
    X_bar = sum(DF[1])/df.shape[0]
    DF[1] = DF[1].apply(lambda x: x - X_bar)
    return(DF)

## Tapered Estimate of Autocovariance Sequence s_tau

def FindAutoCov(DF, tt):
    tau = abs(tt)
    X_t = np.array(DF[1])
    n = X_t.shape[0]
    r = n - tau
    
    ht = h_t[0:r]
    htplustau = h_t[tau:N]
    Xt = X_t[0:r]
    Xtplustau = X_t[tau:N]
    
    AutoCovVec = ht * htplustau * Xt * Xtplustau
    return(sum(AutoCovVec))

## Compute spectral density using autocovariance sequence

def EXP(y, f):
    return(rect(1, -2*(y)*pi*f))
EXP_2 = np.vectorize(EXP)

def FindSDF(DF, f):
    Z = np.array([EXP_2(tau, f) for tau in range(-N+1,N)])
    W = np.array([FindAutoCov(DF, tau) for tau in range(-N+1,N)])
    return(Z.dot(W).real) ## Imaginary part is very close to zero

## Generate graph for non-centered data

xx = np.linspace(-0.5,0.5,1000)
yy_non_centered = np.array([FindSDF(df, f) for f in xx])

plt.figure(figsize=(10, 5))
plt.plot(xx,yy_non_centered)
plt.xlabel("f")
plt.ylabel("S(f)")
plt.title("SDF with Non-Centered Data")
plt.show()

## Generate graph for centered data

df_copy = df.copy()
df_centered = CenterData(df_copy)
yy_centered = np.array([FindSDF(df_centered, f) for f in xx])

plt.figure(figsize=(10, 5))
plt.plot(xx,yy_centered)
plt.xlabel("f")
plt.ylabel("S(f)")
plt.title("SDF with Centered Data")
plt.show()
