
import sys
m,n=map(int,sys.stdin.readline().split())
def duqu(line,n):
    if ' 'in line:
        return line.split()[:n]
    else:
        return list(line)[:n]

grid=[]
for _ in range(m):
    line=sys.stdin.readline().strip()
    grid.append(duqu(line,n))

def abc(grid):
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]
    # visited=[[False]for _ in range(n) for _ in range(m)]
    count=0
    def dfs(row,col):
        if row<0 or row>=m or col<0 or col>=n:
            return
        if grid[row][col]=='0':
            return
        if visited[row][col]:
            return
        visited[row][col]=True
        dfs(row-1,col)
        dfs(row+1,col)
        dfs(row,col-1)
        dfs(row,col+1)
    for row in range(m):
        for col in range(n):
            if grid[row][col]=='1' and not visited[row][col]:
                dfs(row,col)
                count+=1
    return count
print(abc(grid))
        