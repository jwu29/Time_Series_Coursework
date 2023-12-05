import numpy.fft as fft
import math
import numpy as np
import scipy.signal as sn
import matplotlib.pyplot as plt

def periodogram(X):
    N = len(X)
    
    fft_X = fft.fft(X)
    fft_X = fft.fftshift(fft_X) # shift the transform to centre 0 frequency
    
    ret = []
    for i in range(N):
        ret.append((1/N) * (fft_X[i].real**2 + fft_X[i].imag**2)) # find periodogram
    
    return ret
    

def direct(X, p):
    N = len(X)
    pN = math.floor(p * N)
    
    # calculate normalising constant C
    bound1 = [(1 - math.cos(2*np.pi*t/pN+1))**2 for t in range(1, math.ceil(pN/2))]
    sum1 = sum(bound1)
    C = math.sqrt(1/(sum1/2 + N-len(bound1)))
    
    # define h_t & the tapered time series
    Y = []
    for t in range(N):
        if 0 <= t <= pN/2 - 1:
            h = C/2 * (1 - math.cos(2*np.pi*(t+1)/(pN+1)))
        elif pN/2 - 1 < t < N - pN/2:
            h = C
        else:
            h = C/2 * (1 - math.cos(2*np.pi*(N-t)/(pN+1)))
        Y.append(h * X[t])
    
    fft_Y = fft.fft(Y)
    fft_Y = fft.fftshift(fft_Y) # shift the transform to centre 0 frequency

    ret = []
    for i in range(N):
        ret.append(fft_Y[i].real**2 + fft_Y[i].imag**2) # find direct spectral estimate
    
    return ret
    
