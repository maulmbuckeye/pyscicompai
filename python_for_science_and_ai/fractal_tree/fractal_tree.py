
from turtle import *
import common.turtle_helpers as th


def main():

    levels = get_levels()

    with th.render_quickly():
        th.setup_start(0, -250, 90)
        draw_branch(200, levels)

    th.wait_to_close_turtle_window()


def get_levels():
    levels = numinput("Parameters", "Depth of branches off trunk",
                      default=9, minval=0, maxval=15)
    if levels is None:
        print("Thanks for playing")
        exit()
    return levels


def drawing_steps(option: str, length) -> list:
    if option == "2 branch":
        return [(30, length * 0.7),
                (-60, length * 0.5)]
    if option == "3 branch":
        return [(35, length * 0.7),
                (-70, length * 0.5),
                (-10, length * 0.5)]
    if option == "balanced 4":
        return [(60, length * 0.7),
                (-60, length * 0.7),
                (20, length * 0.7),
                (-20, length * 0.7)]


def draw_branch(length, depth_of_this_branch):
    """ Draw a branch (or trunk) of length.
    Level is the number of sub-branches.

    The turtle position and direction of the turtle will now change,
    i.e, this routine cleans up afer itself"""

    if depth_of_this_branch < 0:
        return

    pensize(length/10)
    pencolor("green" if length < 20 else "brown")

    with draw_this_branch(length + th.jitter(length * 0.25)):
        for angle, l in drawing_steps("balanced 4",
                                      length):
            draw_sub_branch(turn_right=angle,
                            sub_branch_length=l,
                            depth_of_parent_branch=depth_of_this_branch)


class draw_this_branch:
    _length = 0

    def __init__(self, this_branch_length):
        self._length = this_branch_length

    def __enter__(self):
        pendown()
        fd(self._length)

    def __exit__(self, t, v, tb):
        penup()
        bk(self._length)


def draw_sub_branch(turn_right, sub_branch_length, depth_of_parent_branch):
    this_turn = turn_right + th.jitter(5)
    rt(this_turn)
    draw_branch(sub_branch_length, depth_of_parent_branch - 1)
    lt(this_turn)


if __name__ == '__main__':
    main()
