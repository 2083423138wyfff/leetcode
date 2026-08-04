import sys
nums=list(map(int,sys.stdin.readline().split()))
#dp[i]定义为以第i个num结尾的最长递增子序列
def abc(nums):
    dp=[1 for _ in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(abc(nums))