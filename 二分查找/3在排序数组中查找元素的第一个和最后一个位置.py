'''
二分查找
1、分别用二分法找>=target的第一个数（左边界） 和 >target的第一个数（有边界）
2、检测左边界有没有越界（详细见代码）
！！记住二分查找是用nums[mid]来比
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeftBound():
            """找第一个 >= target 的位置（左边界）"""
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid      # target 在左边或就是 mid，收紧右边界
                else:
                    left = mid + 1   # target 在右边
            return left
        
        def findRightBound():
            """找第一个 > target 的位置，再减1（即最后一个 target）"""
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1   # 最后一个 target 在右边，收紧左边界
                else:
                    right = mid      # target 在左边
            return left - 1 #因为原来找的left是>target的第一个，所以需要-1，才是target的最右端
        
        # 空数组直接返回
        if not nums:
            return [-1, -1]
        
        leftBound = findLeftBound()
        
        # 验证 target 是否存在：左边界越界，或左边界处的值不是 target
        if leftBound == len(nums) or nums[leftBound] != target:
            return [-1, -1]
        
        rightBound = findRightBound()
        return [leftBound, rightBound]
    
if __name__=='__main__':
    import sys
    solution=Solution()
    target=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.searchRange(nums,target))