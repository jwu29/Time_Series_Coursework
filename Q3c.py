## Q3c
def SubsetData(DF, n):
    return DF.head(n)

def FutureForecast(DF, p, forecast_size):
    Forecast_X_t = []
    X_t = np.array(DF[1][:])
    t = DF.shape[0]
    
    phi_p = MLEFullForecast_FindPhi(DF, p)[0]
    sigma_squared = MLEFullForecast_FindPhi(DF, p)[1]
    while t < DF.shape[0] + forecast_size:
        
        X_t_series = X_t[-p:]
        eps_t = np.random.normal(0, sqrt(sigma_squared))
        
        X_t_plus_1 = dot(X_t_series, phi_p) + eps_t
        
        X_t = np.concatenate((X_t, np.array([X_t_plus_1])))
        Forecast_X_t.append(X_t_plus_1)
        
        t = t+1
    return(np.array(Forecast_X_t))

FutureForecast(df_centered, 10, 12)

## Plot

xx_actual = np.array([x for x in range(80,121)])
xx_forecast = np.array([x for x in range(120,133)])
yy_actual = np.array(df_centered[1][79:])
yy_forecast = np.concatenate((np.array([yy_actual[-1]]),FutureForecast(df_centered, 10, 12)))
plt.figure(figsize=(10, 9))
plt.plot(xx_actual,yy_actual,label="Actual Data")
plt.plot(xx_forecast,yy_forecast, label="Forecast via AR(10) and MLE")
plt.xlabel("t")
plt.ylabel("X_t")
plt.title("Forecast of centered sea-level values using AR(10) (Q3c)")
plt.legend(loc="lower left")
plt.show()
