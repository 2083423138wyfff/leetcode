
class Solution:
    def minWindow(self, target: int, nums):
        window=0
        left=0
        min_len=float('inf')
        for right in range(len(nums)):
            window+=nums[right]
            while window>=target:
                min_len=min(min_len,right-left+1)
                window-=nums[left]
                left+=1
        return min_len if min_len!=float('inf') else 0




            
if __name__=="__main__":
    import sys
    target=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(target,nums))
