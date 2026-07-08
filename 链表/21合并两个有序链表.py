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

def mergeTwoLists(head1,head2):
    dummy=ListNode(0)
    cur=dummy
    cur1=head1
    cur2=head2
    while cur1 and cur2:
        if cur1.val<cur2.val:
            cur.next=cur1
            cur=cur.next
            cur1=cur1.next
        else:
            cur.next=cur2
            cur=cur.next
            cur2=cur2.next
    cur.next=cur1 if cur1 else cur2
    return dummy.next

print(list2array(mergeTwoLists(build_list(nums1),build_list(nums2))))