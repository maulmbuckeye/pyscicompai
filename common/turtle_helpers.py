import random
import turtle as t


class render_quickly:

    def __enter__(self):
        t.delay(0)
        t.tracer(10000)
        t.speed('fastest')

    def __exit__(self, _, value, traceback):
        t.update()


def setup_start(x, y, heading):
    t.penup()
    t.setpos(x, y)
    t.setheading(heading)


class Jitter:

    _has_jitter = True

    @classmethod
    def set(cls, has_jitter):
        cls._has_jitter = has_jitter

    @classmethod
    def jit(cls, amount):
        if cls._has_jitter:
            return random.normalvariate(0, amount)
        else:
            return 0


def wait_to_close_turtle_window():
    input("Hit enter to end")
