"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# This computation actually took a pretty long time compared to the previous questions
# It would be fun to come back to this one and attempt to optimize a bit

def smallest_multiple(n):
    smallest_num = -1
    accumulator = n
    while smallest_num == -1:
        divisible_by_all = True
        for i in range(1, n):
            if accumulator % i != 0:
                divisible_by_all = False
        if divisible_by_all == True:
            smallest_num = accumulator 
        accumulator += n
    return smallest_num


print(smallest_multiple(20))