import math
import numpy as np
import matplotlib.pyplot as plt

def BezierCurveChart():
    x = np.random.random_sample((3,))
    y = np.random.random_sample((3,))
    z = np.random.random_sample((3,))

    CELLS = 100
    segmentosDefinidos = np.size(x, 0)
    n = segmentosDefinidos - 1
    i = 0
    t = np.linspace(0, 1, CELLS)
    b = []

    xBezier = np.zeros((1, CELLS))
    yBezier = np.zeros((1, CELLS))
    zBezier = np.zeros((1, CELLS))

    for k in range(0, segmentosDefinidos):
        b.append(basisFunction(n, i, t))

        xBezier = basisFunction(n, i, t) * x[k] + xBezier
        yBezier = basisFunction(n, i, t) * y[k] + yBezier
        #zBezier = basisFunction(n, i , t) * z[k] + zBezier
        i += 1

    for line in b:
        plt.plot(t, line)
    plt.show()

    fig1 = plt.figure(figsize=(4,4))
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(x,y,z, c="black")
    ax1.plot(xBezier[0], yBezier[0], zBezier[0], c='blue')
    plt.show()

def Ni(n,i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def basisFunction(n, i, t):
    J = np.array(Ni(n,i) * (t**i) * (1-t) ** (n-i))
    return J