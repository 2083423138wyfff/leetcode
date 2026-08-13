import sys
word1=sys.stdin.readline().strip()
word2=sys.stdin.readline().strip()

def abc(word1,word2):
    #dp[i][j]定义为word1前i个字符和word2前j个字符，的最长公共子序列长度
    dp=[[0]*(len(word2)+1)for _ in range(len(word1)+1)]
    for row in range(len(word1)+1):
        dp[row][0]=0
    for col in range(len(word2)+1):
        dp[0][col]=0
    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

print(abc(word1,word2))
    