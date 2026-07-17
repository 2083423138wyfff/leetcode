import sys
nums = list(map(int, sys.stdin.readline().split()))

def abc(nums):
    res = []
    path = []
    
    def backtrack(start):
        res.append(path[:])
        #这题没什么边界条件，所以不需要if
        #因为空集也包含，所以可以直接加
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            
    backtrack(0)
    return res

print(abc(nums))
