import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt

#funkcja do obliczania calki metoda prostokatow
def rectIntegrate(f, a, b):
    return (b-a)*f((a+b)/2)

def trapzIntegrate(f, a, b):
    return (b-a)/2 * (f(a) + f(b))

def simpsonIntegrate(f, a, b):
    return (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

#funkcja podana w zadaniu
f = lambda x: 4/(1+x*x)

#obliczanie bledow
rectErrors = []
trapzErrors = []
simpsonErrors = []
M = []
for m in range(1,26):
    #zmienne pomocnicze
    M.append(m)
    n = 2**m + 1
    dx = 1/(n-1)

    #obliczam wartosc calek
    rectInt = 0
    trapzInt = 0
    simpsonInt = 0
    for i in range(1, n):
        a = (i-1)*dx
        b = i*dx
        rectInt += rectIntegrate(f, a, b)
        trapzInt += trapzIntegrate(f, a, b)
        simpsonInt += simpsonIntegrate(f, a, b)

    #licze bledy
    rectErrors.append(abs((rectInt - np.pi) / np.pi))
    trapzErrors.append(abs((trapzInt - np.pi) / np.pi))
    simpsonErrors.append(abs((simpsonInt - np.pi) / np.pi))


#licze h_min
rectM = [float('inf'), 0]
trapzM = [float('inf'), 0]
simpsonM = [float('inf'), 0]
for i in range(len(M)):
    if rectErrors[i] < rectM[0]:
        rectM[0] = rectErrors[i]
        rectM[1] = M[i]
    if trapzErrors[i] < trapzM[0]:
        trapzM[0] = trapzErrors[i]
        trapzM[1] = M[i]
    if simpsonErrors[i] < simpsonM[0]:
        simpsonM[0] = simpsonErrors[i]
        simpsonM[1] = M[i]

h_min = 1/(2**rectM[1])
print("h_min_prostokaty (dla m =", rectM[1], "):", h_min)

h_min = 1/(2**trapzM[1])
print("h_min_trapezy (dla m =", trapzM[1], "):", h_min)

h_min = 1/(2**simpsonM[1])
print("h_min_simpson (dla m =", simpsonM[1], "):", h_min)

#wykresy
plt.title("Bledy wzgledne kwadratur")
plt.xlabel("m")
plt.ylabel("relative error")
plt.plot(M, rectErrors, label="Metoda prostokatow")
plt.plot(M, trapzErrors, label="Metoda trapezow")
plt.plot(M, simpsonErrors, label="Metoda Simpsona")
plt.yscale("log")
plt.legend()
plt.show()





