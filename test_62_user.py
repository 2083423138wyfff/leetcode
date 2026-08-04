import sys

def abc(m,n):
    count=0
    if m<=0 and n<=0:
        return 0
    elif m<=0 and n>0:
        count+=1
    elif m>0 and n<=0:
        count+=1
    else:
        count+=2
    return abc(m-1,n)+abc(m,n-1)+count

print(abc(3, 2))
print(abc(3, 7))
