class Solution:
    def abc(self,haystack,needle):
        #主串每个位置当起点，逐个字符检查
        n,m=len(haystack),len(needle)
        if m==0:
            return 0#needle字符串不存在时
        if n<m:
            return -1
        else:
            for i in range(n-m+1):#共有n-m种可能
                j=0
                while j<m and haystack[i+j]==needle[j]:
                    j+=1
                if j==m:
                    return i
        return -1
    
    def abcd(self,haystack,needle):
        #KMP:



if __name__=="__main__":
    import sys
    solution=Solution()
    haystack=sys.stdin.readline().split()
    needle=sys.stdin.readline().split()
    print(solution.abc(haystack,needle))