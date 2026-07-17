class Solution:
    def abc(self,nums,val):
        pos=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pos]=nums[i]
                pos+=1

        return pos if nums else -1
if __name__=="__main__":
    import sys
    val=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(nums,val))