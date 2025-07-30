from math import factorial


def get_nth_permutation(num_set: list[int], n: int = 1000000) -> str:
    n = n - 1
    needed_digits = len(num_set)
    nth_permutation: list[str] = []
    while len(nth_permutation) < needed_digits:
        branch_permutations = factorial(len(num_set) - 1)
        for branch, val in enumerate(num_set):
            min_index = branch_permutations * branch
            max_index = min_index + branch_permutations - 1
            if n >= min_index and n <= max_index:
                nth_permutation.append(f"{val}")
                num_set.pop(branch)
                n -= min_index
                break
    return "".join(nth_permutation)


def solve() -> str:
    return get_nth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)


if __name__ == "__main__":
    print(solve())
