from collections import deque
import sys
s=sys.stdin.readline().strip()
p=sys.stdin.readline().strip()
def jishu(s):
    count=[0]*26
    for i in s:
        count[ord(i)-ord('a')]+=1
    return count
def abc(s,p):
    res=[]
    if not s or not p or len(p)>len(s):
        return -1
    count=[0]*26
    for i in p:
        count[ord(i)-ord('a')]+=1
    k=len(p)
    for i in range(len(s)-k+1):
        if list(jishu(s[i:i+k]))==count:
            res.append(i)
    return res

def abcd(s,p):
    res=[]
    k=len(p)
    if k>len(s):
        return res
    count=jishu(p)
    window=[0]*26
    for i in range(len(s)):
        window[ord(s[i])-ord('a')]+=1
        if i>=k:#因为每次只增加一个，所以到后面每次减一个就行，不会减错
            window[ord(s[i-k])-ord('a')]-=1
        if i>=k-1 and window==count:
            res.append(i-k+1)
    return res  
    
print(abcd(s,p))