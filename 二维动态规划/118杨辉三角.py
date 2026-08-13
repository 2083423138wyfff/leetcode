import sys

n=int(sys.stdin.readline())
def abc(n):
    if n==0:
        return []
    dp=[[]for _ in range(n)]
    dp[0]=[1]
    for i in range(1,n):
        cur=[1]
        for j in range(len(dp[i-1])-1):
            cur.append(dp[i-1][j]+dp[i-1][j+1])
        cur.append(dp[i-1][-1])
        dp[i]=cur
    return dp
print(abc(n))