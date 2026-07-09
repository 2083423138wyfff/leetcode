class Solution:
    #哈希表解法
    #排序法
    def hashmap(self,strs):
        hash={}
        for i in strs:
            a=''.join(sorted(i))
            if a not in hash:
                hash[a]=[]
            hash[a].append(i)
        return list(hash.values())
        
if __name__=="__main__":
    import sys
    strs=sys.stdin.readline().split()
    solution=Solution()
    print(solution.hashmap(strs))