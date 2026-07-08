import sys
n=int(sys.stdin.readline())
# def abc(n):
#     if n==0 or n==1:
#         return n
#     else:
#         pre1=0
#         pre2=1
#         for i in range(2,n+1):
#             res=pre1+pre2
#             pre1,pre2=pre2,res
#         return res

#练习递归
def abc(n):
    if n<=1:
        return n
    else:
        return abc(n-1)+abc(n-2)
print(abc(n))