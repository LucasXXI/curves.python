import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline


def SplineChart():
    x = np.array([1,6,7,9,12,20])
    y = np.array([2,8,6,10,14,41])

    x_interp = np.linspace(np.min(x), np.max(x), 50)

    #interpolação sem variaveis de contorno, apenas alterando o tipo de interpolação
    y_linear = interp1d(x,y)
    y_quadratic = interp1d(x, y, kind='quadratic')
    y_cubic = interp1d(x, y, kind='cubic')

    #interpolacao com variaveis de contorno
    y_cubicBc = CubicSpline(x, y, bc_type="natural")

    plt.plot(x,y, "o", label="Data Points")
    plt.plot(x_interp, y_linear(x_interp), "red", label="Linear Spline")
    plt.plot(x_interp, y_quadratic(x_interp), "green", label="Quadratic Spline")
    plt.plot(x_interp, y_cubic(x_interp), "pink", label="Cubic Spline")
    plt.plot(x_interp, y_cubicBc(x_interp), "black", label="Cubic Spline BC")

    plt.legend()
    plt.show()