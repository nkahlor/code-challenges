from typing import OrderedDict
from utils.number_theory import get_proper_divisors


def is_abundant(n: int) -> bool:
    divisors = get_proper_divisors(n)
    return sum(divisors) > n


def is_abundant_sum(abundant_numbers: OrderedDict[int, int], n: int) -> bool:
    number_list = list(abundant_numbers.keys())
    start = 0
    end = len(number_list) - 1
    for _ in range(len(number_list)):
        abundant_sum = number_list[start] + number_list[end]
        double_start = number_list[start] * 2
        double_end = number_list[end] * 2
        if abundant_sum == n or double_start == n or double_end == n:
            return True
        if abundant_sum < n:
            start += 1
        else:
            end -= 1
    return False


def solve() -> int:
    abundant_sums: list[int] = []
    non_abundant_sum = 0
    abundant_numbers: OrderedDict[int, int] = OrderedDict()
    for n in range(1, 28124):
        if is_abundant(n):
            abundant_numbers.setdefault(n, n)
        if not is_abundant_sum(abundant_numbers, n):
            non_abundant_sum += n
        else:
            abundant_sums.append(n)

    return non_abundant_sum


if __name__ == "__main__":
    print(solve())
