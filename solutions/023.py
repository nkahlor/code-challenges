from utils.number_theory import get_proper_divisors


def is_abundant(n: int) -> bool:
    divisors = get_proper_divisors(n)
    return sum(divisors) > n


def not_abundant_sum(abundant_numbers: set[int], n: int) -> bool:
    for abundant_number in abundant_numbers:
        if abundant_number > n // 2:
            break
        if (n - abundant_number) in abundant_numbers:
            return False
    return True


def solve() -> int:
    non_abundant_sum = 0
    abundant_numbers: set[int] = set()
    for n in range(12, 28124):
        if is_abundant(n):
            abundant_numbers.add(n)

    for n in range(1, 28124):
        if not_abundant_sum(abundant_numbers, n):
            non_abundant_sum += n

    return non_abundant_sum


if __name__ == "__main__":
    print(solve())
