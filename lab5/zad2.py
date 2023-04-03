#importy
import numpy as np
import matplotlib.pyplot as plt

#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)

#przesuwanie o wektor [dx, dy]
def moveLambda(f, dx, dy):
    return lambda x: f(x-dx)+dy

#calka metoda prostokatow funkcji f na [xmin, xmax] z n przedzialami
def integralValue(f, xmin, xmax, n):
    sum = 0
    h = (xmax - xmin) / n
    for i in range(1,n):
        y1 = f(xmin+(i-1)*h)
        y2 = f(xmin+i*h)
        sum += 0.5*(y1+y2)*h
    return sum


#funkcje Czebyszewa
T0 = lambda x: 1
T1 = lambda x: x
T2 = lambda x: 2 * x**2 - 1
czebTab = [T0, T1, T2]

#funkcja wag Czebyszewa (2 wersja)
w = lambda x: (1-x**2)**(0.5)

#badana funkcja na przedziale [0,2]
f = lambda x: x**0.5

#przesuwam te funkcje na przedzial [-1,1]
f = moveLambda(f, -1, 0)

#wyznaczam wielomian
p = lambda x: 0
for i in range(3):
    #funkcje do calek
    currF1 = w
    currF1 = multiplyLambda(currF1, f)
    currF1 = multiplyLambda(currF1, czebTab[i])
    currF2 = w
    currF2 = multiplyLambda(currF2, czebTab[i])
    currF2 = multiplyLambda(currF2, czebTab[i])
    #wspolczynnik
    c = integralValue(currF1, -1, 1, 1000) / integralValue(currF2, -1, 1, 1000)
    deltaP = multiplyLambda(lambda x, wsp=c: wsp, czebTab[i])
    p = addLambda(p, deltaP)


#przesuwam p i f z przedzialu [-1,1] na [0,2]
p = moveLambda(p, 1, 0)
f = moveLambda(f, 1, 0)

#wykresy
xData = np.linspace(0, 2, 1000)
yData1 = p(xData)
yData2 = f(xData)
plt.plot(xData, yData1, label="calculated function")
plt.plot(xData, yData2, label="f(x) = sqrt(x)")
plt.legend()
plt.show()

