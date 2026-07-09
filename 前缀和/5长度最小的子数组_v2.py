class Solution:

    def minSubArrayLen(self,target,nums):
        n = len(nums)
        left = 0
        cur_sum = 0          # ← 用变量维护，绝不切片
        min_len = float('inf')
    
        for right in range(n):      # ← 右指针逐个走，不会越界
            cur_sum += nums[right]
        
            while cur_sum >= target:  # ← 满足就收缩，不满足就继续扩
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
    
        return 0 if min_len == float('inf') else min_len  # ← 找不到返回 0     



if __name__ == "__main__":
    import sys
    solution=Solution()
    target=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    print(solution.minSubArrayLen(target,nums))