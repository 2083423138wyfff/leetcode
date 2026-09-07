import sys
strs=list(sys.stdin.readline().split())
def abc(strs):
    #法一，直接利用字符串的排序来实现
    hash={}
    for i in strs:
        key=''.join(sorted(i))
        '''
        if key not in hash:
            hash[key]=[]
        hash[key].append(i)
        '''
        hash.setdefault(key,[]).append(i)
    return list(hash.values())
print(abc(strs))
def ab(strs):
    #法二，利用转数字来实现
    hash={}
    for i in strs:
        count=[0]*26
        for j in i:
            count[ord(j)-ord('a')]+=1
        key=tuple(count)#''.join(map(str,count))
        hash.setdefault(key,[]).append(i)
    return list(hash.values())
print(ab(strs))