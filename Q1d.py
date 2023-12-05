# A
estimate = {6/64:[], 8/64:[], 16/64:[], 26/64:[]}

for i in range(5000): # slow :<
    realisation = simulate_1a(6/64, 26/64, 0.8, 0.8, 64, 1)
    perio = periodogram(realisation)
    d_1 = direct(realisation, 0.05)
    d_2 = direct(realisation, 0.1)
    d_3 = direct(realisation, 0.25)
    d_4 = direct(realisation, 0.5)
    
    #store only values at given frequencies
    estimate[6/64] += [perio[38], d_1[38], d_2[38], d_3[38], d_4[38]] 
    estimate[8/64] += [perio[40], d_1[40], d_2[40], d_3[40], d_4[40]] 
    estimate[16/64] += [perio[48], d_1[48], d_2[48], d_3[48], d_4[48]] 
    estimate[26/64] += [perio[58], d_1[58], d_2[58], d_3[58], d_4[58]] 

# each key in estimate now contains 5000*5 elements from 5000 realisations using each method

# B
# find phi's
def percentage_bias(r):
    r_1 = r
    r_2 = r
    f_1 = 6/64
    f_2 = 26/64
    phi_1 = 2 * r_1 * math.cos(2*np.pi*f_1) + 2 * r_2 * math.cos(2*np.pi*f_2)
    phi_2 = -(r_1**2 + r_2**2 + 2*r_1*r_2*(math.cos(2*np.pi*(f_1+f_2)) + math.cos(2*np.pi*(f_1-f_2))))
    phi_3 = 2 * r_1 * r_2 * (r_1 * math.cos(2*np.pi*f_2) + r_2 * math.cos(2*np.pi*f_1))
    phi_4 = -((r_1*r_2)** 2)

    # true values at given frequencies
    true = S_AR([6/64, 8/64, 16/64, 26/64], [phi_1, phi_2, phi_3, phi_4], 1)
    frequencies = [6/64, 8/64, 16/64, 26/64]

    # sample mean of estimators at given frequencies
    s_percentage_bias = {6/64:[], 8/64:[], 16/64:[], 26/64:[]}

    for i in range(len(true)):
        s_percentage_bias[frequencies[i]].append(100 * abs(1/5000 * sum(estimate[frequencies[i]][0::5])-true[i])/true[i])
        s_percentage_bias[frequencies[i]].append(100 * abs(1/5000 * sum(estimate[frequencies[i]][1::5])-true[i])/true[i])
        s_percentage_bias[frequencies[i]].append(100 * abs(1/5000 * sum(estimate[frequencies[i]][2::5])-true[i])/true[i])
        s_percentage_bias[frequencies[i]].append(100 * abs(1/5000 * sum(estimate[frequencies[i]][3::5])-true[i])/true[i])
        s_percentage_bias[frequencies[i]].append(100 * abs(1/5000 * sum(estimate[frequencies[i]][4::5])-true[i])/true[i])
        
    return s_percentage_bias

percentage_bias(0.8)

# C
pb_f1 = []
pb_f2 = []
pb_f3 = []
pb_f4 = []
for r in np.arange(0.81, 1, 0.01):
    pb_f1 += percentage_bias(r)[6/64]
    pb_f2 += percentage_bias(r)[8/64]
    pb_f3 += percentage_bias(r)[16/64]
    pb_f4 += percentage_bias(r)[26/64]
