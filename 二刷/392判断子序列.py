import sys
s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()
def abc(s,t):
    if len(s)>len(t):
        return False
    if len(s)==0:
        return True
    i=0
    j=0
    while j<len(t):
        if i<len(s) and s[i]==t[j]:
            i+=1
        j+=1
    if i==len(s):
        return True
    return False
print(abc(s,t))