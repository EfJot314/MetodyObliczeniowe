import numpy as np 
import matplotlib.pyplot as plt



N = 9

xData = np.array([
                1900, 1910, 1920,
                1930, 1940, 1950,
                1960, 1970, 1980
                ])

yData = np.array([
                76212168,
                92228496,
                106021537,
                123202624,
                132164569,
                151325798,
                179323175,
                203302031,
                226542199
                ])


#funcje bazowe
fi1 = lambda t: t
fi2 = lambda t: t - 1900
fi3 = lambda t: t - 1940
fi4 = lambda t: (t - 1940) / 40


#macierze
M1 = np.zeros((N,N))
M2 = np.zeros((N,N))
M3 = np.zeros((N,N))
M4 = np.zeros((N,N))



#uzupelnianie macierzy
for i in range(N):
    for j in range(N):
        M1[i,j] = (fi1(xData[i]))**j
        M2[i,j] = (fi2(xData[i]))**j
        M3[i,j] = (fi3(xData[i]))**j
        M4[i,j] = (fi4(xData[i]))**j


#wspolczynniki uwarunkowania
cond1 = np.linalg.cond(M1)
cond2 = np.linalg.cond(M2)
cond3 = np.linalg.cond(M3)
cond4 = np.linalg.cond(M4)

print("Wspolczynniki uwarunkowania:", cond1, cond2, cond3, cond4)


#wybieranie najlepszego uwarunkowania
M = np.zeros((N,N))
fi = None
minCond = min(cond1, cond2, cond3, cond4)
print("Najmniejszy wspolczynnik uwarunkowania:", minCond)

if(cond1 == minCond):
    print("Wybrano baze 1")
    M = M1
    fi = fi1
elif(cond2 == minCond):
    print("Wybrano baze 2")
    M = M2
    fi = fi2
elif(cond3 == minCond):
    print("Wybrano baze 3")
    M = M3
    fi = fi3
elif(cond4 == minCond):
    print("Wybrano baze 4")
    M = M4
    fi = fi4



#wyznaczanie wspolczynnikow
C = np.linalg.solve(M, yData)
print("Otrzymane wspolczynniki:", C)

#tworzenie wielomianu
f = lambda x: C[0] + C[1]*fi(x) + C[2]*(fi(x))**2 + C[3]*(fi(x))**3 + C[4]*(fi(x))**4 + C[5]*(fi(x))**5 + C[6]*(fi(x))**6 + C[7]*(fi(x))**7 + C[8]*(fi(x))**8

#tworzenie danych do wykresu
years = np.array([year for year in range(1900, 1991)])
population_in_USA = np.array([f(year) for year in years])


#wykres macierz
plt.title("Wielomian wyznaczony z macierzy")
plt.plot(years, population_in_USA)
plt.plot(xData, yData, "ro")
plt.show()

#ekstrapolacja dla roku 1990
exp_USA1990 = f(1990)
real_USA1990 = 248709873
print("Populacja USA w 1990 model / wartosc prawdziwa:", exp_USA1990, real_USA1990)

#blad wzgledny ekstrapolacji
relative_error = abs(exp_USA1990 - real_USA1990) / real_USA1990
print("Blad wzgledny ekstrapolacji:", relative_error, "=", relative_error*100, "%")


#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)


#interpolacja Lagrange'a
lagrange = lambda x: 0
for i in range(9):
    deltaW = lambda x: 1
    for j in range(9):
        if(j != i):
            deltaW = multiplyLambda(deltaW, lambda x, xi=xData[i], xj=xData[j]: (x-xj)/(xi-xj))
    deltaW = multiplyLambda(deltaW, lambda x, yi=yData[i]: yi)
    lagrange = addLambda(lagrange, deltaW)

#wykres Lagrange
population_in_USA = np.array([lagrange(year) for year in years])
plt.title("Wielomian Lagrage'a")
plt.plot(years, population_in_USA)
plt.plot(xData, yData, "ro")
plt.show()



#funkcja obliczajaca ilorazy roznicowe
def diff(tab):
    if(len(tab) == 1):
        return yData[tab[0]]
    return (diff(tab[1:]) - diff(tab[:-1])) / (xData[tab[len(tab)-1]] - xData[tab[0]])


#interpolacja Newtona
newton = lambda x: 0
diffTab = []
for i in range(9):
    diffTab.append(i)
    deltaW = lambda x: 1
    for j in range(i):
        deltaW = multiplyLambda(deltaW, lambda x, xj=xData[j]: (x-xj))
    difVal = diff(diffTab)
    deltaW = multiplyLambda(deltaW, lambda x, f=difVal: f)
    newton = addLambda(newton, deltaW)

#wykres Newton
population_in_USA = np.array([newton(year) for year in years])
plt.title("Wielomian Newtona")
plt.plot(years, population_in_USA)
plt.plot(xData, yData, "ro")
plt.show()


#zaokraglanie danych yData
roundFunction = lambda a: 1000000*round(a/1000000)
rounded_yData = np.array([roundFunction(population) for population in yData])

#wyznaczanie wspolczynnikow dla zaokraglonej macierzy
rounded_C = np.linalg.solve(M, rounded_yData)
print("Otrzymane wspolczynniki po zaokragleniu:", rounded_C)

#tworzenie wielomianu dla nowych wspolczynnikow
rounded_f = lambda x: rounded_C[0] + rounded_C[1]*fi(x) + rounded_C[2]*(fi(x))**2 + rounded_C[3]*(fi(x))**3 + rounded_C[4]*(fi(x))**4 + rounded_C[5]*(fi(x))**5 + rounded_C[6]*(fi(x))**6 + rounded_C[7]*(fi(x))**7 + rounded_C[8]*(fi(x))**8

#wykres macierz zaokraglona
population_in_USA = np.array([rounded_f(year) for year in years])
plt.title("Wielomian wyznaczony z macierzy dla zaokraglenego yData")
plt.plot(years, population_in_USA)
plt.plot(xData, rounded_yData, "ro")
plt.show()

