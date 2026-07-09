class Solution:
    def abc(self,nums):
        left=0
        right=len(nums)-1
        maxArea=max(0,(right-left)*min(nums[right],nums[left]))
        while left<right:
            if nums[left]<=nums[right]:
                left+=1
                maxArea=max(maxArea,(right-left)*min(nums[right],nums[left]))
            else:
                right-=1
                maxArea=max(maxArea,(right-left)*min(nums[right],nums[left]))
        return maxArea if nums else -1



            

                


                

if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums))