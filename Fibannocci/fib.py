import abc
from abc import ABC
from math import sqrt, pow


class FibGenerator(ABC):

    @abc.abstractmethod
    def fib(self, n: int) -> int:
        ...

    def print_summary(self, n):
        print(f"fib({n}) = {self.fib(n):,d}")


class RecursiveFibGen (FibGenerator):

    def fib(self, n: int) -> int:
        if n in {1, 2}:
            return 1
        return self.fib(n-1) + self.fib(n-2)


class LoopFibGen (FibGenerator):

    def fib(self, n: int) -> int:
        f2 = 0
        f1 = 1
        for _ in range(n):
            f2, f1 = f1, f1 + f2
        return f1


class RecurrenceFibGen (FibGenerator):

    r1 = (1 + sqrt(5))/2
    r2 = (1 - sqrt(5))/2

    def fib(self, n: int) -> int:
        # http://mathonline.wikidot.com/a-closed-form-of-the-fibonacci-sequence
        raw = (pow(self.r1, n) - pow(self.r2, n))/sqrt(5)
        print(n, self.r1, self.r2, raw)
        return int(raw + 0.000001)


class BorrowedFibGen(FibGenerator):
""" Take from https://medium.com/@evlabs/fibonacci-sequence-in-python-in-4-programming-styles-36199f8e416b"""
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    # RecursiveFibGen().print_summary(10)
    for i in range(1, 6):
        BorrowedFibGen().print_summary(i)

    # LoopFibGen().print_summary(50)
    # RecurrenceFibGen().print_summary(50)
    # LoopFibGen().print_summary(80)
    # RecurrenceFibGen().print_summary(80)
    # LoopFibGen().print_summary(100)
    # RecurrenceFibGen().print_summary(100)
    # LoopFibGen().print_summary(1000)
    # RecurrenceFibGen().print_summary(1000)
