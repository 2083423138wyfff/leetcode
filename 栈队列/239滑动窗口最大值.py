import sys
nums=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())
# def abc(nums,k):
#     if len(nums)<k:
#         return -1
#     res=[0 for _ in range(len(nums)-k+1)]
#     for i in range(len(nums)-k+1):
#         res[i]=max(nums[i:i+k])
#     return res
def abc(nums,k):
    from collections import deque
    result = []
    dq = deque()

    for i in range(len(nums)):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(abc(nums,k))
