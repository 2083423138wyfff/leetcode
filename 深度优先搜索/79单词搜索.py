import sys

m,n=map(int,sys.stdin.readline().split())

def duqu(line):
    if ' 'in line:
        return line.split()[:n]
    else:
        return list(line)[:n]
grid=[]
for _ in range(m):
    line=sys.stdin.readline().strip()
    grid.append(duqu(line))

word=''.join(sys.stdin.readline().strip())

def abc(grid,word):
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]
    def dfs(row,col,index):
        if index==len(word):
            return True
        if row<0 or row>=m or col<0 or col>=n:
            return False
        if visited[row][col]:
            return False
        if grid[row][col]!=word[index]:
            return False
        visited[row][col]=True
        res= (
            dfs(row+1,col,index+1) or
            dfs(row-1,col,index+1) or
            dfs(row,col+1,index+1) or
            dfs(row,col-1,index+1)
        )
        visited[row][col]=False
        return res
        
    for row in range(m):
        for col in range(n):
            if dfs(row,col,0):
                return True
    return False

print(abc(grid,word))
        