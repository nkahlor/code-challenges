import os
import sys
from typing import Self
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from decorators import time_it

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

class Node:
    def __init__(self, left: Self=None, right: Self=None, val: int=0):
        self.left = left
        self.right = right
        self.val = val

def deserialize_input(in_str: str):
    lines = in_str.splitlines()
    curr_line = []
    prev_line = []
    new_node = None
    for line in reversed(lines):
        for c in line.split(" "):
            new_node = Node(val=int(c))
            curr_line.append(new_node)

        if len(prev_line) > len(curr_line):
            for i, node in enumerate(curr_line):
                    node.left = prev_line[i]
                    node.right = prev_line[i + 1]
                
        prev_line = curr_line
        curr_line = []
    return new_node

@time_it
def max_path_sum(root: Node):

    def dfs(node: Node):
        if node == None:
            return 0
        left_sum = dfs(node.left) + node.val
        right_sum = dfs(node.right) + node.val
        return max(left_sum, right_sum)

    return dfs(root)

if __name__ == '__main__':
    tree = deserialize_input(triangle)
    print(max_path_sum(tree))
