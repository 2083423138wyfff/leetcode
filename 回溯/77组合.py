
# import sys
# n=int(sys.stdin.readline().spilt())
# k=int(sys.stdin.readline().spilt())
# def abc(n,k):
#     res=[]
#     path=[]
#     def backtrack(start):
#         if len(path)==k:
#             res.append(path[:])
#             return
#         for i in range(start,n+1):
#             path.append(i)
#             backtrack(i+1)
#             path.pop()
#     backtrack(1)
#     return res
import sys
n=int(sys.stdin.readline())#如果只有一个数，不能在后面加split()
k=int(sys.stdin.readline())
def abc(n,k):
    res=[]
    path=[]
    
    def backtrack(start):
        if len(path)==k:
            res.append(path[:])
            return
        for i in range(start,n+1):
            path.append(i)
            backtrack(i+1)
            path.pop()
    backtrack(1)
    return res

print(abc(n,k))
