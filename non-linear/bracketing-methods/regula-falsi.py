# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:33:43 2019

@author: Kumail
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)*(3.2*np.sin(x)-0.5*np.cos(x))

a = 0

b = 4
i = 0
DOA = 0.0001

fa = f(a)
fb = f(b)
DOAfound = False
error = np.inf
prevFc = 0
i = 0

arr = []
iterations = []

#while  np.round(np.abs(error),3) > DOA:
while i < 10:
    if fa*fb < 0:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if c == 0:
            print("Exact root")
            break
        elif f(c) * f(b) < 0:
            a = c
        elif f(a) * f(c) < 0:
            b = c
        if i > 0:
            error = f(c) - prevFc
        print(f"f(c): {np.round(f(c), 4)} | error: {np.round(np.abs(error),3)}")
        arr.append(np.abs(error))
        iterations.append(i)
        prevFc = f(c);
        i = i + 1
        
plt.plot(iterations, arr)
plt.ylabel("Error")
plt.xlabel("Iterations")
plt.show()
