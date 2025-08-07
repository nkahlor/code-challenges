"""
The smallest product of two 3 digit numbers is 100 * 100 = 10,000, the digit sum is > 9 so we know:
count_digits(x) + count_digits(y) < 6

The largest product of two 2 digit numbers is 99 * 99 = 9801, the digit sum is < 9 so we know
count_digits(x) + count_digits(y) > 4

Putting both constraints together, we show that
count_digits(x) + count_digits(y) == 5

Furthermore we can constrain count_digits(products):
count_digits(x) + count_digits(y) + count_digits(products) = 9
5 + count_digits(products) = 9
therefore, count_digits(products) = 4

Here are the valid combinations of x and y digit lengths:
count_digits(x) = 1, count_digits(y) = 4
count_digits(x) = 2, count_digits(y) = 3

This is good enough for a pretty solid runtime, but we can go further by constraining y
based on the current value of x:

count_digits(x) = 1, count_digits(y) = 4:
Min y: 1000/9 ~= 111.1, but y must be 4-digit, so y ≥ 1000
Max y: 9999/2 = 4999.5, so y ≤ 4999 for x=2
1234 as lower bound to avoid numbers with repeated digits early

count_digits(x) = 2, count_digits(y) = 3:
Min constraint: 1000/99 ~= 10.1, so x ≥ 11
Max constraint: 9999/100 = 99.99, so y ≤ 99 (but y must be 3-digit)

"""

from utils.number_theory import count_digits


def is_pandigital(
    nums: list[int], digits: frozenset[int] = frozenset([1, 2, 3, 4, 5, 6, 7, 8, 9])
) -> bool:
    counter = set(digits)
    for num in nums:
        while num > 0:
            digit = num % 10
            if digit not in counter:
                return False
            counter.remove(digit)
            num //= 10
    return len(counter) == 0


def solve() -> int:
    result: set[int] = set()
    for x in range(2, 10):
        min_y = max(1234, 1000 // x)
        max_y = min(9876, 9876 // x)
        for y in range(min_y, max_y + 1):
            product = x * y
            if count_digits(product) == 4 and is_pandigital([x, y, product]):
                result.add(product)

    for x in range(12, 100):
        min_y = max(123, 1000 // x)
        max_y = min(987, 9876 // x)
        for y in range(min_y, max_y + 1):
            product = x * y
            if count_digits(product) == 4 and is_pandigital([x, y, product]):
                result.add(product)

    return sum(result)


if __name__ == "__main__":
    print(solve())
