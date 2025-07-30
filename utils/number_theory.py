from math import isqrt, log10


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
