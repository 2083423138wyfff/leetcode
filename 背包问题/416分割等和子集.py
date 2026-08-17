import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    if sum(nums)%2!=0:
        return False
    dp=[False]*(sum(nums)//2+1)
    dp[0]=True
    for num in nums:
        for i in range(sum(nums)//2,num-1,-1):
            if i-num>=0:
                dp[i]=dp[i] or dp[i-num]
    return dp[-1]
print(abc(nums))