import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0,10, 100)
y = x

k = 10**3
M = k**2
G = k**3
m = 10**-3
u = m**2
n = m**3

def reactance(f, C):
    Xc = 2 * math.pi * f * C
    return Xc

def reactance_plot(f, C, plotting_func):
    Xc = reactance(f, C)
    plotting_func(f, Xc)

f = np.linspace(0, 10000, )

plt.figure()
plt.subplot(131)
plt.plot(x,y)
plt.subplot(132)
plt.semilogy(x,y)

plt.subplot(133)
x = np.logspace(0,10, 100)
y = x
plt.loglog(x,y)

plt.show()
