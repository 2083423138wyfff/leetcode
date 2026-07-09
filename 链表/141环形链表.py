
import sys
nums=list(map(int,sys.stdin.readline().split()))
pos=int(sys.stdin.readline())

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
#自创方法
# def build_list(nums,pos):
#     dummy=ListNode(0)
#     cur=dummy
#     if pos ==-1:
#         for num in nums:
#             cur.next=ListNode(num)
#             cur=cur.next
#         return dummy.next
#     else:
#         count=0
#         for num in nums:
#             cur.next=ListNode(num)
#             cur=cur.next
#             if pos==count:
#                 a=cur
#             count+=1
#         cur.next=a
#         return dummy.next
def build_list(nums,pos):
    dummy=ListNode(0)
    cur=dummy
    nodes=[]
    for num in nums:
        node=ListNode(num)
        cur.next=node
        cur=node
        nodes.append(node)
    if pos!=-1:
        cur.next=nodes[pos]
    return dummy.next

def list2array(head):
    l=[]
    cur=head
    while cur:
        l.append(cur.val)
        cur=cur.next
    return l

def abc(head):
    fast,slow=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast == slow:
            return True
    return False

print(abc(build_list(nums,pos)))