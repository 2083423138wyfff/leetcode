import sys
nums=list(map(int,sys.stdin.readline().split()))
target=int(sys.stdin.readline())
def abc(nums,target):
    res=[]
    path=[]
    def backtrack(start):
        if sum(path)==target:
            res.append(path[:])
            return
        if sum(path)>target:
            return
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i)
            path.pop()
    backtrack(0)
    return res
print(abc(nums,target))