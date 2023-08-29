def fac(n: int) -> list[int]:
    for possible_factor in range(2, n+1):
        if n % possible_factor == 0:
            return [possible_factor] + fac(n // possible_factor)
    return []
