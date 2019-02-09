'''
    f(x) = 7(e)^0.5x at x=2
    a) find f(2) using 0.3
    c) find approx. error
'''

import numpy as np
import matplotlib.pyplot as plt

x = 2
h = 0.3
minFactor = 0.00001

def f(x):
    return 7*np.exp(0.5*x)

def df(x):
    return (f(x+h) - f(x))/h

pastApprox = df(x)
h = h - minFactor

leastError = np.inf
leastErrori = 0
i = 1

errors = []
iterations = []

while h>=0:
    presentApprox = df(x)
    error = presentApprox - pastApprox
    print(f'Iteration: {i}, Error: {error}')
    h = h - minFactor
    i = i+1
    errors.append(error)
    iterations.append(i)
    
    if error < leastError:
        leastError = error
        leastErrori = i
    
print(f'Least error is: {leastError}')

plt.plot(iterations, errors)
plt.scatter(leastErrori, leastError, color='red')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()
