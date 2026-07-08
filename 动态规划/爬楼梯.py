class Solution:
    def _123(self, num):
        #dp[i]表示和为i的最小完全平方数的数量
        dp=[float('inf')]*(num+1)
        dp[0]=0
        for i in range(1,num+1):
            j=1
            while j**2<=i:
                dp[i]=min(dp[i],dp[i-j**2]+1)
                j+=1
        return dp[num] if num>0 else 0

if __name__ =="__main__":
    Solution=Solution()
    num=int(input())
    print(Solution._123(num))
