import sys
class Solution:
    def abc(self,n,s,w):
        #不进行反转的时候
        ans=0
        max1=0
        max2=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                ans+=w[i]
                gain=-w[i]
            else:
                gain=w[i]
        #反转只影响左右最大相容度
            if gain>max1:
                max2=max1
                max1=gain
            elif gain>max2:
                max2=gain
        return ans+max1+max2

if __name__=='__main__':
    solution=Solution()
    n=int(sys.stdin.readline().strip())
    s=sys.stdin.readline().strip()
    w=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(n,s,w))
