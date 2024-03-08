import math
import numpy as np
import matplotlib.pyplot as plt

def BezierSurfaceChart():
    x = np.asarray([[-0.5, -2, 0], [1., 1, 1], [2, 2, 2]])
    y = np.asarray([[2, 1, 0], [2, 0, -1], [2, 1, 1]])
    z = np.asarray([[1, -1, 2], [0, -0.5, 2], [0.5, 1, 2]])

    uCELLS = 12
    wCELLS = 10

    uPTS = np.size(x, 0)
    wPTS = np.size(x, 1)

    n = uPTS - 1
    m = wPTS - 1

    u = np.linspace(0, 1, uCELLS)
    w = np.linspace(0, 1, wCELLS)

    b = []
    d = []

    xBezier = np.zeros((uCELLS, wCELLS))
    yBezier = np.zeros((uCELLS, wCELLS))
    zBezier = np.zeros((uCELLS, wCELLS))

    for i in range(0, uPTS):

        for j in range(0, wPTS):
            b.append(J(n, i, u))
            d.append(K(m, j, w))

            Jt = J(n, i, u).T

            xBezier = Jt * K(m, j, w) * x[i, j] + xBezier
            yBezier = Jt * K(m, j, w) * y[i, j] + yBezier
            zBezier = Jt * K(m, j, w) * z[i, j] + zBezier

    plt.subplot(121)
    for line in b:
        plt.plot(u, line.T)
    plt.subplot(122)
    for line in d:
        plt.plot(w, line.T)
    plt.show()

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_surface(xBezier, yBezier, zBezier)
    ax.scatter(x,y,z, edgecolors='face')
    plt.show()

def Ni(n,i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def Mj(m,j):
    return math.factorial(m) / (math.factorial(j) * math.factorial(m - j))

def J(n, i ,u):
    return np.matrix(Ni(n, i) * (u**i) * (1-u) ** (n-i))

def K(m, j ,w):
    return np.matrix(Mj(m, j) * (w ** j) * (1 - w) ** (m - j))

BezierSurfaceChart()