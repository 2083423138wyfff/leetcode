class Solution:    
    #哈希表解法
    #先找起点，然后算长度，然后再比对每一个起点的长度
    def hashmap(self,nums):
        hash=set(nums)
        ans=0
        for i in hash:
            if i-1 not in hash:#说明是起点
                current_len=1
                current_num=i
                while current_num +1 in hash:
                    #找当前起点的最长长度
                    current_num+=1
                    current_len+=1
                ans=max(ans,current_len)
        return ans
        
if __name__=="__main__":
    import sys
    nums=list(map(int,sys.stdin.readline().split()))
    solution=Solution()
    print(solution.hashmap(nums))