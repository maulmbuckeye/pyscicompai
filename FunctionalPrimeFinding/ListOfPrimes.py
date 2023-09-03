def prime(n: int) -> bool:
    """ Returns a list of all primes < n"""

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def list_of_primes(n: int) -> list[int]:
    return [n for n in range(2, n+1) if prime(n)]

