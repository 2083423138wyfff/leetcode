import sys
from collections import deque

m,n=map(int,sys.stdin.readline().split())

def duqu(line,n):
    if ' ' in line:
        return ''.join(line.split())[:n]
    else:
        return list(line)[:n]

grid=[]
for _ in range(m):
    line=sys.stdin.readline().strip()
    grid.append(duqu(line,n))

def abc(grid):
    m=len(grid)
    n=len(grid[0])
    visited=[[False] * n for _ in range(m)]
    count=0
    
    def bfs(start_row,start_col):
        queue=deque([(start_row,start_col)])
        visited[start_row][start_col]=True
        while queue:
            row,col=queue.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=row+dr,col+dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc]=True
                    queue.append((nr,nc))
         
    for row in range(m):
        for col in range(n):
            if grid[row][col]=='1' and not visited[row][col]:
                count+=1
                bfs(row,col)
    
    return count

print(abc(grid))