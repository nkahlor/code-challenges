from math import isqrt, log10
from typing import Generator


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


def fibonacci_until(target_value: int) -> int:
    if target_value <= 1:
        return 1

    i, a, b = 2, 1, 1
    while b < target_value:
        a, b = b, a + b
        i += 1
    return i


def count_digits(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return int(log10(n)) + 1
    else:
        return int(log10(-n)) + 1


def is_prime(n: int) -> bool:
    if n <= 0:
        return False
    if n % 2 == 0 and n != 2:
        return False

    for i in range(isqrt(n), 1, -1):
        if n % i == 0:
            return False
    return True


def prime_numbers() -> Generator[int]:
    D: dict[int, list[int]] = {}
    q: int = 2
    while True:
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
