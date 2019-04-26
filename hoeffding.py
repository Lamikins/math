import numpy as np
import sys

#without modifications, np.random.normal is N(0,1)
n = 100 #number of random variables X_i in sample
m = 50 # number of samples of S
x = np.random.normal(size=(n,m))
S = np.sum(x,axis=0)
print(S.shape)

t = float(sys.argv[1])

def get_prob(t):
	prob = np.sum(S >= t) / m
	val = np.exp( (-2 * t ** 2) / (n * (3 + 3) ** 2))
	return prob,val

print(get_prob(t))
