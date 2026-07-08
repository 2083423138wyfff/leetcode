import sys
nums = list(map(int, sys.stdin.readline().split()))
def _123(nums):
    res=0
    for i in range(len(nums)-1):
        res+=max(0,nums[i+1]-nums[i])
    return res
print(_123(nums))