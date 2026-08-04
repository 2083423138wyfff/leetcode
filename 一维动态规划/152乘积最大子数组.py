import sys
nums=list(map(int,sys.stdin.readline().split()))

def abc(nums):
    max_dp=[float('-inf') for _ in range(len(nums))]
    min_dp=[float('inf') for _ in range(len(nums))]
    max_dp[0],min_dp[0]=nums[0],nums[0]
    for i in range(1,len(nums)):
        max_dp[i]=max(nums[i],max_dp[i-1]*nums[i],min_dp[i-1]*nums[i])
        min_dp[i]=min(nums[i],max_dp[i-1]*nums[i],min_dp[i-1]*nums[i])
    return max(max_dp)

print(abc(nums))