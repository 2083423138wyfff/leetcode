class Solution:
    #暴力解法
    def abc(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

    #哈希表解法，核心在于：对于nums[i]，在哈希表里找有没有target-nums[i]
    def haxi(self,nums,target):
        haxi={}
        for i in range(len(nums)):
            if target-nums[i] not in haxi:
                haxi[nums[i]]=i#要把nums[i]作为key存起来
            else:
                return [haxi[target-nums[i]],i]

if __name__=="__main__":
    import sys
    target=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(nums,target))