"""
Adding a digit increases the size of the number faster than the sum can keep up.
Therefore, there is an upper bound to the number of digits we can add before all
numbers are disqualified.

The smallest x digit number can be expressed as 10**x.
The largest possible sum of n powers of x digits, is (9**n) * x
Therefore, the upper bound of digits occurs for the first x such that 10**x > (9**n) * x
"""

from itertools import product


def smallest_x_digit_number(x: int) -> int:
    return 10**x


def largest_sum_of_powers(n: int, x: int) -> int:
    return (9**n) * x


def is_nth_sum_of_digits(test_number: int, n: int) -> bool:
    x = test_number
    sum_of_digits = 0
    while x > 0:
        digit = x % 10
        sum_of_digits += digit**n
        x //= 10
    return sum_of_digits == test_number


def solve() -> int:
    possible_terms: dict[int, int] = {}
    num_digits = 1
    n = 5
    for digit in range(0, 10):
        possible_terms.setdefault(digit, digit**n)

    while smallest_x_digit_number(num_digits) < largest_sum_of_powers(n, num_digits):
        num_digits += 1
    # at this point, we know the answer has at most num_digits
    # start at largest_sum_of_powers for num_digits, and start dropping each digit until we get a hit
    result: set[int] = set()
    for i in range(num_digits + 1):
        for terms in product(range(10), repeat=i):
            sum_of_powers = sum([possible_terms[x] for x in terms])
            if is_nth_sum_of_digits(sum_of_powers, n):
                result.add(sum_of_powers)
    result.remove(0)
    result.remove(1)
    return sum(result)


if __name__ == "__main__":
    print(solve())
