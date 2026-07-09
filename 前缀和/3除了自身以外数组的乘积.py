#answer[i] = （i 左边所有元素的乘积）×（i 右边所有元素的乘积）
class Solution:
    def abc(self,nums):
        hash={}
        cur=1
        ans=[1 for _ in range(len(nums))]
        right=[1 for _ in range(len(nums))]
        left=[1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i]=left[i]*right[i]
        return ans if nums else []
            
if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums))