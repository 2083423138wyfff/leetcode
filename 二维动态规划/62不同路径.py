import sys
m,n=map(int,sys.stdin.readline().split())
def abc(m,n):
    if m<0 or n<0:
        return 0
    if m==0 or n==0:
        return 1
    return abc(m-1,n)+abc(m,n-1)

def abcd(m,n):
    dp=[[1]*n for _ in range(m)]
    for row in range(1,m):
        for col in range(1,n):
            dp[row][col]=dp[row-1][col]+dp[row][col-1]
    return dp[m-1][n-1]
print(abcd(m,n))