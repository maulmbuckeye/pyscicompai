#  Copied from
#  https://github.com/proflynch/CRC-Press/blob/main/Anaconda%20Files/Program_14d.py
#
# Program_14d.py: Three Body Problem.
import matplotlib.pyplot as plt
from numpy.linalg import norm

import setup_3body as s3b
from setup_3body import Delta

GRAVITY = 1


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


def progress_indicator(i):
    if i % 2_000 == 0:
        print('.', end='')
        if i % 100_000 == 0:
            print(end='\n')


def generate_list(setup_func, speed_up=1):
    n, dt = 800_000, 0.000_001
    n = int(n/speed_up)
    dt *= speed_up

    body1, body2, body3 = setup_func()
    for body in (body1, body2, body3):
        body.prepare_for_sim(n, dt)

    # Solve using Euler's numerical method.
    for i in range(n-1):
        progress_indicator(i)

        delta1, delta2, delta3 = planets(body1.history_at(i),
                                         body2.history_at(i),
                                         body3.history_at(i))

        body1.update(i, delta1)
        body2.update(i, delta2)
        body3.update(i, delta3)

    return body1.r, body2.r, body3.r


def plot_body(this_ax, r, color):
    this_ax.plot(r[:, 0],  r[:, 1],  r[:, 2],  "--", color=color, linewidth=0.5)
    this_ax.plot(r[-1, 0], r[-1, 1], r[-1, 2], "o",  color=color, markersize=10)


r1, r2, r3 = generate_list(s3b.conditions_i, speed_up=100)

xmax = 3
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
