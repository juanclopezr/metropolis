import numpy as np
import matplotlib.pyplot as plt

N = 100000
delta = 0.3
x_0 = 0
x = np.array([x_0])

def p(x):
    return np.exp(-x**2/2.)/np.sqrt(2.*np.pi)

for i in range(1,N-1):
    U = np.random.random()*2*delta -delta
    x_new = x[-1]+U
    alpha = min(1,p(x_new)/p(x[-1]))
    u = np.random.random()
    if(u<=alpha):
        x = np.append(x,[x_new])
    else:
        x = np.append(x,[x[-1]])

plt.hist(x,bins=50)
plt.show()
