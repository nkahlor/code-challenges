"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time


def is_palindrome(x):
    str_x = str(x)
    j = len(str_x) - 1
    for i in range(len(str_x)):
        if str_x[i] != str_x[j]:
            return False
        j = j - 1
    return True


def largest_palindrome_product(num_digits):
    largest_number = 10 ** num_digits - 1
    smallest_number = 10 ** (num_digits - 1) 

    max_pal = -1

    max_j_val = largest_number
    for i in range(largest_number, smallest_number, -1):
        for j in range(max_j_val, smallest_number, -1):
            product = i * j
            if is_palindrome(product):
                if product > max_pal:
                    max_pal = product
        max_j_val = max_j_val - 1
    return max_pal

start = time.perf_counter()
print(largest_palindrome_product(3))
end = time.perf_counter()
print(end - start)