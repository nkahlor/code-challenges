"""
Problem: What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

Solution:

I may have made this a little more convoluted than it needed to be, but I'm a little proud of my solution. 

I observed that the problem can be reduced in to simply the horizontal product question, if you can organize the matrix accordingly.

Given the following matrix:
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16

I can compute the largest horizontal product of group size n by simply scanning all groups of n in each row, and keeping track of the largest product I see.

If I want to find the largest vertical product, I could write a new algorithm to scan through the matrix in a different way, or I can just rotate the matrix and 
re-use the algorithm I already wrote!
i.e, turn the matrix into this:
01 05 09 13
02 06 10 14
03 07 11 15
04 08 12 16
and feed it into the horizontal product finder :)

In fact, we can re-shuffle the data diagonally to process the same logic in the same way!

I thought this was a neat way to solve the problem, regardless off its inefficiencies.
"""

from functools import reduce

grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
n = 4


def string_grid_to_matrix(grid):
    return [[int(val) for val in row.split(" ")] for row in grid.split("\n")]


def rotate_grid(grid):
    return [list(tup) for tup in list(zip(*grid))]


def tilt_grid_right(grid, n):
    tilted_grid = []
    num_of_diagonals = len(grid[0]) - n
    for start_row in range(0, len(grid) - 1):
        for offset in range(num_of_diagonals):
            right_diagonal = [
                row[i + offset] for i, row in enumerate(grid[start_row:]) if i < n
            ]
            tilted_grid.append(right_diagonal)
    return tilted_grid


def tilt_grid_left(grid, n):
    tilted_grid = []
    num_of_diagonals = len(grid[0]) - n
    for start_row in range(len(grid) - 1):
        for offset in range(n - 1, num_of_diagonals + 1):
            right_diagonal = [
                row[-(i + offset)] for i, row in enumerate(grid[start_row:]) if i < n
            ]
            tilted_grid.append(right_diagonal)
    return tilted_grid


def largest_horizontal_product_in_grid(grid, n):
    max_product = -1
    for row in grid:
        for index in range(0, len(row), n):
            h_window = row[index : index + n]
            h_product = reduce(lambda x, y: x * y, h_window, 1)
            if h_product > max_product:
                max_product = h_product
    return max_product


def largest_vertical_product_in_grid(grid, n):
    rotated_grid = rotate_grid(grid)
    return largest_horizontal_product_in_grid(rotated_grid, n)


def largest_right_diag_product_in_grid(grid, n):
    rotated_grid = tilt_grid_right(grid, n)
    return largest_horizontal_product_in_grid(rotated_grid, n)


def largest_left_diag_product_in_grid(grid, n):
    rotated_grid = tilt_grid_left(grid, n)
    return largest_horizontal_product_in_grid(rotated_grid, n)


grid = string_grid_to_matrix(grid)
h_max = largest_horizontal_product_in_grid(grid, n)
v_max = largest_vertical_product_in_grid(grid, n)
r_diag_max = largest_right_diag_product_in_grid(grid, n)
l_diag_max = largest_left_diag_product_in_grid(grid, n)

print(max(h_max, v_max, r_diag_max, l_diag_max))