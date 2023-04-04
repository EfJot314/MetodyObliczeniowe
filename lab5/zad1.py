import numpy as np
import matplotlib.pyplot as plt



#dane dotyczace populacji
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


true1990Value = 248709873


#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)

#wyznacznie AIC
def getAIC(X, Y, p, m, n):
    k = m+1
    sum = 0
    for i in range(n):
        sum += (Y[i] - p(X[i]))**2

    aic = 2*k - k*np.log(sum/k)

    if n/k < 40:
        aic += 2*k*(k+1) / (n-k-1)
    
    return aic



#dane x dla wykresow
countinousXData = np.array([year for year in range(1900, 2000)])

#tworze wielomiany, ich wykresy, porownuje bledy, wyznaczam AIC
nOfPolynomials = 6
errorsTab = [0 for i in range(nOfPolynomials+1)]
aicTab = [0 for i in range(nOfPolynomials+1)]
for m in range(nOfPolynomials+1):
    #wyznaczam wielomian
    p = np.polynomial.polynomial.Polynomial.fit(xData, yData, m)
    #wyznaczam blad wzgledny
    errorsTab[m] = abs(p(1990)-true1990Value)/true1990Value
    #wyznaczam wartosc AIC
    aicTab[m] = getAIC(xData, yData, p, m, 9)
    #dodaje do wykresu
    l = "polynomial degree: "+str(m)
    plt.plot(countinousXData, p(countinousXData),linewidth=0.9, label=l)

#dane wejsciowe
plt.plot(xData, yData, "ro", label="population data")

#rok 1990
plt.plot(1990, true1990Value, "bo", label="1990 true population")

plt.title("Polynomials of population in USA")
plt.xlabel("year")
plt.ylabel("population")
plt.legend()
plt.show()


#bledy wzgledne dla 1990 i poszukiwania najmniejszego
minDegree = 0
for i in range(nOfPolynomials+1):
    if errorsTab[i] < errorsTab[minDegree]:
        minDegree = i
    print("Degree:", i, "relative error for 1990:", errorsTab[i])

#najmniejszy blad
print()
print("The lowest relative error for 1990:", errorsTab[minDegree], "degree:", minDegree)
print()


#AIC
minAICDegree = 0
for i in range(nOfPolynomials+1):
    if aicTab[i] < aicTab[minAICDegree]:
        minAICDegree = i
    print("AIC for polynomial degree", i, ":", aicTab[i])


#najmniejsza wartosc AIC
print()
print("The lowest AIC value:", aicTab[minAICDegree], "degree:", minAICDegree)
print()







