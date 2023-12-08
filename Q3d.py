residuals = [] # find the residuals
residuals.append(data[p] - np.dot(phis, data[p-1::-1]))
for t in range(p+1, N):
    rel_x = data[t-1:t-p-1:-1]
    residuals.append(data[t] - np.dot(phis, rel_x))

mean_res = sum(residuals)/len(residuals)
squared_error = [(x_i - mean_res)**2 for x_i in residuals]
sample_sd = sqrt(sum(squared_error)/(len(residuals)-1)) # sample standard deviation of residuals

upper_bound = [X[N+l] + 1.96*sample_sd*sqrt(l+1) for l in range(12)]
lower_bound = [X[N+l] - 1.96*sample_sd*sqrt(l+1) for l in range(12)]

plt.plot([i for i in range(80, 133)], y, 'b')
plt.plot([i for i in range(121, 133)], upper_bound, 'r')
plt.plot([i for i in range(121, 133)], lower_bound, 'g')
plt.show()
