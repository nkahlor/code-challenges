"""
I've done a version of this with dynamic programming before, but we can also do it like this.

One way to think about it, is that every path from origin to destination can be encoded
as a string of right moves (R) and down moves (D). Therefore, the problem reduces to
'find the number of combinations of R and D strings possible to move from origin to destination'

Recall, our grid is m x n

How long can our string be?
    - it must be m steps down to land at the origin
    - it must be n steps right to land at origin
Therefore, string length must be m + n

Now we're cooking with gas! We're really just asking: 
    - How combinations of down (m) moves are present in the total moves?
    or
    - How combinations of right (n) moves are present in the total moves?

Essentially, just take the smaller of the 2 for speed of the comb calculation!
"""

from math import comb
m = 20
n = 20
print(comb(m + n, min(m, n)))