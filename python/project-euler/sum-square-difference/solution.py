"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i ** 2
    return sum_squares


def square_of_sums(n):
    return sum(list(range(1, n + 1))) ** 2


def sum_square_difference(n):
    return square_of_sums(n) - sum_of_squares(n)


print(sum_square_difference(100))