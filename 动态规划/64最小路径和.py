import sys
m, n = map(int, sys.stdin.readline().split())


def duqu(line, n):
    if ' ' in line:
        return list(map(int, line.split()))[:n]
    else:
        return list(map(int, line.strip()))[:n]


grid = []
for _ in range(m):
    line = sys.stdin.readline()
    grid.append(duqu(line, n))


def abc(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for row in range(1, m):
        dp[row][0] = dp[row - 1][0] + grid[row][0]
    for col in range(1, n):
        dp[0][col] = dp[0][col - 1] + grid[0][col]
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
    return dp[m - 1][n - 1]


print(abc(grid))
