import random
from turtle import *


def main():
    delay(0)
    tracer(1000)
    speed('fastest')

    penup()
    setpos(0, -250)
    setheading(90)

    levels = numinput("Parameters", "Depth of branches off trunk",
                      default=9, minval=0, maxval=15)

    draw_branch(200, levels)
    update()
    input("Hit enter to end")


def draw_branch(length, depth_of_this_branch):
    """ Draw a branch (or trunk) of length.
    Level is the number of sub-branches.

    The turtle position and direction of the turtle will now change,
    i.e, this routine cleans up afer itself"""

    if depth_of_this_branch < 0:
        return

    pensize(length/10)
    pencolor("green" if length < 20 else "brown")

    this_branch_length = length + random.normalvariate(0, length * 0.25)
    pendown()
    fd(this_branch_length)
    draw_sub_branch(turn_right=30,
                    sub_branch_length=length * 0.7,
                    depth_of_parent_branch=depth_of_this_branch)
    draw_sub_branch(turn_right=-60,
                    sub_branch_length=length * 0.5,
                    depth_of_parent_branch=depth_of_this_branch)
    penup()
    bk(this_branch_length)


def draw_sub_branch(turn_right, sub_branch_length, depth_of_parent_branch):
    this_turn = turn_right + random.normalvariate(0, 5)
    rt(this_turn)
    draw_branch(sub_branch_length, depth_of_parent_branch - 1)
    lt(this_turn)


if __name__ == '__main__':
    main()
