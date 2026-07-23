import sys

nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    max_ans=float('-inf')
    dp=[0 for _ in range(len(nums))]
    dp[0]=nums[0]
    for i in range(1,len(nums)):
        dp[i]=max(nums[i],dp[i-1]+nums[i])
    return max(dp)
print(abc(nums))