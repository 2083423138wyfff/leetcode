class Solution:
    #暴力求解
    def longestCommonPrefix(self,s):
        #当前字符大家都有，就继续往前；没有就返回上一次的值
        ans=''
        if not s:     # 或 if len(s) == 0
            return ""
        for i in range(len(s[0])):
            ch=s[0][i]
            for j in range(1,len(s)):
                #必须先计算长度
                if len(s[j])<=i or s[j][i]!=ch :
                    return s[0][:i]
        return s[0] if s else -1              



if __name__ == "__main__":
    import sys
    solution=Solution()
    s=list(map(str,sys.stdin.readline().split()))
    print(solution.longestCommonPrefix(s))