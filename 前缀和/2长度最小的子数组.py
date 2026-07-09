
class Solution:
    def abc(self,nums,target):
        left=0
        min_len=float('inf')

        cur=0
        for right in range(len(nums)):
            cur+=nums[right]
            while cur>=target:

                min_len=min(min_len,right-left+1)
                cur-=nums[left]
                left+=1
        return min_len if min_len !=float('inf') else 0
if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    target=int(sys.stdin.readline())
    print(solution.abc(nums,target))