class Solution:
    def abc(self,nums1,nums2):
        for i in range(len(nums2)):
            nums1[len(nums1)-i-1]=nums2[i]
        return nums1.sort()

        


if __name__=="__main__":
    import sys
    solution=Solution()
    nums1=list(map(int,sys.stdin.readline().split()))
    nums2=list(map(int,sys.stdin.readline().split()))
    print(solution.abc(nums1,nums2))