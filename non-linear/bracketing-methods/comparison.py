# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:05:26 2019

@author: Kumail
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use("seaborn")


def f(x):
    return np.exp(-x)*(3.2*np.sin(x)-0.5*np.cos(x))
    
a = 0
b = 4
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


# bisection
while  np.round(np.abs(error),3) > DOA:
    if fa*fb < 0:
        c = (a+b)/2
        fc = f(c)
        if c == 0:
            print("Exact root")
            break
        elif fc * fb < 0:
            a = c
        elif fa * fc < 0:
            b = c
        if i > 0:
            error = prevFc - fc
        print(f"f(c): {np.round(f(c), 4)} | error: {np.round(np.abs(error),3)}")
        arr.append(np.abs(error))
        iterations.append(i)
        prevFc = fc;
        i = i + 1

a = -4
b = 4
i = 0
DOA = 0.001

fa = f(a)
fb = f(b)
DOAfound = False
error = np.inf
prevFc = 0
i = 0
arr2 = []
iterations2 = []

# regula-falsi
while  np.round(np.abs(error),3) > DOA:
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
        arr2.append(np.abs(error))
        iterations2.append(i)
        prevFc = f(c);
        i = i + 1

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title('Bisection vs Regula-Falsi for Non-Linear Eq.', color='r')
ax.plot(iterations, arr, 'go-', label='Bisection')
ax.plot(iterations2, arr2, 'ro-', label='Regula-Falsi')
ax.legend()
plt.ylabel("Error")
plt.xlabel("Iterations")
plt.show()