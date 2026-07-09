import sys
s=sys.stdin.readline().strip()
for i in range(len(s)):
    if s[i]=='a':
        print(i+1)