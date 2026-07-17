#炒鸡回文构造
class Solution:
    def abc(self,nums):
        if nums //2==0:
            return False
        else:
            return True

        
if __name__=="__main__":
    import sys
    n=int(sys.stdin.readline().strip())
    solution=Solution()
    for _ in range(n):
        nums=list(map(int,sys.stdin.readline().split()))
        print(solution.abc(nums))