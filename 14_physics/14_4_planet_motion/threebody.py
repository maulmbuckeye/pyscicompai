#  Copied from
#  https://github.com/proflynch/CRC-Press/blob/main/Anaconda%20Files/Program_14d.py
#
# Program_14d.py: Three Body Problem.
from collections import namedtuple

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


GRAVITY = 1

Position = namedtuple('Position', ['r', 'v', 'm'])
Delta = namedtuple('Delta', ['dr', 'dv'])


def delta_v(source, buddy):
    norm_cubed = norm(source.r - buddy.r) ** 3
    res = -GRAVITY * buddy.m * (source.r - buddy.r) / norm_cubed
    return res


def planets(body1, body2, body3):

    dr1, dr2, dr3 = body1.v, body2.v, body3.v
    dv1 = delta_v(body1, body2) + delta_v(body1, body3)
    dv2 = delta_v(body2, body1) + delta_v(body2, body3)
    dv3 = delta_v(body3, body1) + delta_v(body3, body2)
    return Delta(dr1, dv1), Delta(dr2, dv2), Delta(dr3, dv3)


class Body:
    def __init__(self, n, *, r, velocity, m=1):
        self.v = np.zeros((n, 3))
        self.v[0] = velocity
        self.r = np.zeros((n, 3))
        self.r[0] = r
        self.m = m

    def current(self, i):
        return Position(self.r[i], self.v[i], self.m)


def generate_list(speed_up=1):
    n, dt = 800_000, 0.000_01
    n = int(n/speed_up)
    dt *= speed_up

    body1 = Body(n, r=[0, 0, 0], velocity=[0,   0,  0], m=100)
    body2 = Body(n, r=[1, 0.1, 0], velocity=[1,   9, -1])
    body3 = Body(n, r=[-1, 0, 0], velocity=[0, -10,  0])

    # Solve using Euler's numerical method.
    for i in range(n-1):
        delta1, delta2, delta3 = planets(body1.current(i), body2.current(i), body3.current(i))
        dr1, dv1 = delta1
        dr2, dv2 = delta2
        dr3, dv3 = delta3
        body1.r[i+1] = body1.r[i] + dr1 * dt
        body2.r[i+1] = body2.r[i] + dr2 * dt
        body3.r[i+1] = body3.r[i] + dr3 * dt
        body1.v[i+1] = body1.v[i] + dv1 * dt
        body2.v[i+1] = body2.v[i] + dv2 * dt
        body3.v[i+1] = body3.v[i] + dv3 * dt

    return body1.r, body2.r, body3.r


def plot_body(this_ax, r, color):
    this_ax.plot(r[:, 0],  r[:, 1],  r[:, 2],  "--", color=color, linewidth=0.5)
    this_ax.plot(r[-1, 0], r[-1, 1], r[-1, 2], "o",  color=color, markersize=10)


r1, r2, r3 = generate_list(speed_up=100)

xmax = 2
ax = plt.figure(figsize=(10, 12)).add_subplot(projection='3d')

plt.title('Three Body Interaction', fontsize=20)
plt.rcParams["font.size"] = "6"
plt.xlim(-xmax, xmax)
plt.ylim(-xmax, xmax)
plot_body(ax, r1, 'orange')
plot_body(ax, r2, 'red')
plot_body(ax, r3, 'blue')

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")

ax.view_init(-120, 20)

plt.show()
