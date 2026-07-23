import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
grid=[]
def duqu(line,n):
    if ' 'in line:
        return line.strip()[:n]
    else:
        return list(line)[:n]
for _ in range(m):
     line=sys.stdin.readline()
     grid.append(duqu(line,n))

def abc(grid):
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]
    max_area=0
    
    def bfs(start_row,start_col):
        queue=deque([(start_row,start_col)])
        visited[start_row][start_col]=True
        area=0
        while queue:
            row,col=queue.popleft()
            area+=1
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=row+dr
                nc=col+dc
                if 0<= nr <m and 0<= nc <n and grid[nr][nc]=='1' and not visited[nr][nc]:
                    queue.append((nr,nc))
                    visited[nr][nc]=True
        return area
    
    for row in range(m):
        for col in range(n):
            if not visited[row][col] and grid[row][col]=='1':
                max_area=max(max_area,bfs(row,col))
    return max_area

print(abc(grid))
            