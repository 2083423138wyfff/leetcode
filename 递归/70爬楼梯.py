import sys
n=int(sys.stdin.readline())

#练习递归
def abc(n):
    if n<=1:
        return n
    elif n==2:
        return 2
    else:
        return abc(n-1)+abc(n-2)
print(abc(n))