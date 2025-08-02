def solve() -> int:
    target = 200
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]

    cache: dict[tuple[int, int], int] = {}

    def dfs(target: int, i: int) -> int:
        if target == 0:
            return 1
        if target < 0 or i >= len(denominations):
            return 0

        if (i, target) in cache:
            return cache[(i, target)]

        ways_with_coin = dfs(target - denominations[i], i)
        ways_without_coin = dfs(target, i + 1)
        result = ways_with_coin + ways_without_coin
        cache[(i, target)] = ways_with_coin + ways_without_coin
        return result

    return dfs(target, 0)


if __name__ == "__main__":
    print(solve())
