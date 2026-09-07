import sys
s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()
def abc(s,t):
    if not t or len(t)>len(s):
        return ''
    need={}
    for i in t:
        need[ord(i)-ord('a')]=need.get(ord(i)-ord('a'),0)+1
    valid_t=len(need)
    valid_s=0
    window={}
    left=0
    leng=float('inf')
    res=''
    for right in range(len(s)):
        window[ord(s[right])-ord('a')]=window.get(ord(s[right])-ord('a'),0)+1
        if ord(s[right])-ord('a') in need and window[ord(s[right])-ord('a')]==need[ord(s[right])-ord('a')]:
            valid_s+=1
        while valid_s==valid_t:
            start=left
            if right-start+1<leng:
                leng=right-start+1
                res=s[start:right+1]
            window[ord(s[left])-ord('a')]=window.get(ord(s[left])-ord('a'))-1
            if ord(s[left])-ord('a') in need and window[ord(s[left])-ord('a')]<need[ord(s[left])-ord('a')]:
                valid_s-=1
            left+=1
    return res
print(abc(s,t))