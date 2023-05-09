import numpy as np
import matplotlib.pyplot as plt


g = lambda x: (x*x + 1) / (2*x + 1)


n = 10

yTab = [0 for i in range(n)]
for i in range(1, n):
    yTab[i] = g(yTab[i-1])

#wartosci bezwzgledne x
xTab = [np.sqrt(yTab[i]) for i in range(n)]

print("x =",xTab)
print("y =", yTab)

#wyznaczania errorow
y0 = np.sqrt(5)/2 - 0.5
errors = [abs((yTab[i] - y0) / y0) for i in range(n)]


#wykres errorow
plt.title("Wartość bezwzględna błędu względnego rozwiązania metodą Newtona")
plt.xlabel("Liczba iteracji")
plt.ylabel("Błąd względny")
plt.plot(errors)
plt.yscale('log')
plt.show()










