class Solution:
    def _123(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return [i,j]
        return -1



if __name__ == "__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    target=int(sys.stdin.readline().strip())
    print(solution._123(nums,target))