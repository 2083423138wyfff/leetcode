class Solution:
    def abc(self,s,p):
        need=[0]*26
        for c in p:
            need[ord(c)-ord('a')]+=1 
        window=[0]*26
        ans=[]
        for right in range(len(s)):
            window[ord(s[right])-ord('a')]+=1
            if right>= len(p):
                window[ord(s[right-len(p)])-ord("a")]-=1
            if right>=len(p)-1 and window==need:
                ans.append(right-len(p)+1)
        return ans
                

            
if __name__=="__main__":
    import sys
    s=sys.stdin.readline().strip()
    p=sys.stdin.readline().strip()
    solution=Solution()
    print(solution.abc(s,p))
