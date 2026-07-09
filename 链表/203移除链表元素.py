import sys
nums=list(map(int,sys.stdin.readline().split()))
val=int(sys.stdin.readline())
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

def delete_val(head,val):
    while head and head.val==val:
        head=head.next
    cur=head
    while cur and cur.next:
        if cur.next.val==val:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head

print(list2array(delete_val(build_list(nums),val)))