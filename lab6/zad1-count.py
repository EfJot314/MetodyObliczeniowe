import numpy as np
from pathlib import Path

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


#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data.npy"

with open(path, 'wb') as file:
    #zapis do pliku
    np.save(file, M)
    np.save(file, rectErrors)
    np.save(file, trapzErrors)
    np.save(file, simpsonErrors)
    print("Zapisano!")
    





