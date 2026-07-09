import sys
nums=list(map(int,sys.stdin.readline().split()))
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

def swap_pairs(head):
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    while pre.next and pre.next.next:
        first=pre.next
        second=pre.next.next
        rest=second.next
        pre.next=second
        second.next=first
        first.next=rest
        pre=first
    return dummy.next

print(list2array(swap_pairs(build_list(nums))))
     
        
        
    