"""
This one really stumped me for a while. I identified pretty quick the need for DP, but
it took me forever to realize how to structure it. The commented is my original solution,
but I later looked up a better way to do it and that's the one I have running
by default below.
"""

denominations = [1, 2, 5, 10, 20, 50, 100, 200]

# def solve() -> int:
#     target = 200
#     denominations = [1, 2, 5, 10, 20, 50, 100, 200]

#     cache: dict[tuple[int, int], int] = {}

#     def dfs(target: int, i: int) -> int:
#         if target == 0:
#             return 1
#         if target < 0 or i >= len(denominations):
#             return 0

#         if (i, target) in cache:
#             return cache[(i, target)]

#         ways_with_coin = dfs(target - denominations[i], i)
#         ways_without_coin = dfs(target, i + 1)
#         result = ways_with_coin + ways_without_coin
#         cache[(i, target)] = ways_with_coin + ways_without_coin
#         return result

#     return dfs(target, 0)


def solve() -> int:
    target = 1000
    cache: list[int] = [0] * (target + 1)
    cache[0] = 1
    for coin in denominations:
        for j in range(coin, target + 1):
            cache[j] = cache[j] + cache[j - coin]
    return cache[target]


if __name__ == "__main__":
    print(solve())
