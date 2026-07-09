class Solution:
    def abc(self,s,t):
        i = j = 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n




if __name__=="__main__":
    import sys
    solution=Solution()
    s=sys.stdin.readline().split()
    t=sys.stdin.readline().split()
    print(solution.abc(s,t))