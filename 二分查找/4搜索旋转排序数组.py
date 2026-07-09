'''
二分查找
1、如果mid直接等于target
2、先去判断哪边有序，再去想怎么二分
3、这题要左闭右闭
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left]<=nums[mid]:#左边有序
                if nums[left]<=target<nums[mid]:#target在左边
                    right=mid-1
                else:
                    left=mid+1
            else:#右边有序
                if nums[mid]<target<=nums[right]:#target在右边
                    left=mid+1
                else:
                    right=mid-1
        return -1
                
                
    
if __name__=='__main__':
    import sys
    solution=Solution()
    target=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.searchRange(nums,target))