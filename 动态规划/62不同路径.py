import sys
m, n = map(int, sys.stdin.readline().split())


def abc(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0 or n == 0:
        return 1
    return abc(m - 1, n) + abc(m, n - 1)


print(abc(m - 1, n - 1))
