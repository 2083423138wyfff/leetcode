import sys
s=list(sys.stdin.readline().strip())
st=''.join(c for c in s if c.isalnum()).lower()
def abc(st):
    if len(st)==0:
        return True
    left=0
    right=len(st)-1
    
    while left<=right:
        if st[left]!=st[right]:
            return False
        left+=1
        right-=1
    return True
# print(abc(st))

#变式1 680
def abcd(st):
    if len(st)==0:
        return True
    left=0
    right=len(st)-1
    while left<=right:
        if st[left]!=st[right]:
            return abc(st[left+1:right+1]) or abc(st[left:right])
        left+=1
        right-=1
    return True
# print(abcd(st))

#变式2 5
def abcde(st):
    def expand(l,r,st):
        while l>=0 and r<=len(st)-1 and st[l]==st[r]:
            l-=1
            r+=1
        return l+1,r-1#返回的是元组，这个要记住
    if len(st)==0:
        return 0
    res=1
    start=0
    for i in range(1,len(st)):
        l1,r1=expand(i,i,st)
        l2,r2=expand(i-1,i,st)
        if r1-l1+1>res:
            res=r1-l1+1
            start=l1
        if r2-l2+1>res:
            res=r2-l2+1
            start=l2

    return st[start:start+res]
    
# print(abcde(st))

#变式3 234
import sys
nums=list(map(int,sys.stdin.readline().split()))
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def nums2listnode(nums):
    dummy=ListNode(0)
    cur=dummy
    for num in nums:
        cur.next=ListNode(num)
        cur=cur.next
    return dummy.next
def listnode2nums(head):
    cur=head
    l=[]
    while cur.next:
        l.append(cur.val)
        cur=cur.next
    return l
def findmid(head):
    fast=head
    slow=head
    while fast.next and fast.next.next:
        fast=fast.next.next
        slow=slow.next
    return slow
def reverse(head):
    pre=None
    cur=head
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    return pre
def abc3(head):
    mid=findmid(head)
    re_mid=reverse(mid)
    cur1=head
    cur2=re_mid
    while cur1 and cur2:
        if cur1.val!=cur2.val:
            return False
        cur1=cur1.next
        cur2=cur2.next
    return True
print(abc3(nums2listnode(nums)))