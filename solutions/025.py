from utils.number_theory import count_digits, fibonacci


def solve() -> int:
    x = 1
    fibonacci_number = 0
    while count_digits(fibonacci_number) < 1000:
        fibonacci_number = fibonacci(x)
        x += 1
    return x


if __name__ == "__main__":
    print(solve())
