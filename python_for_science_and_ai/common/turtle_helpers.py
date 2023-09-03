import turtle as t


def render_quickly():
    t.delay(0)
    t.tracer(1000)
    t.speed('fastest')


def setup_start(x,y, heading):
    t.penup()
    t.setpos(x,y)
    t.setheading(heading)