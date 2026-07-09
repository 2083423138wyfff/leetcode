import sys
nums1=list(map(int,sys.stdin.readline().split()))
nums2=list(map(int,sys.stdin.readline().split()))

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def build_list(nums):
    dummy=ListNode(0)
    cur=dummy
    for num in nums:
        cur.next=ListNode(num)
        cur=cur.next
    return dummy.next

def list2array(head):
    l=[]
    cur=head
    while cur:
        l.append(cur.val)
        cur=cur.next
    return l

def abc(head1, head2):
    dummy=ListNode(0)
    cur=dummy
    carry=0
    cur1=head1
    cur2=head2
    while cur1 or cur2 or carry:#链表没走完，或者进位还没消掉，就继续。
        #因为cur1.val和cur2.val不一定能同时存在，所以要分开赋值
        val1=cur1.val if cur1 else 0
        val2=cur2.val if cur2 else 0
        total=val1+val2+carry
        digit=total % 10
        carry=total //10
        cur.next=ListNode(digit)
        cur=cur.next
        if cur1:
            cur1=cur1.next
        if cur2:
            cur2=cur2.next
        
    return dummy.next

print(list2array(abc(build_list(nums1),build_list(nums2))))