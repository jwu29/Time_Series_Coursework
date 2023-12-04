estimate = {"p":[], "d_1":[], "d_2":[], "d_3":[], "d_4":[]}

for i in range(5000): # slow :<
    realisation = simulate_1a(6/64, 26/64, 0.8, 0.8, 64, 1)
    perio = periodogram(realisation)
    d_1 = direct(realisation, 0.05)
    d_2 = direct(realisation, 0.1)
    d_3 = direct(realisation, 0.25)
    d_4 = direct(realisation, 0.5)
    
    #store only values at given frequencies
    estimate["p"] += [perio[38], perio[40], perio[48], perio[58]] 
    estimate["d_1"] += [d_1[38], d_1[40], d_1[48], d_1[58]]
    estimate["d_2"] += [d_2[38], d_2[40], d_2[48], d_2[58]]
    estimate["d_3"] += [d_3[38], d_3[40], d_3[48], d_3[58]]
    estimate["d_4"] += [d_4[38], d_4[40], d_4[48], d_4[58]]
  # find phi's
r_1 = 0.8
r_2 = 0.8
f_1 = 6/64
f_2 = 26/64

phi_1 = 2 * r_1 * math.cos(2*np.pi*f_1) + 2 * r_2 * math.cos(2*np.pi*f_2)
phi_2 = -(r_1 + r_2 + 4 * r_1 * r_2 * math.cos(2*np.pi*f_1) * math.cos(2*np.pi*f_2))
phi_3 = 2 * r_1 * r_2 * (r_1 * math.cos(2*np.pi*f_2) + r_2 * math.cos(2*np.pi*f_1))
phi_4 = -((r_1*r_2)** 2)

# true values at given frequencies
true = S_AR([6/64, 8/64, 16/64, 26/64], [phi_1, phi_2, phi_3, phi_4], 1)
print(true)

# sample mean of estimators at given frequencies
s_percentage_bias = {"p":[], "d_1":[], "d_2":[], "d_3":[], "d_4":[]}

for estimator in s_percentage_bias:
    s_percentage_bias[estimator].append(100 * abs(1/5000 * sum(estimate[estimator][0::4])-true[0])/true[0])
    s_percentage_bias[estimator].append(100 * abs(1/5000 * sum(estimate[estimator][1::4])-true[1])/true[1])
    s_percentage_bias[estimator].append(100 * abs(1/5000 * sum(estimate[estimator][2::4])-true[2])/true[2])
    s_percentage_bias[estimator].append(100 * abs(1/5000 * sum(estimate[estimator][3::4])-true[3])/true[3])

print(s_percentage_bias)
