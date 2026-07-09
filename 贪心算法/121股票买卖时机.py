import sys
nums = list(map(int, sys.stdin.readline().split()))
def _123(nums):
    min_num=float('inf')
    res=0
    for i in range(len(nums)):
        min_num=min(min_num,nums[i])
        res=max(res,nums[i]-min_num)
    return res
print(_123(nums))