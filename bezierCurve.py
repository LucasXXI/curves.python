import math
import numpy as np
import matplotlib.pyplot as plt

def BezierCurveChart():
    # Gera pontos de controle aleatórios para x, y, z
    x = np.random.random_sample((3,))
    y = np.random.random_sample((3,))
    z = np.random.random_sample((3,))

    # Define a resolução da curva
    CELLS = 100
    # Calcula o número de segmentos/pontos de controle
    segmentosDefinidos = np.size(x, 0)
    # Grau da curva de Bézier
    n = segmentosDefinidos - 1
    i = 0
    # Gera 100 valores de t entre 0 e 1
    t = np.linspace(0, 1, CELLS)

    # Inicializa as matrizes para armazenar os valores da curva de Bézier
    xBezier = np.zeros((1, CELLS))
    yBezier = np.zeros((1, CELLS))
    zBezier = np.zeros((1, CELLS))

    # Lista para armazenar as funções de base
    b = []

    for k in range(0, segmentosDefinidos):
        # Calcula a contribuição do ponto de controle atual
        b.append(basisFunction(n, i, t))

        # Calcula as coordenadas da curva de Bézier
        xBezier = basisFunction(n, i, t) * x[k] + xBezier
        yBezier = basisFunction(n, i, t) * y[k] + yBezier
        #zBezier = basisFunction(n, i , t) * z[k] + zBezier
        i += 1

    # Plota as funções de base
    for line in b:
        plt.plot(t, line)
    plt.show()

    # Plota a curva de Bézier e os pontos de controle no espaço 3D
    fig1 = plt.figure(figsize=(4,4))
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(x,y,z, c="black")  # Pontos de controle
    ax1.plot(xBezier[0], yBezier[0], zBezier[0], c='blue')  # Curva de Bézier
    plt.show()

# Calcula o coeficiente binomial
def Ni(n,i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

# Define a função de base (polinômios de Bernstein)
def basisFunction(n, i, t):
    J = np.array(Ni(n,i) * (t**i) * (1-t) ** (n-i))
    return J