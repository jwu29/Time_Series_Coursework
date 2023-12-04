# Sample percentage biases came out suspiciously high for all 5 estimators, so here are the plots 
# to see where/if I went wrong anywhere with the functions

# TEST TO SEE IF FUNCTIONS ARE WRITTEN WRONG
realisation1 = simulate_1a(6/64, 26/64, 0.8, 0.8, 64, 1)
period = periodogram(realisation1)
pd_1 = direct(realisation1, 0.05)
pd_2 = direct(realisation1, 0.1)
pd_3 = direct(realisation1, 0.25)
pd_4 = direct(realisation1, 0.5)
freqs = fft.fftfreq(64)
shifted = fft.fftshift(freqs)

# true values
true = S_AR(shifted, [phi_1, phi_2, phi_3, phi_4], 1)
plt.plot(shifted, true)

# periodogram
plt.plot(shifted, period)

# tapering p=0.05
plt.plot(shifted, pd_1)

# tapering p=0.1
plt.plot(shifted,pd_2)

#tapering p=0.25
plt.plot(shifted, pd_3)

#tapering p=0.5
plt.plot(shifted, pd_4)
