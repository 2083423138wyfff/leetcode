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

def reverse_list(head):
    '''
    cur当前处理的节点
    pre待处理的新头
    nxt临时保存cur的下一个节点
    '''
    
    pre=None
    cur=head
    while cur:
        rest=cur.next#先记住下一个节点，防止断链
        cur.next=pre#把当前节点反过来指向前一个
        pre=cur#前进一步，站到当前节点位置
        cur=rest# 前进一步，去处理下一个节点
    return pre

print(list2array(reverse_list(build_list(nums))))
        
        