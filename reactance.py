import numpy as np
import matplotlib.pyplot as plt
import math

k = 10**3
M = k**2
G = k**3

m = 10**-3
u = m**2
n = m**3

R = 100
C = 100*u

def reactance(f, C):
    Xc = 1 / (2 * math.pi * f * C)
    return Xc

def low_pass_gain(f, C, R):
    Xc = reactance(f, C)
    A = Xc / np.sqrt(R**2 + Xc**2)
    return A

def low_pass_plot(f, C, R, plotting_func):
    A = []
    for freq in f:
        A.append(low_pass_gain(freq,C,R))
    plotting_func(f,A)

def main():
    plt.figure()
    plt.subplot(131)
    f = np.linspace(1,100*k, 100)
    low_pass_plot(f, C, R, plt.plot)
    plt.subplot(132)
    f = np.logspace(0,5, 100)
    low_pass_plot(f, C, R, plt.semilogx)
    plt.subplot(133)
    f = np.logspace(0,5, 100)
    low_pass_plot(f, C, R, plt.loglog)
    plt.show()

if __name__ == "__main__":
    main()
