class Solution:
    def SlidingWindow(self,s):
        #用字典记录出现过的字符及其位置
        left=0
        ans=0
        char_index={}
        for right in range(len(s)):
            if s[right] in char_index:
                left=max(left,char_index[s[right]])+1
            char_index[s[right]]=right
            ans=max(ans,right-left+1)
        return ans if s else -1

            
if __name__=="__main__":
    import sys
    s=sys.stdin.readline().strip()
    solution=Solution()
    print(solution.abc(s))
