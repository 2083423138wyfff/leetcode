import sys
nums1=list(map(int,sys.stdin.readline().split()))
nums2=list(map(int,sys.stdin.readline().split()))
def abc(nums1,nums2):
    #确保nums1是长的那个
    if len(nums1)<len(nums2):
        nums1,nums2=nums2,nums1
    nums1 = nums1 + [0] * len(nums2)
    ins1=len(nums1)-1-len(nums2)
    ins2=len(nums2)-1
    ins=len(nums1)-1
    while ins2>=0:
        if ins1>=0 and nums1[ins1]>nums2[ins2]:
            nums1[ins]=nums1[ins1]
            ins1-=1
        else:
            nums1[ins]=nums2[ins2]
            ins2-=1
        ins-=1
    return nums1
print(abc(nums1,nums2))