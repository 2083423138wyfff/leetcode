import sys
m,n=map(int,sys.stdin.readline().split())
def duqu(line):
    if ' 'in line:
        return line.split()[:n]
    else:
        return list(line)
    
grid=[]
for _ in range(m):
    line=sys.stdin.readline()
    grid.append(duqu(line))

def abc(grid):
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]
    max_area=0
    def dfs(row,col):
        if row<0 or row>=m or col<0 or col>=n:
            return 0
        if visited[row][col]:
            return 0
        if grid[row][col]!='1':
            return 0
        visited[row][col]=True
        return 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
    for row in range(m):
        for col in range(n):
            max_area=max(max_area,dfs(row,col))
    return max_area

print(abc(grid))
    
