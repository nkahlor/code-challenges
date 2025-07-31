"""
start at 1
add 2 4 times,
add 4 4 times,
add 6 4 times,
repeat until you hit the end
"""


def solve() -> int:
    diagonal_sum = 1
    diagonal_value = 1
    for i in range(3, 1002, 2):
        for _ in [0, 1, 2, 3, 4]:
            diagonal_value += i - 1
            diagonal_sum += diagonal_value
    return diagonal_sum


if __name__ == "__main__":
    print(solve())
