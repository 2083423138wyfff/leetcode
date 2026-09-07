from collections import deque
import sys

nums=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline().strip())

def abc(nums,k):
    queue=deque()#存下标
    res=[]
    for i,num in enumerate(nums):
        while queue and nums[queue[-1]]<num:
            queue.pop()
        queue.append(i)
        if i-queue[0]>=k:
            queue.popleft()
        if i>=k-1:
            res.append(nums[queue[0]])
    return res
print(abc(nums,k))