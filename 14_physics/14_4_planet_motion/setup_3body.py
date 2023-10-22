# noinspection PyPep8

from collections import namedtuple

import numpy as np

Position = namedtuple('Position', ['r', 'v', 'm'])
Delta = namedtuple('Delta', ['dr', 'dv'])


class Body:

    dt = None
    n = None

    def __init__(self, *, r, velocity, m=1):
        self.m = m
        self.v = np.zeros((Body.n, 3))
        self.v[0] = velocity
        self.r = np.zeros((Body.n, 3))
        self.r[0] = r

    @classmethod
    def prepare_for_sim(cls, n, dt):
        cls.n = n
        cls.dt = dt

    def history_at(self, i):
        return Position(self.r[i], self.v[i], self.m)

    def update_euler(self, i, delta):
        """ The original technic is Euler's method.
        This was the method used in _Python for Scientific Computing_, p.199
        The errors in this preventing the mole I configuratoin from remaining stable.
        """

        self.r[i+1] = self.r[i] + delta.dr * self.dt
        self.v[i+1] = self.v[i] + delta.dv * self.dt

    def update(self, i, delta):
        """ This is Semi-implicit Euder method.
        https://en.wikipedia.org/wiki/Semi-implicit_Euler_method

        Alternates include Verlet integration, Leapfrog integration, and Symplectic integrator (see Wikipedia).
         """

        self.v[i + 1] = self.v[i] + delta.dv * self.dt
        self.r[i+1] = self.r[i] + self.v[i + 1] * self.dt


def figure_eight():
    """
    A remarkable periodic solution of the three-body problem in the case of equal masses
    by Alain Chenciner and Richard Montgomery
    Annals of Mathematics, 152 (2000), 881–901
    https://arxiv.org/pdf/math/0011268.pdf
    """
    x1x =  0.970_004_36
    x1y = -0.243_087_53

    x3vx = -0.932_407_37
    x3vy = -0.864_731_46

    body1 = Body(r=[ x1x,  x1y, 0], velocity=[-x3vx/2, -x3vy/2, 0])
    body2 = Body(r=[-x1x, -x1y, 0], velocity=[-x3vx/2, -x3vy/2, 0])
    body3 = Body(r=[   0,    0, 0], velocity=[   x3vx,    x3vy, 0])

    return body1, body2, body3


def conditions_i():
    body1 = Body(r=[0, 0, 0],  velocity=[0,   0, 0], m=100)
    body2 = Body(r=[1, 0, 0],  velocity=[0,  10, 0])
    body3 = Body(r=[-1, 0, 0], velocity=[0, -10, 0])

    return body1, body2, body3


def conditions_ii():
    body1 = Body(r=[ 0, 0, 0], velocity=[0,   0, 0], m=100)
    body2 = Body(r=[ 1, 0, 1], velocity=[0,  10, 0])
    body3 = Body(r=[-1, 0, 1], velocity=[0, -10, 0])

    return body1, body2, body3


def conditions_iii():
    body1 = Body(r=[ 0,   0, 0], velocity=[0,   0,  0], m=100)
    body2 = Body(r=[ 1, 0.1, 0], velocity=[1,   9, -1])
    body3 = Body(r=[-1,   0, 0], velocity=[0, -10,  0])

    return body1, body2, body3


def hand_in_hand_in_oval():
    """
    NAME: Hand-in-hand-in-oval
    DISCOVERED: 2016 by Matthew Sheen
    http://three-body.ipb.ac.rs/sheen_sol.php?id=3

    Worked with Semi-implicit Euler
    n=80,000 dt=0.0001

    """
    body1 = Body(r=[ 0.906009977921,  0.347143444587, 0], velocity=[ 0.242474965162,  1.045019736387, 0])
    body2 = Body(r=[-0.263245299491,  0.140120037700, 0], velocity=[-0.360704684300, -0.807167979922, 0])
    body3 = Body(r=[-0.252150695248, -0.661320078799, 0], velocity=[ 0.118229719138, -0.237851756465, 0])

    return body1, body2, body3


def moth_1():
    """
    NAME: Moth 1
    DISCOVERED: 2012

    Worked with Semi-implicit Euler
    n=1,600,000 dt=0.000 1
    """
    p1 = 0.464_445
    p2 = 0.396_060
    body1 = Body(r=[-1, 0, 0], velocity=[   p1,    p2, 0])
    body2 = Body(r=[ 1, 0, 0], velocity=[   p1,    p2, 0])
    body3 = Body(r=[ 0, 0, 0], velocity=[-2*p1, -2*p2, 0])

    return body1, body2, body3
