import pandas as pd
import numpy as np
from scipy.linalg import lstsq
import matplotlib.pyplot as plt


#pobieranie danych
labelsData = pd.read_csv('/home/filipjedrzejewski/MetodyObliczeniowe/lab2/breast-cancer.labels')
trainData = pd.read_csv('/home/filipjedrzejewski/MetodyObliczeniowe/lab2/breast-cancer-train.dat')
validateData = pd.read_csv('/home/filipjedrzejewski/MetodyObliczeniowe/lab2/breast-cancer-validate.dat')

#wybrane dane do histogramow
#texture
l1 = labelsData.iloc[:,0][2]
df1 = trainData.iloc[:,2]
#smoothness
l2 = labelsData.iloc[:,0][5]
df2 = trainData.iloc[:,5]
#perimeter
l3 = labelsData.iloc[:,0][3]
df3 = trainData.iloc[:,3]
#fractal_dimension
l4 = labelsData.iloc[:,0][10]
df4 = trainData.iloc[:,10]

#liczba cech
m = 10

#liczba danych w train
nt = trainData.shape[0]

#liczba danych w validate
nv = validateData.shape[0]


#inicjowanie macierzy
At = np.zeros((nt,m), dtype=float)
Av = np.zeros((nv,m), dtype=float)


#wypelnianie macierzy
delta = 2
for column in range(m):
    #train
    for row in range(nt):
        At[row,column] = trainData.iat[row,column+delta]
    #validate
    for row in range(nv):
        Av[row,column] = validateData.iat[row,column+delta]


sil = lambda a : (a==2 and 2 or a*sil(a-1))

m = 4
features = [2, 4, 5, 10]
pars  = {"M": 1, "B": -1}
#macierze quad
At_quad = np.zeros((nt,2*m+sil(m-1)), dtype=float)
Av_quad = np.zeros((nv,2*m+sil(m-1)), dtype=float)
#wektory b
bt = np.zeros((nt,1), dtype=float)
bv = np.zeros((nv,1), dtype=float)


for row in range(nt):
    bt[row,0] = pars[trainData.iat[row,1]]
    column = 0
    #bez przeksztalcenia
    for f in features:
        At_quad[row, column] = trainData.iat[row,f]
        column += 1
    #kwadrat
    for f in features:
        value = (trainData.iat[row,f])**2
        At_quad[row, column] = value
        column += 1
    for f1 in range(m):
        for f2 in range(f1+1, m):
            value = trainData.iat[row,features[f1]] * trainData.iat[row,features[f2]]
            At_quad[row, column] = value
            column += 1

for row in range(nv):
    bv[row,0] = pars[validateData.iat[row,1]]
    column = 0
    #bez przeksztalcenia
    for f in features:
        Av_quad[row, column] = validateData.iat[row,f]
        column += 1
    #kwadrat
    for f in features:
        value = (validateData.iat[row,f])**2
        Av_quad[row, column] = value
        column += 1
    for f1 in range(m):
        for f2 in range(f1+1, m):
            value = validateData.iat[row,features[f1]] * validateData.iat[row,features[f2]]
            Av_quad[row, column] = value
            column += 1

    
#wyznaczanie macierzy wag
w, res1, rnk1, s1 = lstsq(At, bt)
w_quad, res2, rnk2, s2 = lstsq(At_quad, bt)


#wyznaczanie wspolczynnikow uwarunkowania
cond = np.linalg.cond(At)
cond_quad = np.linalg.cond(At_quad)

print("Wspolczynniki uwarunkowania lin/quad:")
print(cond, cond_quad)
print()


#przewidywania
p = np.matmul(Av, w)
p_quad = np.matmul(Av_quad, w_quad)

#sprawdzanie jakosci przewidywan
tp, tn, fp, fn = 0, 0, 0, 0     #true-positive, true-negative, false-positive false-negative
tp_quad, tn_quad, fp_quad, fn_quad = 0, 0, 0, 0

for i in range(len(p)):
    expected = (bv[i]>0)
    
    current = (p[i]>0)
    if current and expected:
        tp += 1
    elif current and not expected:
        fp += 1
    elif not current and not expected:
        tn += 1
    elif not current and expected:
        fn += 1
    
    current = (p_quad[i]>0)
    if current and expected:
        tp_quad += 1
    elif current and not expected:
        fp_quad += 1
    elif not current and not expected:
        tn_quad += 1
    elif not current and expected:
        fn_quad += 1

print("WYNIKI")
print("Postac: true-positive, false-positive, true-negative, false-negative")
print("Wyniki dla reprezentacji liniowej")
print(tp, fp, tn, fn)
print("Wyniki dla reprezentacji kwadratowej")
print(tp_quad, fp_quad, tn_quad, fn_quad)



#wykresy histogramow
plt.subplot(2,2,1)
plt.hist(df1)
plt.title(l1)
plt.ylabel("frequency")
plt.xlabel(l1+" value")

plt.subplot(2,2,2)
plt.hist(df2)
plt.title(l2)
plt.ylabel("frequency")
plt.xlabel(l2+" value")

plt.subplot(2,2,3)
plt.hist(df3)
plt.title(l3)
plt.ylabel("frequency")
plt.xlabel(l3+" value")

plt.subplot(2,2,4)
plt.hist(df4)
plt.title(l4)
plt.ylabel("frequency")
plt.xlabel(l4+" value")

plt.show()












