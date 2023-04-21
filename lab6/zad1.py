import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt

#funkcja do obliczania calki metoda prostokatow
def rectIntegrate(Y, dx):
    result = 0
    for y in Y:
        result += y*dx
    return result

#funkcja podana w zadaniu
f = lambda x: 4/(1+x*x)

#obliczanie bledow
rectErrors = []
trapzErrors = []
simpsonErrors = []
X = []
for m in range(1,25):
    X.append(m)
    n = 2**m + 1
    dx = 1/(n-1)
    y = [f(i*dx) for i in range(n)]
    rectErrors.append(abs((rectIntegrate(y, dx) - np.pi) / np.pi))
    trapzErrors.append(abs((scint.trapz(y, dx=dx) - np.pi) / np.pi))
    simpsonErrors.append(abs((scint.simps(y, dx=dx) - np.pi) / np.pi))


#wykresy
plt.title("Bledy wzgledne kwadratur")
plt.xlabel("m")
plt.ylabel("relative error")
plt.plot(X, rectErrors, label="Metoda prostokatow")
plt.plot(X, simpsonErrors, label="Metoda trapezow")
plt.plot(X, trapzErrors, label="Metoda Simpsona")
plt.yscale("log")
plt.legend()
plt.show()


