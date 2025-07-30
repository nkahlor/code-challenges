from utils.number_theory import get_proper_divisors


def sum_proper_divisors(n: int) -> int:
    return sum(get_proper_divisors(n))


def solve(n: int = 10000) -> int:
    amicable_numbers: set[int] = set()

    for a in range(1, n):
        b = sum_proper_divisors(a)
        if b > 0:
            possibly_amicable = sum_proper_divisors(b)
            if a == possibly_amicable and a != b:
                amicable_numbers.add(a)
                amicable_numbers.add(b)

    return sum(amicable_numbers)


if __name__ == "__main__":
    print(solve())
