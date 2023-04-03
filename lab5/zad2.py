#funkcje pomocnicze do operacji na funkcjach lambda
def addLambda(f1, f2):
    return lambda x: f1(x)+f2(x)

def multiplyLambda(f1, f2):
    return lambda x: f1(x)*f2(x)

def moveLambda(f, dx, dy):
    return lambda x: f(x-dx)+dy

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

#funkcja wag Czebyszewa



#badana funkcja na przedziale [0,2]
f = lambda x: x**0.5

#przesuwam te funkcje na przedzial [-1,1]
f = moveLambda(f, -1, 0)

#wyznaczam wielomian
p = lambda x: 0
for i in range(3):
    currF1 = lambda x: czebTab[i]
    currF1 = multiplyLambda(currF1, f)
    currF2 = multiplyLambda(currF1, )
    c = integralValue()

