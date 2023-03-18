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
minCond = min(cond1, cond2, cond3, cond4)
print("Najmniejszy wspolczynnik uwarunkowania:", minCond)
if(cond1 == minCond):
    M = M1
elif(cond2 == minCond):
    M = M2
elif(cond3 == minCond):
    M = M3
elif(cond4 == minCond):
    M = M4


#wyznaczanie wspolczynnikow
C = np.linalg.solve(M, yData)

print("Otrzymane wspolczynniki:", C)






