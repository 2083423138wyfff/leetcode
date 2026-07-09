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

# def abc(head):#转成列表比较
#     l=list2array(head)
#     return l==l[::-1]

def reverse(head):#反转链表
    pre=None
    cur=head
    while cur:
        rest=cur.next
        cur.next=pre
        pre=cur
        cur=cur.next
    return pre

def findmiddle(head):#找中点
    fast,slow=head,head
    while fast.next and fast.next.next:
        #不用判断是否到末尾，因为fast到了最后的时候，就自动不满足循环条件了
        fast=fast.next.next
        slow=slow.next
    return slow

def abc(head):
    middle=reverse(findmiddle(head))
    while middle and head:
        if head.val!=middle.val:
            return False
        else:
            head=head.next
            middle=middle.next
    return True
    
        

print(abc(build_list(nums)))