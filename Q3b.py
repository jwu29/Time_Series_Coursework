## Q3b
from cmath import rect

def MLEFullForecast_FindPhi(DF, p):
    n = DF.shape[0]
        
    F_rows_list = [FindFRow(DF, p, i) for i in range(1, n-p+1)]
    F = np.array([np.array(r) for r in F_rows_list])
        
    X = np.array(DF[1][p:])
        
    phi_p = dot(inv(dot(F.T, F)), dot(F.T, X))
    sigma_squared = (dot(X - dot(F,phi_p), X - dot(F,phi_p))) / (n - 2*p)
        
    return(phi_p, sigma_squared)

def invabs(x):
    return(1/(abs(x))**2)

def EXP(y, f):
    return(rect(1, -2*(y)*pi*f))
EXP_2 = np.vectorize(EXP)

def S_AR_v2(DF, f, p):
    phis = MLEFullForecast_FindPhi(DF, p)[0]
    sigma2 = MLEFullForecast_FindPhi(DF, p)[1]
    z = np.array([EXP_2(x, f) for x in range(1,p+1)]).T
    result = sigma2 * np.array(list(map(invabs, 1 - z.dot(phis))))
    return(result) ## Imaginary part is very close to zero

## plot
xx = np.linspace(-0.5,0.5,1000)
df_copy = df.copy()
df_centered = CenterData(df_copy)
yy_centered_v2 = S_AR_v2(df_centered, xx, 10)

plt.figure(figsize=(10, 5))
plt.plot(xx,yy_centered_v2)
plt.xlabel("f")
plt.ylabel("S(f)")
plt.title("SDF with Centered Data (Q3b)")
plt.show()
