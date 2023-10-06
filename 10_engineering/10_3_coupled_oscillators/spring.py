import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m1, m2 = 1, 2
k1, k2, k3 = 1, 2, 3
x10, y10 = 0, 0
x20, y20 = 1, 0

tmax, n = 100, 1001


def mass_spring(x, t, m1, m2, k1, k2, k3):  # noqa
    _x1, _y1, _x2, _y2 = x
    dx1 = _y1
    dy1 = -(k1 * _x1 + k2 * (_x1 - _x2)) / m1
    dx2 = _y2
    dy2 = -(k2 * (_x2 - _x1) + k3 * _x2) / m2
    return dx1, dy1, dx2, dy2


t = np.linspace(0, tmax, n)
f = odeint(mass_spring, (x10, y10, x20, y20), t, args=(m1, m2, k1, k2, k3))

x1, y1, x2, y2 = f.transpose() # noqa

plt.figure(1)
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Two-Mass, Three-Spring")
plt.plot(t, x1, label="x1")
plt.plot(t, x2, label="x2")
legend = plt.legend(loc="best")
plt.show()


