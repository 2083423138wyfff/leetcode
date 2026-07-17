
class Solution:
    def abc(self, k: int, nums):
        window={}
        for right in range(len(nums)):
            num=nums[right]
            if num not in window:
                window[num]=right
            elif num in window and right-window[num]<=k:
                return True
            elif num in window and right-window[num]>k:
                window[num]=right
        return False




if __name__=="__main__":
    import sys
    k=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.abc(k,nums))
