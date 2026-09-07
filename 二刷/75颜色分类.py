import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    left=0
    mid=0
    right=len(nums)-1
    while mid<=right:
        if nums[mid]==0:
            nums[mid],nums[left]=nums[left],nums[mid]
            mid+=1
            left+=1
        elif nums[mid]==2:
            nums[mid],nums[right]=nums[right],nums[mid]
            right-=1
        else:
            mid+=1
    return nums
print(abc(nums))