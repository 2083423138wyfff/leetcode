import sys
word1=sys.stdin.readline().strip()
word2=sys.stdin.readline().strip()
def abc(word1,word2):
    i=0
    res=''
    while i<len(word1) and i<len(word2):
        res=res+word1[i]+word2[i]
        i+=1
    if len(word1)>i:
        res=res+word1[i:len(word1)]
    elif len(word2)>i:
        res=res+word2[i:len(word2)]
    return res
print(abc(word1,word2))