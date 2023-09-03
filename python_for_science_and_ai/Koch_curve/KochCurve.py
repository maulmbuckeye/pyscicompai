from turtle import *

speed(0)


def KochCurve(length, level):  # noqa
    if level == 0:
        fd(length)
        return

    KochCurve(length/3, level-1)
    lt(60)
    KochCurve(length/3, level-1)
    rt(120)
    KochCurve(length/3, level-1)
    lt(60)
    KochCurve(length/3, level-1)


if __name__ == '__main__':
    KochCurve(300, 4)
    input("Hit enter to finish")



