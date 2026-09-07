import sys
nums=list(map(int,sys.stdin.readline().split()))
target=int(sys.stdin.readline().strip())
def abc(nums,target):
    hash={}
    for i in range(len(nums)):
        if nums[i] not in hash:
            hash[nums[i]]=i
        if target-nums[i] in hash and hash[target-nums[i]]!=i:
            return [i,hash[target-nums[i]]]
    return -1
print(abc(nums,target))