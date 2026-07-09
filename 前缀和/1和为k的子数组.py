#考虑用前序和+哈希表
class Solution:
    def abc(self,nums,k):
        hash={0:1}#空数组和为0，有一个
        sum=0
        ans=0
        for num in nums:
            sum+=num
            ans+=hash.get(sum-k,0)
            hash[sum]=hash.get(sum,0)+1
        return ans if nums else -1
if __name__=="__main__":
    import sys
    solution=Solution()
    nums=list(map(int,sys.stdin.readline().split()))
    k=int(sys.stdin.readline())
    print(solution.abc(nums,k))