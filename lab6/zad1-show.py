import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data.npy"

#odczyt z pliku
with open(path, 'rb') as file:
    M = np.load(file)
    rectErrors = np.load(file)
    trapzErrors = np.load(file)
    simpsonErrors = np.load(file)

print(M)
print(rectErrors)

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
plt.ylabel("blad wzgledny")
plt.plot(M, rectErrors, label="Metoda prostokatow")
plt.plot(M, trapzErrors, label="Metoda trapezow")
plt.plot(M, simpsonErrors, label="Metoda Simpsona")
plt.yscale("log")
plt.legend()
plt.show()


#rzedy zbieznosci
def orderOfConvergence(i1, i2, errors):
    h1 = 1 / (2 ** i1)
    h2 = 1 / (2 ** i2)
    return np.log( errors[i2]/errors[i1] ) / np.log( h2 / h1)

#print dla czytelnosci
print()
print("Orders of convergence:")

#metoda prostokatow
print("---------------------------")
print("Rect:")
for i in range(1, 20):
    print(orderOfConvergence(i-1, i, rectErrors))

#metoda trapezow
print("---------------------------")
print("Trapz:")
for i in range(1, 21):
    print(orderOfConvergence(i-1, i, trapzErrors))

#metoda Simpsona
print("---------------------------")
print("Simpson:")
for i in range(1, 8):
    print(orderOfConvergence(i-1, i, simpsonErrors))

