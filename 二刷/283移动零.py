import sys
nums=list(map(int,sys.stdin.readline().split()))
val=int(sys.stdin.readline().strip())
def abc(nums):
    slow=0
    if not nums:
        return []
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1
    for i in range(slow,len(nums)):
        nums[i]=0
    return nums
# print(abc(nums))
def abc1(nums,val):
    slow=0
    if not nums:
        return 0
    for fast in range(len(nums)):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            slow+=1
    return slow
# print(abc1(nums,val))

def abc2(nums):
    res=[]
    if not nums:
        return -1
    res.append(nums[0])
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1] and i<len(nums):
            continue
        res.append(nums[i])
    return res
# print(abc2(nums))

def abc3(nums):
    slow=0
    for fast in range(len(nums)):
        if nums[fast]>=0:
            slow+=1
        else:
            nums[fast],nums[slow]=nums[slow],nums[fast]
        