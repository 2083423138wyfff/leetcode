class Solution:
    def abc(self,nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                if left<right and nums[left]+nums[right]+nums[i]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif left<right and nums[left]+nums[right]+nums[i]>0:
                    right-=1
                elif left<right and nums[left]+nums[right]+nums[i]<0:
                    left+=1
        return ans

                


                

if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums))