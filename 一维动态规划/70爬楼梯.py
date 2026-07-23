import sys
n=int(sys.stdin.readline().strip())
def abc(n):
    if n<=0:
        return -1
    if 0<n<=2:
        return n
    return abc(n-1)+abc(n-2)

def abcd(n):
    if n<=0:
        return -1
    if 0<n<=2:
        return n
    pre=1
    cur=2
    ans=0
    for _ in range(3,n+1):
        ans=pre+cur
        pre=cur
        cur=ans
    return ans

print(abc(n))
print(abcd(n))