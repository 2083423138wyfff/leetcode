import sys
n=int(sys.stdin.readline().strip())
def abc(n):
    dp=[float('inf')]*(n+1)
    dp[0]=0
    nums=[]
    for i in range(1,n+1):
        if i**2<=n: 
            nums.append(i**2)
        for num in nums:
            if i>=num:
                dp[i]=min(dp[i],dp[i-num]+1)
    return dp[-1]
print(abc(n))
    