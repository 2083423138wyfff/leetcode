import sys
s=list(sys.stdin.readline().strip())
def abc(s):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        if ch in ')]}':
            if len(stack) == 0 or pairs[ch] != stack[-1]:
                return False
            stack.pop()
print(abc(s))