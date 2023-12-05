## Q1b

def EXP(y, f):
    return(rect(1, -2*(y)*pi*f))
EXP_2 = np.vectorize(EXP)

def invabs(x):
    return(1/(abs(x))**2)

def S_AR(f,phis,sigma2):
    r = phis.size
    z = np.array([EXP_2(x, f) for x in range(1,r+1)]).T
    result = sigma2 * np.array(list(map(invabs, 1 - z.dot(phis))))
    return(result)

print(S_AR(np.array([-0.3,-0.1,0.2,0.4]),
           np.array([0.4,0.8,0.5,0.9,0.3]),
           1))
