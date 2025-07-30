from math import isqrt, log10
from functools import cache


def get_proper_divisors(n: int) -> list[int]:
    if n < 1:
        raise ValueError("Input must be a positive integer")
    elif n == 1:
        return []

    sqrt_n = isqrt(n)
    divisors: list[int] = [1]

    for divisor in range(2, sqrt_n + 1):
        if n % divisor == 0:
            divisors.append(divisor)
            divisor_pair = n // divisor
            if divisor != divisor_pair:
                divisors.append(divisor_pair)

    return divisors


@cache
def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_digits(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return int(log10(n)) + 1
    else:
        return int(log10(-n)) + 1
