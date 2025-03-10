"""
1. calculate factorial
2. sum digits of result
"""

def factorial(n):
    ans = 1
    for i in range(2, n):
        ans *= i
    return ans

if __name__ == '__main__':
    digit_sum = 0
    n_factorial = factorial(100)
    while n_factorial > 0:
        digit_sum += n_factorial % 10
        n_factorial = n_factorial // 10
    print(digit_sum)