# import sys

# def daily_temperatures(temperatures):
#     n = len(temperatures)
#     answer = [0] * n
#     stack = []

#     for i in range(n):
#         while stack and temperatures[i] > temperatures[stack[-1]]:
#             prev = stack.pop()
#             answer[prev] = i - prev
#         stack.append(i)

#     return answer

# if __name__ == "__main__":
#     temps = list(map(int, sys.stdin.readline().split()))
#     print(daily_temperatures(temps))
import sys
nums=list(map(int,sys.stdin.readline().split()))
def abc(nums):
    answer=[0 for _ in range(len(nums))]
    stack=[]
    for i in range(len(nums)):
        while stack and nums[i]>nums[stack[-1]]:
            pre=stack.pop()
            answer[pre]=i-pre
        stack.append(i)
    return answer
print(abc(nums))