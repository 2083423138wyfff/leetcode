import sys
s=list(sys.stdin.readline().strip())
def abc(s):
    res=[]
    left=0
    right=0
    dicts={}
    for i,ch in enumerate(s):
        dicts[ch]=i
    for i in range(len(s)):
        right=max(right,dicts[s[i]])
        if i==right:
            res.append(i-left+1)
            left=i+1
    return res
print(abc(s))