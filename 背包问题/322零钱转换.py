import sys
coins=list(map(int,sys.stdin.readline().split()))
amount=int(sys.stdin.readline().strip())
def abc(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if i>=coin:
                dp[i]=min(dp[i-coin]+1,dp[i])
    return dp[-1] if dp[-1]!=float('inf') else -1
print(abc(coins,amount))