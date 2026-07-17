class Solution:
    def abc(self,nums):
        pos=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[pos]=nums[i]
                pos+=1

        return nums[:pos] if nums else -1
if __name__=="__main__":
    import sys
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(nums))