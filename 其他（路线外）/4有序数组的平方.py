class Solution:
    def abc(self,nums):
        left=0
        right=len(nums)-1
        pos=len(nums)-1
        ans=[0 for _ in range(len(nums))]
        while left<=right:
            if nums[right]**2>=nums[left]**2:
                ans[pos]=nums[right]**2
                right-=1
                pos-=1
            else:
                ans[pos]=nums[left]**2
                left+=1
                pos-=1
        return ans



            

                


                

if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums))