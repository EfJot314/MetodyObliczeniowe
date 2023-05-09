import numpy as np
import matplotlib.pyplot as plt


#funkcje dane w zadaniu
f = lambda x: x*x - 3*x + 2

g1 = lambda x: (x*x + 2) / 3
g2 = lambda x: (3*x - 2) ** 0.5
g3 = lambda x: 3 - 2/x if x != 0 else float('inf')
g4 = lambda x: (x*x - 2) / (2*x - 3) if x != 3/2 else float('inf')



gFunctions = [g1, g2, g3, g4]
X = [0 for i in range(4)]

epsData = [[] for i in range(4)]
for i in range(10):
    for j in range(4):
        #wyznaczanie kolejnego x
        X[j] = gFunctions[j](X[j])

        #ustalanie pierwiastka
        x0 = 0
        #dla g1 i g4 pierwiastkiem jest 1
        if j == 0 or j == 3:
            x0 = 1
        #dla g2 i g3 pierwiastkiem jest 2
        else:
            x0 = 2
        
        #obliczanie bledu
        epsData[j].append(abs(X[j] - x0))



#empiryczny rzad zbieznosci
xOrderData = [[] for i in range(4)]
orderData = [[] for i in range(4)]
for j in range(4):
    for i in range(1, 10-1):
        if epsData[j][i-1] == 0 or epsData[j][i] == 0 or epsData[j][i+1] == 0:
            pass
        else:
            xOrderData[j].append(i)
            orderData[j].append(np.log(epsData[j][i] / epsData[j][i+1]) / np.log(epsData[j][i-1] / epsData[j][i]))


#wykresy empirycznych rzedow zbieznosci
plt.title("Empiryczne rzędy zbieżności")
plt.xlabel("Numer iteracji")
plt.ylabel("Wartość rzędu zbieżności")
plt.plot(xOrderData[0], orderData[0], label="g1")
plt.plot(xOrderData[1], orderData[1], label="g2")
plt.plot(xOrderData[2], orderData[2], label="g3")
plt.plot(xOrderData[3], orderData[3], label="g4")
plt.legend()
plt.show()




#zamiana bledow bezwzglednych na wzgledne
for j in range(4):
    x0 = 0
    if j == 0 or j == 3:
        x0 = 1
    else:
        x0 = 2

    for i in range(10):
        epsData[j][i] /= x0


#wykresy bledow
plt.title("Wartości bezwzględne błędów względnych wyznaczenia pierwiastka równania")
plt.xlabel("Numer iteracji")
plt.ylabel("Błąd względny")
plt.plot(epsData[0], label="g1")
plt.plot(epsData[1], label="g2")
plt.plot(epsData[2], label="g3")
plt.plot(epsData[3], label="g4")
plt.yscale('log')
plt.legend()
plt.show()

