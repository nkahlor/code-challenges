"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# This problem wasn't super fun, I just stole the isPrime method I wrote for a previous problem and chucked it in here :/


from math import sqrt


def is_prime(x):
    # Even numbers are never prime (except for 2)
    if x % 2 == 0 and x != 2:
        return False

    for i in range(int(sqrt(x)), 1, -1):
        if x % i == 0:
            return False
    return True


def nth_prime(n):
    prime_count = 1
    prime_candidate = 3
    while prime_count < n:
        if is_prime(prime_candidate):
            prime_count += 1
        prime_candidate += 2
    return prime_candidate - 2


print(nth_prime(10001))