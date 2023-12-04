## Q3a
import numpy as np
from numpy import dot
from scipy.linalg import toeplitz, inv
from math import sqrt 

## Embedded Functions
def FindUntaperedAutoCov(DF, tt):
    tau = abs(tt)
    X_t = np.array(DF[1])
    n = X_t.shape[0]
    r = n - tau

    Xt = X_t[0:r]
    Xtplustau = X_t[tau:n]
    
    AutoCovVec = Xt * Xtplustau
    result = (1/n) * sum(AutoCovVec)
    return(result)

def SubsetData(DF, n):
    return DF.head(n)

def FindFRow(DF, p, row): ## row index starts with 1; returns list for smooth implementation
    X_t = np.array(DF[1])
    n = X_t.shape[0]
    
    if row <= N-p:
        F_row_unflip = X_t[row-1:(p-1+row)]
        return(list(np.flip(F_row_unflip)))
    else:
        return("If this message appears the method isn't working.")

## Fitting using Yule-Walker (YW) Method
def YuleWalkerForecast(DF, p):
    t = 60
    Forecast_X_t = []
    while t < 120:
        
        DF_sub = SubsetData(DF, t)
        
        BigGamma_vec = np.array([FindUntaperedAutoCov(DF_sub, tt) for tt in range(0,p)])
        BigGamma = toeplitz(BigGamma_vec)
        SmallGamma = np.array([FindUntaperedAutoCov(DF_sub, tt) for tt in range(1,p+1)])
        phi_p = dot(inv(BigGamma), SmallGamma)
        
        sigma_squared = BigGamma_vec[0] - dot(phi_p, SmallGamma)
        
        X_t_series = np.array(DF_sub[1][-p:])
        eps_t = np.random.normal(0, sqrt(sigma_squared))
        
        X_t_plus_1 = dot(X_t_series, phi_p) + eps_t
        Forecast_X_t.append(X_t_plus_1)
        
        t = t + 1
    return(np.array(Forecast_X_t))

## Fitting using Maximum Likelihood Estimation (MLE)
def MLEForecast(DF, p):
    t = 60
    Forecast_X_t = []
    while t < 120:
        DF_sub = SubsetData(DF, t)
        n = DF_sub.shape[0]
        
        F_rows_list = [FindFRow(DF_sub, p, i) for i in range(1, n-p+1)]
        F = np.array([np.array(r) for r in F_rows_list])
        
        X = np.array(DF_sub[1][p:])
        
        phi_p = dot(inv(dot(F.T, F)), dot(F.T, X))
        sigma_squared = (dot(X - dot(F,phi_p), X - dot(F,phi_p))) / (n - 2*p)
        
        X_t_series = np.array(DF_sub[1][-p:])
        eps_t = np.random.normal(0, sqrt(sigma_squared))
        
        X_t_plus_1 = dot(X_t_series, phi_p) + eps_t
        Forecast_X_t.append(X_t_plus_1)
        
        t = t + 1
    return(np.array(Forecast_X_t))
    pass

## Loading actual data
actual_data = np.array(df_centered[1][60:])

## Computing RMSE for both methods
def RMSE_YW(DF, p):
    error_YW = YuleWalkerForecast(DF,p) - actual_data
    RMSE = sqrt(error_YW.dot(error_YW) / error_YW.shape[0])
    return(RMSE)

def RMSE_MLE(DF, p):
    error_MLE = MLEForecast(DF,p) - actual_data
    RMSE = sqrt(error_MLE.dot(error_MLE) / error_MLE.shape[0])
    return(RMSE)

RMSE_YW_list = [RMSE_YW(df_centered, q) for q in range(1,11)]
RMSE_MLE_list = [RMSE_MLE(df_centered, q) for q in range(1,11)]

## Tabulation of RMSE values
RMSE_dict = {"p in AR(p)":[n for n in range(1,11)], "RMSE from Yule-Walker":RMSE_YW_list, "RMSE from MLE": RMSE_MLE_list}
RMSE_table = pd.DataFrame(data=RMSE_dict).set_index(["p in AR(p)"])

print(RMSE_table)

## Plot of actual data against forecast data
xx_forecast = np.array([x for x in range(61,121)])

plt.figure(figsize=(12, 8))
plt.plot(xx_forecast, actual_data, label="Actual Data")
plt.plot(xx_forecast, MLEForecast(df_centered, 10), label="AR(10) through MLE", linestyle="dotted")
plt.plot(xx_forecast, YuleWalkerForecast(df_centered, 10), label="AR(10) through YW", linestyle="dotted")
plt.xlabel("t")
plt.ylabel("X_t")
plt.title("Forecast of centered sea-level values using AR model")
plt.legend(loc="lower left")
plt.show()

