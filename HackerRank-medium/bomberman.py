#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
# O(log(n))

def bomberMan(n, grid):
    c,r=len(grid[0]),len(grid)
    if n<2: return grid
    if n%2==0: return ['O'*c for _ in range(r)]
    n//=2    
    for q in range((n+1)%2+1):
        new_grid=[['O']*c for i in range(r)]
        coordinates=[(0,0),(0,-1),(-1,0),(1,0),(0,1)]
        def detonate(x,y):
            if 0<=x<r and 0<=y<c: new_grid[x][y]='.'
        for row in range(r):
            for col in range(c):
                if grid[row][col]=='O':
                    for i,j in coordinates:
                        detonate(row+i,col+j)
        grid=new_grid
    return ["".join(x) for x in grid]
    
    # Write your code here
