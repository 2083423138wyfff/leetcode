class Solution:
    #暴力求解，求出所有连续子数组的和
    def maxSubArray(self,nums):
        ans=float('-inf')
        for i in range(1,len(nums)+1):
                for j in range(i):
                    ans=max(ans,sum(nums[j:i]))
        return ans if nums else -1              



if __name__ == "__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.maxSubArray(nums))