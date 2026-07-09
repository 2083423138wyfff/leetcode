#炒鸡回文构造
class Solution:
    def abc(self,nums):
        i=n=nums[0]
        j=i+1
        m=nums[1]
        for a in range(m):
            for b in range(m):
                if         
if __name__=="__main__":
    import sys
    n=int(sys.stdin.readline().strip())
    solution=Solution()
    for _ in range(n):
        nums=list(map(int,sys.stdin.readline().split()))
        print(solution.abc(nums))