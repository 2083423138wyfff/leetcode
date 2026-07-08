import sys
nums = list(map(int, sys.stdin.readline().split()))
def _123(nums):
    pre=0
    for i in range(len(nums)):
        if pre >=i:
            pre=max(pre,i+nums[i])
    if pre>=len(nums)-1:
        return True
    else:
        return False
    
print(_123(nums))