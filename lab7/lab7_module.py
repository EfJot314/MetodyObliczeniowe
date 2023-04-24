import scipy.special as scis
import scipy.integrate as scint

#funkcje do calkowania
def rectIntegrate(f, a, b):
    if f((a+b)/2) != None:
        return (b-a)*f((a+b)/2)
    return 0

def trapzIntegrate(f, a, b):
    if f(a) != None and f(b) != None:
        return (b-a)/2 * (f(a) + f(b))
    return 0

def simpsonIntegrate(f, a, b):
    if f(a) != None and f(b) != None and f((a+b)/2) != None:
        return (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))
    return 0


#kwadratura Gaussa-Legendre'a dla przedzialu [a, b]
def gaussLegendreQuadrature(f, a, b, n):
    roots, weights = scis.roots_legendre(n)

    #obliczanie wartosci calki
    result = 0
    for i in range(len(roots)):
        x = ((b-a) * roots[i] + a + b) / 2
        w = (b-a) * weights[i] / 2
        if f(x) != None:
            result += w * f(x)
    
    #return wyniku
    return result


def trapzAdaptive(f, a, b, eps):
    result = scint.quad_vec(f, a, b, epsrel=eps, quadrature='trapezoid', full_output=True)
    toReturn = (result[0], result[2].neval)
    return toReturn

def gaussKronrodAdaptive(f, a, b, eps):
    result = scint.quad_vec(f, a, b, epsrel=eps, quadrature='gk21', full_output=True)
    toReturn = (result[0], result[2].neval)
    return toReturn








