"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Helpful math stuff

Any positive integer can be expressed as a factor of 2 integers.
That is to say for n = x * y, we can get any n by selecting the right x and y.
Furthermore, we know that 1 <= x <= n and 1 <= y <= n. Neither factor can exceed the product, or dip below 1.
Likewise, 1 factor must be less than or equal to the other. Let's call the smaller one x: x <= y.
Let's assume that x > sqrt(n).
Because y > x, it follows that y > sqrt(n)
If we proceed to multiply x and y, we end up with the following contradiction:
x * y > sqrt(n) * sqrt(n)
or, simplified
x * y > n
this statement is a contradiction because we know that x * y is precisely n.
Therefore the initial assumption (that x > sqrt(n)) is necessarily false.
That means that for any positive composite number, there exists a factor x such that x <= sqrt(n)


We know that for any composite number (n) there must exist a factor (x) such that x <= sqrt(n).
x is either prime or composite. If x is prime, it happens to be the largest prime factor.
More likely, the largest prime factor will be < x. 
In Either case, the largest prime factor is < sqrt(n), or n itself is prime.
"""


from math import sqrt
import time

def is_prime(x):
    # Even numbers are never prime (except for 2)
    if x % 2 == 0 and x != 2:
        return False

    for i in range(int(sqrt(x)), 1, -1):
        if x % i == 0:
            return False
    return True

def largest_prime_factor(n):
    for i in range(int(sqrt(n)), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return n

print(largest_prime_factor(600851475143))