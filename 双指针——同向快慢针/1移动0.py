class Solution:
    def abc(self,nums):
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for j in range(pos+1,len(nums)):
                nums[j]=0

        return nums if nums else -1
if __name__=="__main__":
    import sys
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(nums))