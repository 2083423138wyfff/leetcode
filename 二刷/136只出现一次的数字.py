import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    res=0
    for i in range(len(nums)):
        res=res^nums[i]
    return res 
print(abc(nums))