import sys
s=list(sys.stdin.readline().strip())
# k=int(sys.stdin.readline().strip())
def abc(s):
    if len(s)==0:
        return s
    left=0
    right=len(s)-1
    while left<=right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return ''.join(s)
# print(abc(s))
#541
def abc1(s,k):
    for i in range(0,len(s),2*k):
        left=i
        right=min(i+k-1,len(s)-1)
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
    return ''.join(s)
# print(abc1(s,k))
#557
# s=sys.stdin.readline().split()
def abc2(s):
    res=[]
    for s1 in s:
        res.append(abc(list(s1)))
    return ' '.join(res)
# print(abc2(s))
#345
def abc3(s):
    l=list('aeiouAEIOU')
    left=0
    right=len(s)-1
    while left<=right:
        while left<right and s[left] not in l :
            left+=1
        while left<right and s[right] not in l :
            right-=1
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return ''.join(s)
print(abc3(s))