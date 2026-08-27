import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    res=float('-inf')
    left=0
    right=len(nums)-1
    while left<right:
        res=max(res,min(nums[left],nums[right])*(right-left))
        if nums[left]<=nums[right]:
            left+=1
        else:
            right-=1
    return res
#print(abc(nums))

#42接雨水
def abc1(nums):
    res=0
    left=0
    right=len(nums)-1
    max_left=nums[left]
    max_right=nums[right]
    while left<right:
        if nums[left]<=nums[right]:
            res+=max_left-nums[left]
            left+=1
            max_left=max(max_left,nums[left])
        else:
            res+=max_right-nums[right]
            right-=1
            max_right=max(max_right,nums[right])
    return res
print(abc1(nums))