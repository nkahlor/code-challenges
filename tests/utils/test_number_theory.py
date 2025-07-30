import pytest
from utils.number_theory import get_proper_divisors


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
