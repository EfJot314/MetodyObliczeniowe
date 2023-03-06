import math
import numpy as np
import matplotlib.pyplot as plt


def true_function(n):
    return (4**(1-n))/3

# a_n+1 = 2.25*a_n - 0.5*a_n-1 => a_n = 2.25*a_n-1 - 0.5*a_n-2

#tworzenie ciagu
n = 225
xData = [1,2]
anData = [1/3, 1/12]
errorData = [0, 0]
for i in range(2, n):
    xData.append(i+1)
    anData.append(2.25*anData[i-1]-0.5*anData[i-2])
    true_value = true_function(i+1)
    errorData.append((abs(anData[i]-true_value))/true_value)

#zmiana typu danych
xData = np.array(xData)
anData = np.array(anData)
errorData = np.array(errorData)

#wyswietlanie n dla ktorego wykres zaczyna rosnac
print("n =", xData[np.argmin(anData)])

#rysowanie wykresu
#wykres a_n
plt.subplot(1,2,1)
plt.title(r"$a_n = 2.25 \cdot a_{n-1} - 0.5 \cdot a_{n-2}$")
plt.xlabel(r"$n$")
plt.ylabel(r"$a_n$")
plt.yscale("log")
plt.plot(xData, anData)
#wykres bledu
plt.subplot(1,2,2)
plt.title(r"$error = \frac{a_n-true_a}{true_a}$")
plt.xlabel(r"$n$")
plt.ylabel(r"$error$")
plt.yscale("log")
plt.plot(xData, errorData)
plt.show()



