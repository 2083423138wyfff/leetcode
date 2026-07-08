import sys
nums = list(map(int, sys.stdin.readline().split()))
def _123(nums):
    jumps=0
    current_end=0
    farthest=0
    for i in range(len(nums)-1):
        farthest=max(farthest,i+nums[i])
        if i == current_end:
            jumps+=1
            current_end=farthest
    return jumps

print(_123(nums))