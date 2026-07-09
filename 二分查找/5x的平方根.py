'''
二分查找
核心是找一个最大的ans，使得ans**2<=x，且（ans+1）**2>x
左边界0，有边界x//2+1
'''


class Solution:
    def abc(self, x: int) -> int:
        left=0
        right=x//2+1
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        
                
                
    
if __name__=='__main__':
    import sys
    solution=Solution()
    x=int(sys.stdin.readline().strip())
    print(solution.abc(x))