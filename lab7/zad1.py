import lab7_module as module
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


#funkcja z zadania
f = lambda x: 4 / (1 + x*x)

#liczenie calek
gkN = []
gkErrors = []
tN = []
tErrors = []
for m in range(15):
    #wyznaczanie wartosci calek
    result1, n1 = module.gaussKronrodAdaptive(f, 0, 1, 10**(-m))
    result2, n2 = module.trapzAdaptive(f, 0, 1, 10**(-m))

    #dane do wykresow
    gkN.append(n1)
    gkErrors.append(abs((result1 - np.pi) / np.pi))

    tN.append(n2)
    tErrors.append(abs((result2 - np.pi) / np.pi))

#Gauss-Legendre
glErrors = []
glN = []
for n in range(1, 500):
    #obliczanie wartosci calki
    result = module.gaussLegendreQuadrature(f, 0, 1, n)

    #dane do wykresu (n i error)
    glN.append(n)
    glErrors.append(abs((result - np.pi) / np.pi))



#zaladowanie danych z poprzedniego zadania
#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data1.npy"
#odczyt z pliku
with open(path, 'rb') as file:
    M = np.load(file)
    rectErrors = np.load(file)
    trapzErrors = np.load(file)
    simpsonErrors = np.load(file)


#zmiana danych X
for i in range(len(glN)):
    glN[i] = np.log2(glN[i]-1)
for i in range(len(gkN)):
    gkN[i] = np.log2(gkN[i]-1)
for i in range(len(tN)):
    tN[i] = np.log2(tN[i]-1)


print("bledy GK:", gkErrors)
print("liczba ewaluacji GK:", gkN)


#wykresy
plt.title("Błędy względne kwadratur")
plt.xlabel("m")
plt.ylabel("błąd względny")
plt.plot(M, rectErrors, label="Metoda prostokątów")
plt.plot(M, trapzErrors, label="Metoda trapezów")
plt.plot(M, simpsonErrors, label="Metoda Simpsona")
plt.plot(glN, glErrors, label="Metoda Gaussa-Legendre'a")
plt.plot(gkN, gkErrors, label="Metoda Gaussa-Kronroda")
plt.plot(tN, tErrors, label="Metoda adaptacyjna trapezów")
plt.yscale("log")
plt.legend()
plt.show()

