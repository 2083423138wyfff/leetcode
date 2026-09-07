import sys
from collections import deque
strs=sys.stdin.readline().strip()
def abc(strs):
    queue=deque()
    res=0
    for i in range(len(strs)):
        if strs[i] not in queue:
            queue.append(strs[i])
        else:
            res=max(res,len(queue))
            while strs[i] in queue:
                queue.popleft()
            queue.append(strs[i])
    res=max(res,len(queue))
    return res
print(abc(strs))