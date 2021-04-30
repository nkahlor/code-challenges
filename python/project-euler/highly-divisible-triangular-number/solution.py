from math import sqrt


def get_divisions(n, divisor):
    count = 0
    while n % divisor == 0:
        n //= divisor
        count += 1
    return n, count


def prime_factorization(n):
    if n % 2 == 0:
        n, divisions_by_2 = get_divisions(n, 2)
        factorization = [(2, divisions_by_2)]
    else:
        factorization = []
    for i in range(3, int(sqrt(n)), 2):
        n, instances = get_divisions(n, i)
        if instances > 0:
            factorization.append((i, instances))
    if n > 1:
        factorization.append((n, 1))
    return factorization


def get_divisor_count(x):
    if x == 1:
        return 1
    if x == 2 or x == 3:
        return 2
    divisor_count = 1
    factorization = prime_factorization(x)
    for factor in factorization:
        exponent, factor_count = factor
        divisor_count *= factor_count + 1
    return divisor_count


def first_triangular_number_with_over_n_divisors(n):
    count = 1
    divisor_count = -1
    last_seen_number = 0
    while divisor_count <= n:
        last_seen_number += count
        divisor_count = get_divisor_count(last_seen_number)
        count += 1
    return last_seen_number


print(first_triangular_number_with_over_n_divisors(500))
