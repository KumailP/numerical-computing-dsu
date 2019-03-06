'''
    f(x) = 7(e)^0.5x at x=2
'''

import numpy as np
import matplotlib.pyplot as plt

# x from - 10 to 100 with 10 difference
x = -10

def f(x):
    return 7*np.exp(0.5*x)

X = []
Y = []

while x <= 10:
    y = f(x)
    print(f'x: {x}, y: {y}')
    
    Y.append(y)
    X.append(x)
    
    x = x+1
     
    
plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.show()
