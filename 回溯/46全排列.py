
# import sys

# nums=list(map(int,sys.stdin.readline().split()))

# class Solution:
#     def abc(self,nums):
#         res=[]
#         path=[]
#         used=[False]*len(nums)
#         def backtrack():
#             if len(path)==len(nums):
#                 res.append(path[:])
#                 return
            
#             for i in range(len(nums)):
#                 if used[i]:
#                     continue
#                 used[i]=True
#                 path.append(nums[i])
#                 backtrack()
#                 path.pop()
#                 used[i]=False
#         backtrack()
#         return res

# solution=Solution()
# print(solution.abc(nums))
import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    res=[]
    path=[]
    used=[False]*len(nums)
    def backtrack():
        if len(nums)==len(path):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i]=False
    backtrack()
    return res
print(abc(nums))
    