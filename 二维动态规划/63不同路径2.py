import sys
m,n=map(int,sys.stdin.readline().split())
grid=[]
def duqu(line,n):
    if ' 'in line:
        return list(map(int,line.split()))[:n]
    else:
        return list(map(int,line.strip()))[:n]
for _ in range(m):
    line=sys.stdin.readline()
    grid.append(duqu(line,n))
    
def abcd(grid):
    m=len(grid)
    n=len(grid[0])
    if grid[0][0]==1:
            return 0
    dp=[[1]*n for _ in range(m)]
    for col in range(n):
        if grid[0][col]==1:
            for j in range(col,n):
                dp[0][j]=0
            break
    for row in range(m):
        if grid[row][0]==1:
            for i in range(row,m):
                dp[i][0]=0
            break
    for row in range(1,m):
        for col in range(1,n):
            if grid[row][col]!=1:
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
            else:
                dp[row][col]=0
    return dp[m-1][n-1]
print(abcd(grid))