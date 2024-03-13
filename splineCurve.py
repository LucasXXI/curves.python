import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

def SplineChart():
    # Define os pontos de controle para a interpolação
    x = np.array([1,6,7,9,12,20])
    y = np.array([2,8,6,10,14,41])

    # Cria um conjunto de pontos para interpolação, aumentando a densidade de pontos entre o mínimo e o máximo de x
    x_interp = np.linspace(np.min(x), np.max(x), 50)

    # Realiza interpolação linear, criando uma curva spline que conecta todos os pontos de controle com segmentos de linha reta
    y_linear = interp1d(x,y)

    # Realiza interpolação quadrática, utilizando polinômios de segundo grau para conectar os pontos
    y_quadratic = interp1d(x, y, kind='quadratic')

    # Realiza interpolação cúbica, utilizando polinômios de terceiro grau para uma curva mais suave
    y_cubic = interp1d(x, y, kind='cubic')

    # Interpolação cúbica com variáveis de contorno definidas como "natural", criando uma spline cúbica que tem sua segunda derivada igual a zero nos pontos extremos
    y_cubicBc = CubicSpline(x, y, bc_type="natural")

    # Plota os pontos de controle
    plt.plot(x, y, "o", label="Data Points")

    # Plota as splines resultantes com diferentes graus e condições
    plt.plot(x_interp, y_linear(x_interp), "red", label="Linear Spline")
    plt.plot(x_interp, y_quadratic(x_interp), "green", label="Quadratic Spline")
    plt.plot(x_interp, y_cubic(x_interp), "pink", label="Cubic Spline")
    plt.plot(x_interp, y_cubicBc(x_interp), "black", label="Cubic Spline BC")

    # Adiciona legenda e exibe o gráfico
    plt.legend()
    plt.show()