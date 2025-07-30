import pytest
from utils.number_theory import get_proper_divisors, fibonacci_until, count_digits


class TestGetProperDivisors:
    def test_one(self):
        result = get_proper_divisors(1)
        assert result == []

    def test_prime(self):
        assert get_proper_divisors(2) == [1]
        assert get_proper_divisors(3) == [1]
        assert get_proper_divisors(7) == [1]
        assert get_proper_divisors(13) == [1]

    def test_perfect_square(self):
        result = get_proper_divisors(4)
        assert sorted(result) == [1, 2]

        result = get_proper_divisors(9)
        assert sorted(result) == [1, 3]

        result = get_proper_divisors(16)
        assert sorted(result) == [1, 2, 4, 8]

    def test_composite(self):
        result = get_proper_divisors(6)
        assert sorted(result) == [1, 2, 3]

        result = get_proper_divisors(12)
        assert sorted(result) == [1, 2, 3, 4, 6]

        result = get_proper_divisors(20)
        assert sorted(result) == [1, 2, 4, 5, 10]

    def test_larger_numbers(self):
        result = get_proper_divisors(28)
        assert sorted(result) == [1, 2, 4, 7, 14]

        result = get_proper_divisors(100)
        assert sorted(result) == [1, 2, 4, 5, 10, 20, 25, 50]

    def test_input_zero(self):
        with pytest.raises(ValueError):
            get_proper_divisors(0)

    def test_negative_number(self):
        with pytest.raises(ValueError):
            get_proper_divisors(-6)


class TestFibonacciUntil:
    def test_base_cases(self):
        assert fibonacci_until(1) == 1
        assert fibonacci_until(2) == 3

    def test_exact_fibonacci_values(self):
        assert fibonacci_until(1) == 1
        assert fibonacci_until(2) == 3
        assert fibonacci_until(3) == 4
        assert fibonacci_until(5) == 5
        assert fibonacci_until(8) == 6
        assert fibonacci_until(13) == 7
        assert fibonacci_until(21) == 8

    def test_between_fibonacci_values(self):
        assert fibonacci_until(4) == 5
        assert fibonacci_until(6) == 6
        assert fibonacci_until(9) == 7
        assert fibonacci_until(14) == 8

    def test_larger_values(self):
        assert fibonacci_until(55) == 10
        assert fibonacci_until(100) == 12
        assert fibonacci_until(1000) == 17

    def test_power_of_10_targets(self):
        assert fibonacci_until(10) == 7
        assert fibonacci_until(100) == 12
        assert fibonacci_until(1000) == 17


class TestCountDigits:
    def test_zero(self):
        assert count_digits(0) == 1

    def test_single_digit_positive(self):
        assert count_digits(1) == 1
        assert count_digits(5) == 1
        assert count_digits(9) == 1

    def test_single_digit_negative(self):
        assert count_digits(-1) == 1
        assert count_digits(-5) == 1
        assert count_digits(-9) == 1

    def test_two_digit_numbers(self):
        assert count_digits(10) == 2
        assert count_digits(25) == 2
        assert count_digits(99) == 2
        assert count_digits(-10) == 2
        assert count_digits(-25) == 2
        assert count_digits(-99) == 2

    def test_three_digit_numbers(self):
        assert count_digits(100) == 3
        assert count_digits(456) == 3
        assert count_digits(999) == 3
        assert count_digits(-100) == 3
        assert count_digits(-456) == 3
        assert count_digits(-999) == 3

    def test_larger_numbers(self):
        assert count_digits(1000) == 4
        assert count_digits(12345) == 5
        assert count_digits(1000000) == 7
        assert count_digits(-1000) == 4
        assert count_digits(-12345) == 5
        assert count_digits(-1000000) == 7

    def test_very_large_numbers(self):
        assert count_digits(123456789012345) == 15
        assert count_digits(-123456789012345) == 15
