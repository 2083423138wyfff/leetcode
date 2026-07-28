import sys
n=int(sys.stdin.readline())
#递归法
def abc(n):
    if n<0:
        return -1
    if 0<=n<=1:
        return n
    return abc(n-1)+abc(n-2)
#动态规划
def abcd(n):
    if n<0:
        return -1
    if 0<=n<=1:
        return n
    pre=0
    cur=1
    ans=0
    for _ in range(2,n+1):
        ans=pre+cur
        pre=cur
        cur=ans
    return ans

print(abcd(n))