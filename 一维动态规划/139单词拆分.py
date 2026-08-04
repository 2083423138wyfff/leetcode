import sys
s=sys.stdin.readline().strip()
wordDict=sys.stdin.readline().split()

def abc(s,wordDict):
    word_set=set(wordDict)
    dp=[False]*(len(s)+1)#为什么要加1,因为dp[i]定义为在第i个字符后面切割，能不能被拆分。dp[0]为空字符
    dp[0]=True
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i]=True
                break
    return dp[len(s)]

print(abc(s,wordDict))