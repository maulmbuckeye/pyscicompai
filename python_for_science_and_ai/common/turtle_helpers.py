import random
import turtle as t


class render_quickly:

    def __enter__(self):
        t.delay(0)
        t.tracer(1000)
        t.speed('fastest')

    def __exit__(self, type, value, traceback):
        t.update()


def setup_start(x, y, heading):
    t.penup()
    t.setpos(x, y)
    t.setheading(heading)


def jitter(amount):
    return random.normalvariate(0, amount)
