class Solution:
    def abc(self,nums):
        if nums[0]==nums[1]:
            return 'YES'
        if abs(nums[0]-nums[1])%3==0:
            return 'YES'
        else:
            return 'NO'
if __name__=="__main__":
    import sys
    t=int(sys.stdin.readline().strip())
    solution=Solution()
    for _ in range(t):
        nums=list(map(int,sys.stdin.readline().split()))
        print(solution.abc(nums))
