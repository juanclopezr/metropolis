import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data_trend.dat')

N = 10000
deltam = 0.2
deltab = 0.3
m_0 = 1.
b_0 = 1.
m = np.array([m_0])
b = np.array([b_0])

def p(x):
    return np.exp(-x**2/2.)

for i in range(1,N-1):
    Um = np.random.random()*2*deltam-deltam
    m_new = m[-1]+Um
    Ub = np.random.random()*2*deltab-deltab
    b_new = b[-1]+Ub
    yo = data[:,1]-(m[-1]*data[:,0]+b[-1])
    yo = np.dot(yo,yo)
    yn = data[:,1]-(m_new*data[:,0]+b_new)
    yn = np.dot(yn,yn)
    alpha = min(1,p(yn)/p(yo))
    u = np.random.random()
    if(u<=alpha):
        m = np.append(m,[m_new])
        b = np.append(b,[b_new])
    else:
        m = np.append(m,[m[-1]])
        b = np.append(b,[b[-1]])

#plt.scatter(b,m)
plt.scatter(data[:,0],data[:,1])
plt.plot(data[:,0],m[-1]*data[:,0]+b[-1])
plt.show()
