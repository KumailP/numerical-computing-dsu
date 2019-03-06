# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:00:24 2019

@author: Kumail
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)*(3.2*np.sin(x)-0.5*np.cos(x))
    
a = 3
b = 6
i = 0
DOA = 0.001

fa = f(a)
fb = f(b)
DOAfound = False
error = np.inf
prevFc = 0
i = 0

arr = []
iterations = []

accuracy = 0.001

while  np.abs(error) > accuracy:
    if fa*fb < 0:
        c = (a+b)/2
        fc = f(c)
        if fc == 0:
            print("Exact root")
            break
        elif fc * f(b) < 0:
            a = c
        elif f(a) * fc < 0:
            b = c
        if i > 0:
            error = prevFc - fc
        print(f"f(c): {np.round(f(c), 4)} | error: {np.round(np.abs(error),3)}")
        arr.append(np.abs(error))
        iterations.append(i)
        prevFc = fc;
        i = i+1
    else:
        print("Condition not met")
        break

plt.plot(iterations, arr)
plt.ylabel("Error")
plt.xlabel("Iterations")
plt.show()