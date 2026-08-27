import sys
haystack=sys.stdin.readline().strip()
needle=sys.stdin.readline().strip()
def abc(l1,l2):
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]==l2[j]:
            i+=1
            j+=1
        else:
            i=i-j+1
            j=0
        if j==len(l2):
            return i-j
    return -1
print(abc(haystack,needle))

#变式2 KMP
def abc2(l1,l2):
    