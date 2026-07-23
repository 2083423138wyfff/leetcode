import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
def duqu(line,n):
    if ' 'in line:
        return line.split()[:n]
    else:
        return list(line)[:n]
grid=[]
for _ in range(m):
    line=sys.stdin.readline()
    grid.append(duqu(line,n))
    
def abc(grid):
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]
    fresh=0
    minute=0
    queue=deque()
    for row in range(m):
        for col in range(n):
            if grid[row][col]=='1':
                fresh+=1
            if grid[row][col]=='2':
                visited[row][col]=True
                queue.append((row,col))
    if fresh==0:
        return 0
    while queue:
        minute+=1
        for _ in range(len(queue)):
            row,col=queue.popleft()
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr=dr+row
                nc=dc+col
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]=='1':
                    grid[nr][nc]='2'
                    visited[nr][nc]=True
                    queue.append((nr,nc))
                    fresh-=1
    if fresh!=0:
        return -1
    return minute -1
print(abc(grid))
        
    