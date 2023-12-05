#Q1d D

# f = 6/64
plt.plot(np.arange(0.81, 1, 0.01), pb_f1[0::5], 'b', label='periodogram')
plt.plot(np.arange(0.81, 1, 0.01), pb_f1[1::5], 'r', label='tapering p = 0.05')
plt.plot(np.arange(0.81, 1, 0.01), pb_f1[2::5], 'g', label='tapering p = 0.1')
plt.plot(np.arange(0.81, 1, 0.01), pb_f1[3::5], 'y', label='tapering p = 0.25')
plt.plot(np.arange(0.81, 1, 0.01), pb_f1[4::5], 'p', label='tapering p = 0.5')
plt.legend()

# f = 8/64
plt.plot(np.arange(0.81, 1, 0.01), pb_f2[0::5], 'b', label='periodogram')
plt.plot(np.arange(0.81, 1, 0.01), pb_f2[1::5], 'r', label='tapering p = 0.05')
plt.plot(np.arange(0.81, 1, 0.01), pb_f2[2::5], 'g', label='tapering p = 0.1')
plt.plot(np.arange(0.81, 1, 0.01), pb_f2[3::5], 'y', label='tapering p = 0.25')
plt.plot(np.arange(0.81, 1, 0.01), pb_f2[4::5], 'p', label='tapering p = 0.5')
plt.legend()

# f = 16/64
plt.plot(np.arange(0.81, 1, 0.01), pb_f3[0::5], 'b', label='periodogram')
plt.plot(np.arange(0.81, 1, 0.01), pb_f3[1::5], 'r', label='tapering p = 0.05')
plt.plot(np.arange(0.81, 1, 0.01), pb_f3[2::5], 'g', label='tapering p = 0.1')
plt.plot(np.arange(0.81, 1, 0.01), pb_f3[3::5], 'y', label='tapering p = 0.25')
plt.plot(np.arange(0.81, 1, 0.01), pb_f3[4::5], 'p', label='tapering p = 0.5')
plt.legend()

# f = 26/64
plt.plot(np.arange(0.81, 1, 0.01), pb_f4[0::5], 'b', label='periodogram')
plt.plot(np.arange(0.81, 1, 0.01), pb_f4[1::5], 'r', label='tapering p = 0.05')
plt.plot(np.arange(0.81, 1, 0.01), pb_f4[2::5], 'g', label='tapering p = 0.1')
plt.plot(np.arange(0.81, 1, 0.01), pb_f4[3::5], 'y', label='tapering p = 0.25')
plt.plot(np.arange(0.81, 1, 0.01), pb_f4[4::5], 'p', label='tapering p = 0.5')
plt.legend()
