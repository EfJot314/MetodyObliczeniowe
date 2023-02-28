#importy
import math
import numpy as np
import matplotlib.pyplot as plt


#funkcje pomocnicze
def trueDerivative(x):
    return 1+(math.tan(x))**2


def derivative1(f, h, x):
    return (f(x+h)-f(x))/h

def derivative2(f, h, x):
    return (f(x+h)-f(x-h))/(2*h)


def f(x):
    return math.tan(x)


#generowanie danych
x = 1
xData = []
yData1 = []
yData2 = []

true_value = trueDerivative(x)

for k in range(17):
    h = 10**(-k)
    d1 = derivative1(f, h, x)
    d2 = derivative2(f, h, x)

    delta1 = abs(d1 - true_value)/true_value
    delta2 = abs(d2 - true_value)/true_value

    yData1.append(delta1)
    yData2.append(delta2)
    xData.append(h)

#zmiana typu danych
xData = np.array(xData)
yData1 = np.array(yData1)
yData2 = np.array(yData2)

#rysowanie wykresow
#wykres1
plt.subplot(1,2,1)
plt.title(r"$f'(x) = \frac{f(x+h)-f(x)}{h}$")
plt.yscale("log")
plt.xscale("log")
plt.plot(xData, yData1)
#wykres2
plt.subplot(1,2,2)
plt.title(r"$f'(x) = \frac{f(x+h)-f(x-h)}{2h}$")
plt.yscale("log")
plt.xscale("log")
plt.plot(xData, yData2)
plt.show()





