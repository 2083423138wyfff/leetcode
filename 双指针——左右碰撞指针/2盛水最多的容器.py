class Solution:
    def maxArea(self,nums):
        left=0
        right=len(nums)-1
        ans=0
        pre=(right-left)*min(nums[left],nums[right])
        ans=max(ans,pre)
        while left<=right:#因为是先移动，再计算，所以不能等于
            if nums[left]<=nums[right]:
                left+=1
                ans=max(ans,(right-left)*min(nums[left],nums[right]))
            else:
                right-=1
                ans=max(ans,(right-left)*min(nums[left],nums[right]))
        return ans if nums else -1        



if __name__ == "__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.maxArea(nums))