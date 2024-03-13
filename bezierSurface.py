import math
import numpy as np
import matplotlib.pyplot as plt

def BezierSurfaceChart():
    # Pontos de controle definidos para as coordenadas x, y e z
    x = np.asarray([[-0.5, -2, 0], [1., 1, 1], [2, 2, 2]])
    y = np.asarray([[2, 1, 0], [2, 0, -1], [2, 1, 1]])
    z = np.asarray([[1, -1, 2], [0, -0.5, 2], [0.5, 1, 2]])

    # Define a resolução da superfície nas direções u e w
    uCELLS = 12
    wCELLS = 10

    # Calcula o número de pontos de controle em cada direção
    uPTS = np.size(x, 0)
    wPTS = np.size(x, 1)

    # Graus da superfície de Bézier nas direções u e w
    n = uPTS - 1
    m = wPTS - 1

    # Gera vetores paramétricos u e w
    u = np.linspace(0, 1, uCELLS)
    w = np.linspace(0, 1, wCELLS)

    # Inicializa listas para armazenar as funções de base
    b = []
    d = []

    # Inicializa matrizes para as coordenadas da superfície de Bézier
    xBezier = np.zeros((uCELLS, wCELLS))
    yBezier = np.zeros((uCELLS, wCELLS))
    zBezier = np.zeros((uCELLS, wCELLS))

    # Itera sobre os pontos de controle
    for i in range(0, uPTS):
        for j in range(0, wPTS):
            # Calcula as funções de base para cada direção
            b.append(J(n, i, u))
            d.append(K(m, j, w))

            # Transpõe a matriz de funções de base J para a multiplicação correta
            Jt = J(n, i, u).T

            # Calcula as coordenadas da superfície de Bézier
            xBezier += Jt * K(m, j, w) * x[i, j]
            yBezier += Jt * K(m, j, w) * y[i, j]
            zBezier += Jt * K(m, j, w) * z[i, j]

    # Plota as funções de base para u e w
    plt.subplot(121)
    for line in b:
        plt.plot(u, line.T)
    plt.subplot(122)
    for line in d:
        plt.plot(w, line.T)
    plt.show()

    # Visualiza a superfície de Bézier e os pontos de controle no espaço 3D
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_surface(xBezier, yBezier, zBezier)
    ax.scatter(x.flatten(), y.flatten(), z.flatten(), edgecolors='face')
    plt.show()

# Calcula o coeficiente binomial para a direção u
def Ni(n,i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

# Calcula o coeficiente binomial para a direção w
def Mj(m,j):
    return math.factorial(m) / (math.factorial(j) * math.factorial(m - j))

# Define a função de base J para a direção u
def J(n, i ,u):
    return np.matrix(Ni(n, i) * (u**i) * (1-u) ** (n-i))

# Define a função de base K para a direção w
def K(m, j ,w):
    return np.matrix(Mj(m, j) * (w ** j) * (1 - w) ** (m - j))

BezierSurfaceChart()