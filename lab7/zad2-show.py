import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data2.npy"

#odczyt z pliku
with open(path, 'rb') as file:
    M1 = np.load(file)
    rectErrors1 = np.load(file)
    trapzErrors1 = np.load(file)
    simpsonErrors1 = np.load(file)
    glN1 = np.load(file)
    glErrors1 = np.load(file)
    gkN1 = np.load(file)
    gkErrors1 = np.load(file)
    tN1 = np.load(file)
    tErrors1 = np.load(file)
    M2 = np.load(file)
    rectErrors2 = np.load(file)
    trapzErrors2 = np.load(file)
    simpsonErrors2 = np.load(file)
    glN2 = np.load(file)
    glErrors2 = np.load(file)
    gkN2 = np.load(file)
    gkErrors2 = np.load(file)
    tN2 = np.load(file)
    tErrors2 = np.load(file)


#zmiana danych X
for i in range(len(glN1)):
    glN1[i] = np.log2(glN1[i])
for i in range(len(gkN1)):
    gkN1[i] = np.log2(gkN1[i]-1)
for i in range(len(tN1)):
    tN1[i] = np.log2(tN1[i]-1)
for i in range(len(glN2)):
    glN2[i] = np.log2(glN2[i])
for i in range(len(gkN2)):
    gkN2[i] = np.log2(gkN2[i]-1)
for i in range(len(tN2)):
    tN2[i] = np.log2(tN2[i]-1)


#wykresy f1
plt.title("Błędy względne kwadratur funkcji f1(x)")
plt.xlabel("m")
plt.ylabel("błąd względny")
plt.plot(M1, rectErrors1, label="Metoda prostokątów")
plt.plot(M1, trapzErrors1, label="Metoda trapezów")
plt.plot(M1, simpsonErrors1, label="Metoda Simpsona")
plt.plot(glN1, glErrors1, label="Metoda Gaussa-Legendre'a")
plt.plot(gkN1, gkErrors1, label="Metoda Gaussa-Kronroda")
plt.plot(tN1, tErrors1, label="Metoda adaptacyjna trapezów")
plt.yscale("log")
plt.legend()
plt.show()


#wykresy f2
plt.title("Błędy względne kwadratur funkcji f2(x)")
plt.xlabel("m")
plt.ylabel("błąd względny")
plt.plot(M2, rectErrors2, label="Metoda prostokątów")
plt.plot(M2, trapzErrors2, label="Metoda trapezów")
plt.plot(M2, simpsonErrors2, label="Metoda Simpsona")
plt.plot(glN2, glErrors2, label="Metoda Gaussa-Legendre'a")
plt.plot(gkN2, gkErrors2, label="Metoda Gaussa-Kronroda")
plt.plot(tN2, tErrors2, label="Metoda adaptacyjna trapezów")
plt.yscale("log")
plt.legend()
plt.show()