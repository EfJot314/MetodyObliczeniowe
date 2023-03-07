import pandas as pd
import numpy as np
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












