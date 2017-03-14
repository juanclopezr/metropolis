import numpy as np
import matplotlib.pyplot as plt

x = np.array([3.0,5.0,12.0])
a = 1.0
b = 20.0

xp = np.linspace(1.0,20.0,1000)

def prob(x,lam):
	z = -lam*(np.exp(-b/lam)-np.exp(-a/lam))
	return np.exp(-x/lam)/z
	
def nasty_function(x,lam):
	return np.exp(-0.5*np.sum((prob(x,lam)-1./3.)**2))

lam_walk = np.empty((0)) #this is an empty list to keep all the steps
lam_0 = 8.0*((np.random.random())-0.5) #this is the initialization
lam_walk = np.append(lam_walk,lam_0)

n_iterations = 200000 #this is the number of iterations I want to make
for i in range(n_iterations):
    lam_prime = np.random.normal(lam_walk[i], 0.1) #0.1 is the sigma (std. dev) in the normal distribution
    alpha = nasty_function(x,lam_prime)/nasty_function(x,lam_walk[i])
    if(alpha>=1.0):
        lam_walk  = np.append(lam_walk,lam_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            lam_walk = np.append(lam_walk,lam_prime)
        else:
            lam_walk = np.append(lam_walk,lam_walk[i])
            
f = nasty_function(xp,lam_walk[-1])
norm = sum(f*(x[1]-x[0]))
plot(x,f/norm, linewidth=1, color='r')
count, bins, ignored = plt.hist(x_walk, 1000, normed=True)

#fig = figure(1, figsize=(9.5,6.5))
plt.xlabel('x')
plt.ylabel('p(x)')
ax = axes()
ax.set_xlim([-4.0,4.0])
ax.set_ylim([0.0,2.0])
