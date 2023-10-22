#  Copied from
#  https://github.com/proflynch/CRC-Press/blob/main/Anaconda%20Files/Program_14d.py
#
# Program_14d.py: Three Body Problem.
import matplotlib.pyplot as plt
from numpy.linalg import norm

import setup_3body as s3b
from setup_3body import Delta, Body
import thethreebodies as t3b

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


DOT_EQUALS = 2_000
LINE_EQUALS = 100_000


def progress_indicator(i, n):

    if i == 0:
        print(f'Each dot represents {DOT_EQUALS:,} iterations out of {n:,}.')
        return

    if i % DOT_EQUALS == 0:
        print('.', end='')
        if i % LINE_EQUALS == 0:
            print(f' {i:>12,}', end='\n')


def generate_list(setup_func, n, dt):

    Body.prepare_for_sim(n, dt)
    body1, body2, body3 = setup_func()

    # Solve using Euler's numerical method.
    for i in range(n-1):
        progress_indicator(i, n)

        delta1, delta2, delta3 = planets(body1.history_at(i),
                                         body2.history_at(i),
                                         body3.history_at(i))
        body1.update(i, delta1)
        body2.update(i, delta2)
        body3.update(i, delta3)

    return t3b.TheThreeBodies(body1, body2, body3)


def plot_body(this_ax, r, color):
    this_ax.plot(r[:, 0],  r[:,  1], r[:, 2],  "--", color=color, linewidth=0.5)
    this_ax.plot(r[-1, 0], r[-1, 1], r[-1, 2], "o",  color=color, markersize=10)


def _add_centered_title(text, above_the_drawing, fontsize, *, linespacing=1.0, va="bottom"):
    plt.annotate(
        text=text,
        xy=(0.5, above_the_drawing),
        xycoords="axes fraction", ha="center", va=va,
        fontsize=fontsize, linespacing=linespacing
    )


def plot_system(the_system, n, dt, start=0, stop=None):

    history_of_bodies_positions = the_system.get_plotting_data(start, stop)

    ax = plt.figure(figsize=(10, 12)).add_subplot(projection='3d')

    _add_centered_title(
        "Three Body Interaction",
        above_the_drawing=1.07, fontsize=30
    )
    _add_centered_title(
        f"{n=:,}  {dt=:f} ",
        above_the_drawing=1.03, fontsize=8
    )

    plt.rcParams["font.size"] = "6"

    max_axis = max(h.max() for h in history_of_bodies_positions)
    ax.set_xlim(-max_axis, max_axis)
    ax.set_ylim(-max_axis, max_axis)
    ax.set_zlim(-max_axis, max_axis)

    for history_of_body, color in zip(history_of_bodies_positions,
                                      ['orange', 'red', 'blue']):
        plot_body(ax, history_of_body, color)

    ax.set_xlabel("x(t)")
    ax.set_ylabel("y(t)")
    ax.set_zlabel("z(t)")

    ax.view_init(-120, 20)

    plt.show()


DEFAULT_ITERATION, DEFAULT_TIME_INTERVAL = 1_600_000, 0.000_01


def main(speed_up=10):

    n = int(DEFAULT_ITERATION/speed_up)
    dt = DEFAULT_TIME_INTERVAL * speed_up

    # n = 30_000_000

    the_system = generate_list(s3b.moth_1, n, dt)

    plot_system(the_system, n, dt)

    return the_system

if __name__ == '__main__':
    main()
