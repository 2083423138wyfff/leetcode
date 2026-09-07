import sys
nums=set(map(int,sys.stdin.readline().split()))
def abc(nums):
    if not nums:
        return 0
    leng=float('-inf')
    for num in nums:
        if num-1 not in nums:
            start=num
            cur=start
            while cur+1 in nums:
                cur+=1
            leng=max(leng,cur-start)
    return leng+1
print(abc(nums))
