# import sys
# s = sys.stdin.readline().strip()
# def abc(s):
#     res = []
#     path = []
#     def is_palindrome(sub):
#         left, right = 0, len(sub) - 1
#         while left < right:
#             if sub[left] != sub[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#     def backtrack(start):
#         if start == len(s):
#             res.append(path[:])
#             return
#         for end in range(start, len(s)):
#             sub = s[start:end + 1]
#             if is_palindrome(sub):
#                 path.append(sub)
#                 backtrack(end + 1)
#                 path.pop()
#     backtrack(0)
#     return res
# print(abc(s))

import sys
s=sys.stdin.readline().strip()
def abc(s):
    def huiwen(sub):
        left,right=0,len(sub)-1
        while left<=right:
            if sub[left]==sub[right]:
                left+=1
                right-=1
            else:
                return False
        return True
    res=[]
    path=[]
    def backtrack(start):
        if start==len(s):
            res.append(path[:])
            return
        for end in range(start,len(s)):
            if huiwen(s[start:end+1]):
                path.append(s[start:end+1])
                backtrack(end+1)
                path.pop()
    backtrack(0)
    return res
print(abc(s))
                