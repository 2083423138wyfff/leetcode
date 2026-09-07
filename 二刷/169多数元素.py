import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    hash={}
    for i in range(len(nums)):
        hash[nums[i]]=hash.get(nums[i],0)+1
        if hash[nums[i]]>(len(nums)/2):
            return nums[i]
    
print(abc(nums))