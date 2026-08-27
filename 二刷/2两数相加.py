import sys
nums1=list(map(int,sys.stdin.readline().split()))
nums2=list(map(int,sys.stdin.readline().split()))
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
    l=[]
    cur=head
    while cur:
        l.append(cur.val)
        cur=cur.next
    return l

def abc(head1,head2):
    l1=listnode2nums(head1)
    l2=listnode2nums(head2)
    num1=int(''.join(map(str,l1[::-1])))
    num2=int(''.join(map(str,l2[::-1])))
    sum_list=list(map(int,(str(num1+num2).strip())))
    return sum_list[::-1]

# print(abc(nums2listnode(nums1),nums2listnode(nums2)))

def abc1(head1,head2):
    dummy=ListNode(0)
    cur=dummy
    l1=head1
    l2=head2
    carry=0
    while l1 or l2 or carry!=0:
        if l1 :
            x=l1.val
        else:
            x=0
        if l2:
            y=l2.val
        else:
            y=0
        sum_=x+y+carry
        cur.next=ListNode(sum_%10)
        carry=sum_//10
        cur=cur.next
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
    return dummy.next
print(listnode2nums(abc1(nums2listnode(nums1),nums2listnode(nums2))))