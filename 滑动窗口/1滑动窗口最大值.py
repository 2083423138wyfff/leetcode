class Solution:
    def abc(self,k,nums):
        for i in range(len(nums)-k+1):
            print(max(nums[i:i+k]))
    #滑动窗口解法
    def SlidingWindow(self,k,nums):
        if not nums or k ==0 :
            return []
        from collections import deque
        q=deque()
        ans=[]
        for i,num in enumerate(nums):
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(i)
            if q[0]<=i-k:
                q.popleft()
            if i >= k-1:
                ans.append(nums[q[0]])

        return ans

            
if __name__=="__main__":
    import sys
    nums=list(map(int,sys.stdin.readline().split()))
    k=int(sys.stdin.readline().strip())
    solution=Solution()
    print(solution.abc(k,nums))
