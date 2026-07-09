class Solution:
    def abc(self,word1,word2):
        l=[]
        for i in range(min(len(word1),len(word2))):
            l.append(word1[i])
            l.append(word2[i])
        if len(word1)>len(word2):
            l.append(word1[len(word2):])
        else:
            l.append(word2[len(word1):])
        return ''.join(l) 



if __name__=="__main__":
    import sys
    solution=Solution()
    word1=sys.stdin.readline().split()
    word2=sys.stdin.readline().split()
    print(solution.abc(word1,word2))