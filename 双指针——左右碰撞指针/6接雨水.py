class Solution:
    def abc(self,nums):
        sumwater=0
        left,right=0,len(nums)-1
        maxleft=nums[0]
        maxright=nums[len(nums)-1]
        while left<right:
            if maxleft<=maxright:
                left+=1
                sumwater+=max(maxleft-nums[left],0)
                maxleft=max(maxleft,nums[left])
            else:
                right-=1
                sumwater+=max(maxright-nums[right],0)
                maxright=max(maxright,nums[right])
        return sumwater
if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums))