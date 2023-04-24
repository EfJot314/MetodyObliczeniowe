import scipy.special as scis
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#funkcja dana w zadaniu
f = lambda x: 4/ (1 + x*x)


#kwadratura Gaussa-Legendre'a dla przedzialu [a, b]
def gaussLegendreQuadrature(f, a, b, n):
    roots, weights = scis.roots_legendre(n)

    #obliczanie wartosci calki
    result = 0
    for i in range(len(roots)):
        x = ((b-a) * roots[i] + a + b) / 2
        w = (b-a) * weights[i] / 2
        result += w * f(x)
    
    #return wyniku
    return result



errors = []
ns = []
for n in range(1, 40):
    #obliczanie wartosci calki
    result = gaussLegendreQuadrature(f, 0, 1, n)

    #dane do wykresu (n i error)
    ns.append(n)
    errors.append(abs((result - np.pi) / np.pi))

#wykres tylko tej metody
plt.title("Bledy wzgledne kwadratury Gaussa-Legendre'a")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("blad wzgledny")
plt.plot(ns, errors)
plt.show()


#zmiana danych X
for i in range(len(ns)):
    ns[i] = np.log2(ns[i]-1)

#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data.npy"

#odczyt z pliku
with open(path, 'rb') as file:
    M = np.load(file)
    rectErrors = np.load(file)
    trapzErrors = np.load(file)
    simpsonErrors = np.load(file)

#wspolny wykres wszytskich metod
plt.title("Bledy wzgledne kwadratur")
plt.xlabel("m")
plt.ylabel("blad wzgledny")
plt.plot(M, rectErrors, label="Metoda prostokatow")
plt.plot(M, trapzErrors, label="Metoda trapezow")
plt.plot(M, simpsonErrors, label="Metoda Simpsona")
plt.plot(ns, errors, label="Metoda Gaussa-Legendre'a")
plt.yscale("log")
plt.legend()
plt.show()

