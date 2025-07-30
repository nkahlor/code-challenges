from utils.number_theory import fibonacci_until


def fibonacci_nth_digits(n_digits: int) -> int:
    return fibonacci_until(pow(10, n_digits - 1))


def solve() -> int:
    return fibonacci_nth_digits(1000)


if __name__ == "__main__":
    print(solve())
