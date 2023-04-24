import scipy.special as scis
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#funkcja dana w zadaniu
f = lambda x: 4/ (1 + x*x)


#zamiast skalowac licze dwa razy calke dla [-1, 1] z 2*n wezlami, a nastepnie wszystko dziele przez 2, poniewaz f(x) jest parzysta
errors = []
ns = []
for n in range(1, 40):
    #wyznaczam wezly i wagi dla N = 2*n
    roots, weights = scis.roots_legendre(2*n)

    #obliczanie wartosci calki
    result = 0
    for i in range(len(roots)):
        result += weights[i] * f(roots[i])
    
    #dziele na 2, bo liczylem na dwa razy wiekszym przedziale
    result /= 2

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

