class Solution:
    def abc(self,nums:list[int],target:int)-> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                return middle
            else:
                right = middle
        if target>nums[middle]:
            return middle+1
        else:
            return middle
if __name__=='__main__':
    import sys
    solution=Solution()
    target=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(target,nums))