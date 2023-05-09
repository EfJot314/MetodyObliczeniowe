import numpy as np
import matplotlib.pyplot as plt



#funkcje dane w zadaniu
f1 = lambda x: x**3 - 2*x - 5
f2 = lambda x: np.e ** (-x) - x
f3 = lambda x: x * np.sin(x) - 1


#pochodne tych funkcji
df1 = lambda x: 3 * x**2 - 2
df2 = lambda x: -np.e ** (-x) - 1
df3 = lambda x: np.sin(x) + x * np.cos(x)


#TU SIE ZORIENTOWALEM ZE CHYBA WSM NIE MUSZE NIC PROGRAMOWAC
