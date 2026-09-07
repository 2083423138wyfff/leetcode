import sys
nums=set(map(int,sys.stdin.readline().split()))
def abc(nums):
    res=float('inf')
    for num in nums:
        if num>0:
            res=min(res,num)
    if res!=1:
        return 1
    else:
        while res+1 in nums:
            res=res+1
        return res+1
    
print(abc(nums))