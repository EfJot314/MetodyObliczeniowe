#importy
import math
import numpy as np 
import scipy as scp
import matplotlib.pyplot as plt



#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)

#definiuje f1 i f2
f1 = lambda x: 1/(1+25*x*x)
f2 = lambda x: math.exp(math.cos(x))



#a)

#liczba wezlow
N = 12

#zbiory x
h = 2/N
xData = np.array([-1+j*h for j in range(N+1)])
czebXData = np.array([math.cos((2*j+1)*math.pi/(2*(N+1))) for j in range(N+1)])

#zbiory Y
yData = f1(xData)
czebYData = f1(czebXData)

print(yData)
print(czebYData)

#funkcja do Lagrange'a
def lagrange(X, Y, n):
    lagrange = lambda x: 0
    for i in range(n):
        deltaW = lambda x: 1
        for j in range(n):
            if(j != i):
                deltaW = multiplyLambda(deltaW, lambda x, xi=X[i], xj=X[j]: (x-xj)/(xi-xj))
        deltaW = multiplyLambda(deltaW, lambda x, yi=Y[i]: yi)
        lagrange = addLambda(lagrange, deltaW)
    return lagrange

fL = lagrange(xData, yData, N+1)
fSpline = scp.interpolate.CubicSpline(xData, yData)
fCzebL = lagrange(czebXData, czebYData, N+1)

#dane do wykresow
n = (N-1)*10
h = 2/n
plotX = np.array([-1+h*j for j in range(n+1)])
dTheta = math.pi/n
czebPlotX = np.array([math.cos(dTheta*j) for j in range(n)])

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




