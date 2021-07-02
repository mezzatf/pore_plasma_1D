import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


a = 100.0 * 1e-6
b = 600.0 * 1e-6

x = np.linspace(-1*b, 1*b, 1000)

y = np.linspace(-1*b, 1*b, 1000)

X,Y    = np.meshgrid(x,y)
sigmaR = a**2/(b**2 - a**2) *(1.0 + (b**2/(X**2 + Y**2)))

# plt.imshow(sigmaR, interpolation='gaussian' )
plt.contourf(X*1e6, Y*1e6, sigmaR, cmap='hsv')
plt.colorbar();
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()
