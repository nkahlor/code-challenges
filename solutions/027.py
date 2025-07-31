"""
This one had me stumped at first, but I realized the trick is to identify rules of what a and b can be.

for instance, to satisfy the question we need n = 0 and n = 1 both to produce primes.

when n = 0, b is all that's left. Therefore, b must be prime.

likewise, when n = 1, the quadratic becomes 1 + a + b. Therefore, a + b + 1 must be prime.

These 2 constraints do a lot to help narrow down the solution space.
"""

from utils.number_theory import is_prime, prime_numbers


def quadratic_fn(n: int, a: int, b: int) -> int:
    return n**2 + a * n + b


def solve() -> int:
    prime_number = prime_numbers()
    possible_a_values = range(-999, 1000)
    possible_b_values: set[int] = set()
    possible_combinations: list[tuple[int, int]] = []

    b = 0
    while b < 1000:
        b = next(prime_number)
        if b < 1000:
            possible_b_values.add(b)

    for b in possible_b_values:
        for a in possible_a_values:
            if a + b <= 0:
                continue
            if is_prime(a + b + 1):
                possible_combinations.append((a, b))

    longest_a = 0
    longest_b = 0
    longest_chain = 0
    for a, b in possible_combinations:
        y = quadratic_fn(2, a, b)
        prime_chain = 2
        while y > 0 and is_prime(y):
            prime_chain += 1
            y = quadratic_fn(prime_chain, a, b)
        if longest_chain < prime_chain:
            longest_chain = prime_chain
            longest_a = a
            longest_b = b

    return longest_a * longest_b


if __name__ == "__main__":
    print(solve())
