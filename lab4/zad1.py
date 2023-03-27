#importy
import random as rnd
import numpy as np 
import scipy as scp
import matplotlib.pyplot as plt


#funkcja random
def getRandom(a, b):
    w = b-a
    return a+w*rnd.random()

#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)

#funkcja do Lagrange'a
def lagrange(X, Y, n):
    lagrange = lambda x: 0
    for i in range(n+1):
        deltaW = lambda x: 1
        for j in range(n+1):
            if(j != i):
                deltaW = multiplyLambda(deltaW, lambda x, xi=X[i], xj=X[j]: (x-xj)/(xi-xj))
        deltaW = multiplyLambda(deltaW, lambda x, yi=Y[i]: yi)
        lagrange = addLambda(lagrange, deltaW)
    return lagrange




#definiuje f1 i f2
f1 = lambda x: 1/(1+25*x*x)
f2 = lambda x: np.exp(np.cos(x))



#a)

#liczba wezlow
N = 12

#zbiory x
h = 2/N
xData = np.array([-1+j*h for j in range(N+1)])
czebXData = np.array([np.cos((2*j+1)*np.pi/(2*(N+1))) for j in range(N+1)])

#zbiory Y
yData = f1(xData)
czebYData = f1(czebXData)

#wyznaczanie funkcji interpolacyjnych
fL = lagrange(xData, yData, N)
fSpline = scp.interpolate.CubicSpline(xData, yData)
fCzebL = lagrange(czebXData, czebYData, N)

#dane do wykresow
n = (N-1)*10
h = 2/n
plotX = np.array([-1+h*j for j in range(n+1)])
dTheta = np.pi/n
czebPlotX = np.array([np.cos(dTheta*j) for j in range(n)])

#wykresy
plt.plot(xData, yData, "ro", label="równoodległe węzły")
plt.plot(czebXData, czebYData, "go", label="węzły Czebyszewa")
plt.plot(plotX, fL(plotX), label="wielomian Lagrange'a dla równoodległych węzłów")
plt.plot(plotX, fSpline(plotX), label="kubiczne funkcje sklejane")
plt.plot(czebPlotX, fCzebL(czebPlotX), label="wielomian Lagrange'a dla węzłów Czebyszewa")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()




#b)

#miesce na dane
lagrangeErrors1 = []
splineErrors1 = []
czebErrors1 = []

lagrangeErrors2 = []
splineErrors2 = []
czebErrors2 = []

nData = np.array([j for j in range(4,51)])


testXData1 = np.array([getRandom(-1, 1) for j in range(500)])
testXData2 = np.array([getRandom(0, 2*np.pi) for j in range(500)])

#petla tworzaca dane
for n in nData:
    #f1

    #zbiory x
    h = 2/n
    xData = np.array([-1+j*h for j in range(n+1)])
    czebXData = np.array([np.cos((2*j+1)*np.pi/(2*(n+1))) for j in range(n+1)])

    #zbiory Y
    yData = f1(xData)
    czebYData = f1(czebXData)

    #wyznaczanie funkcji interpolacyjnych
    fL = lagrange(xData, yData, n)
    fSpline = scp.interpolate.CubicSpline(xData, yData)
    fCzebL = lagrange(czebXData, czebYData, n)

    #wyznaczanie wektorow bledow
    errorL = f1(testXData1)-fL(testXData1)
    errorS = f1(testXData1)-fSpline(testXData1)
    errorC = f1(testXData1)-fCzebL(testXData1)

    #przechowywanie danych do wykresow
    lagrangeErrors1.append(np.linalg.norm(errorL))
    splineErrors1.append(np.linalg.norm(errorS))
    czebErrors1.append(np.linalg.norm(errorC))



    #f2

    #zbiory x
    h = 2*np.pi/n
    xData = np.array([-1+j*h for j in range(n+1)])
    czebXData = np.array([ 2*np.pi*(np.cos((2*j+1)*np.pi/(2*(n+1)))+1)/2 for j in range(n+1)])

    #zbiory Y
    yData = f1(xData)
    czebYData = f1(czebXData)

    #wyznaczanie funkcji interpolacyjnych
    fL = lagrange(xData, yData, n)
    fSpline = scp.interpolate.CubicSpline(xData, yData)
    fCzebL = lagrange(czebXData, czebYData, n)

    #wyznaczanie wektorow bledow
    errorL = f2(testXData2)-fL(testXData2)
    errorS = f2(testXData2)-fSpline(testXData2)
    errorC = f2(testXData2)-fCzebL(testXData2)

    #przechowywanie danych do wykresow
    lagrangeErrors2.append(np.linalg.norm(errorL))
    splineErrors2.append(np.linalg.norm(errorS))
    czebErrors2.append(np.linalg.norm(errorC))


#wykresy
plt.title("f1(x)")
plt.plot(nData, lagrangeErrors1, label = "Lagrange dla równoodległych węzłów")
plt.plot(nData, splineErrors1, label = "kubiczne funkcje sklejane")
plt.plot(nData, czebErrors1, label = "Lagrange dla węzłów Czebyszewa")
plt.xlabel("N")
plt.ylabel("norma wektora błędu")
plt.legend()
plt.show()

plt.title("f2(x)")
plt.plot(nData, lagrangeErrors1, label = "Lagrange dla równoodległych węzłów")
plt.plot(nData, splineErrors1, label = "kubiczne funkcje sklejane")
plt.plot(nData, czebErrors1, label = "Lagrange dla węzłów Czebyszewa")
plt.xlabel("N")
plt.ylabel("norma wektora błędu")
plt.legend()
plt.show()






