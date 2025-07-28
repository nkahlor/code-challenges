from math import isqrt


def get_divisors(n: int) -> list[int]:
    sqrt_n = isqrt(n)
    divisors: list[int] = []

    for divisor in range(1, sqrt_n + 1):
        if n % divisor == 0:
            divisors.append(divisor)
            divisor_pair = n // divisor
            if divisor != divisor_pair:
                divisors.append(divisor_pair)
    return divisors
