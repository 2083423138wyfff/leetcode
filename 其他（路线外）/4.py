def abc(s):
    left=0
    window={}
    max_len=float('-inf')
    start=0
    if len(s)==0 or len(s)==1:
        return len(s),s
    for right in range(len(s)):
        window[s[right]]=window.get(s[right],0)+1
        while window[s[right]] >1:
            window[s[left]]-=1
            left+=1
            if max_len<right-left+1:
                max_len=right-left+1
                start=left

    return max_len,s[start:start+max_len] if s else -1