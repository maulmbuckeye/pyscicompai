#  Copied from
#  https://github.com/proflynch/CRC-Press/blob/main/Anaconda%20Files/Program_14d.py
#

# Program_14d.py: Three Body Problem.
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


def Planets(r1, r2, r3, v1, v2, v3, G=1, m1=100, m2=1, m3=1):  # noqa
    r12, r13, r23 = norm(r1-r2), norm(r1-r3), norm(r2-r3)
    dr1, dr2, dr3 = v1, v2, v3   # noqa
    dv1 = -G*m2*(r1-r2)/r12**3 - G*m3*(r1-r3)/r13**3  # noqa
    dv2 = -G*m3*(r2-r3)/r23**3 - G*m1*(r2-r1)/r12**3  # noqa
    dv3 = -G*m1*(r3-r1)/r13**3 - G*m2*(r3-r2)/r23**3  # noqa
    return dr1, dr2, dr3, dv1, dv2, dv3


def generate_list():
    n, dt = 10_000, 0.000_01  # noqa

    r1, r2, r3 = np.zeros((n, 3)), np.zeros((n, 3)), np.zeros((n, 3))  # noqa
    v1, v2, v3 = np.zeros((n, 3)), np.zeros((n, 3)), np.zeros((n, 3))

    # The initial conditions.
    r1[0], r2[0], r3[0] = np.array([0, 0, 0]), np.array([1, 0.1, 0]), np.array([-1, 0, 0])
    v1[0], v2[0], v3[0] = np.array([0, 0, 0]), np.array([2, 8, -2]), np.array([0, -10, 0])

    # Solve using Euler's numerical method.
    for i in range(n-1):
        dr1, dr2, dr3, dv1, dv2, dv3 = Planets(r1[i], r2[i], r3[i], v1[i], v2[i], v3[i])
        r1[i+1] = r1[i] + dr1 * dt
        r2[i+1] = r2[i] + dr2 * dt
        r3[i+1] = r3[i] + dr3 * dt
        v1[i+1] = v1[i] + dv1 * dt
        v2[i+1] = v2[i] + dv2 * dt
        v3[i+1] = v3[i] + dv3 * dt

    return r1, r2, r3, n


r1, r2, r3, n = generate_list()

xmax = 2
ax = plt.figure(figsize=(10, 12)).add_subplot(projection='3d')
plt.rcParams["font.size"] = "6"
plt.xlim(-xmax, xmax)
plt.ylim(-xmax, xmax)

ax.plot(r1[:, 0],   r1[:, 1],   r1[:, 2],   "--", color="orange")
ax.plot(r1[n-1, 0], r1[n-1, 1], r1[n-1, 2], "o",  color="orange", markersize=10)
ax.plot(r2[:, 0],   r2[:, 1],   r2[:, 2],   "--", color="red")
ax.plot(r2[n-1, 0], r2[n-1, 1], r2[n-1, 2], "o", color="red", markersize=10)
ax.plot(r3[:, 0],   r3[:, 1],   r3[:, 2],   "--", color="blue")
ax.plot(r3[n-1, 0], r3[n-1, 1], r3[n-1, 2], "o", color="blue", markersize=10)

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")

ax.view_init(-120, 20)

plt.show()
