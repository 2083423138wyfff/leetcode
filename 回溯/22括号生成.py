# import sys

# n = int(sys.stdin.readline())

# def abc(n):
#     res = []

#     def backtrack(path, left, right):
#         if len(path) == 2 * n:
#             res.append(path)
#             return

#         if left < n:
#             backtrack(path + "(", left + 1, right)

#         if right < left:
#             backtrack(path + ")", left, right + 1)

#     backtrack("", 0, 0)
#     return res

# print(abc(n))
import sys
n = int(sys.stdin.readline())
def abc(n):
    res=[]
    def backtrack(path,left,right):
        if len(path)==2*n:
            res.append(path)
            return
        if left<n:
            backtrack(path+'(',left+1,right)
        if right<left:
            backtrack(path+')',left,right+1)
    backtrack('',0,0)
    return res
print(abc(n))
