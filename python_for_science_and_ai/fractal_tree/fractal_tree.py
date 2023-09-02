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

    branch(200, levels)
    update()
    input("Hit enter to end")


def branch(length, depth_of_subbranches):
    """ Draw a branch (or trunk) of length.
    Level is the number of sub-branches."""

    if depth_of_subbranches < 0:
        return

    pensize(length/10)
    pencolor("green" if length < 20 else "brown")

    branch_length = length + random.normalvariate(0, length * 0)
    pendown()
    fd(branch_length)
    rt(30)
    branch(length * 0.7, depth_of_subbranches - 1)
    lt(90)
    branch(length * 0.5, depth_of_subbranches - 1)
    rt(60)
    penup()
    bk(branch_length)


if __name__ == '__main__':
    main()
