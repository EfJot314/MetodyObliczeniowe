import numpy as np
from pathlib import Path
import lab7_module as module


def integrateFunction(f, tv, file):
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
            rectInt += module.rectIntegrate(f, a, b)
            trapzInt += module.trapzIntegrate(f, a, b)
            simpsonInt += module.simpsonIntegrate(f, a, b)

        #licze bledy
        rectErrors.append(abs((rectInt - tv) / tv))
        trapzErrors.append(abs((trapzInt - tv) / tv))
        simpsonErrors.append(abs((simpsonInt - tv) / tv))

    #Gauss-Legendre
    glErrors = []
    glN = []
    for n in range(1, 40):
        #obliczanie wartosci calki
        result = module.gaussLegendreQuadrature(f, 0, 1, n)

        #dane do wykresu (n i error)
        glN.append(n)
        glErrors.append(abs((result - np.pi) / np.pi))

    
    #metody adaptacyjne
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
        gkErrors.append(abs((result1 - tv) / tv))

        tN.append(n2)
        tErrors.append(abs((result2 - tv) / tv))



    #zapis do pliku
    np.save(file, M)
    np.save(file, rectErrors)
    np.save(file, trapzErrors)
    np.save(file, simpsonErrors)
    np.save(file, glN)
    np.save(file, glErrors)
    np.save(file, gkN)
    np.save(file, gkErrors)
    np.save(file, tN)
    np.save(file, tErrors)
    print("Zapisano!")



#funkcje dane w zadaniu
f1 = lambda x: np.sqrt(x) * np.log(x) if x > 0 else 0
a = 0.001
b = 0.004
f2 = lambda x: 1 / ((x - 0.3)**2 + a) + 1 / ((x - 0.9)**2 + b)

#dokladne wartosci calek
tv1 = -4/9
tv2 = 1 / np.sqrt(a) * (np.arctan((1 - 0.3) / np.sqrt(a)) + np.arctan(0.3 / np.sqrt(a)))
tv2 += 1 / np.sqrt(b) * (np.arctan((1 - 0.9) / np.sqrt(b)) + np.arctan(0.9 / np.sqrt(b)))

#pobieranie i tworzenie sciezki do pliku z danymi
path = str(Path(__file__).parent.absolute())
path += "/data2.npy"

#nadpisuje plik danymi f1
with open(path, 'wb') as file:
    integrateFunction(f1, tv1, file)

#appenduje do pliku danymi f2
with open(path, 'ab') as file:
    integrateFunction(f2, tv2, file)
    





