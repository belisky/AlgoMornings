#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#O(n^2)
 

def twoPluses(grid):
    r=len(grid)
    c=len(grid[0])    
    
    sumstack=[]
    setstack=[]
    
    for row in range(r):
        for col in range(c):
            if grid[row][col]=='G':
                sums=1
                t=1
                set1={(row,col)}
                while col+t<=c-1 and col-t>=0 and row+t<=r-1 and row-t>=0:
                    if grid[row+t][col]==grid[row-t][col]==grid[row][col+t]==grid[row][col-t]=='G':                      
                        
                        set1.update({(row+t,col),(row-t,col),(row,col-t),(row,col+t)})
                        
                        sums+=4
                        t+=1
                        sumstack.append(sums)
                        setstack.append(set1.copy())
                    else:
                        break
    ans=float('-inf')
    if len(sumstack)==1:
        return sumstack[0]
    elif len(sumstack)==0:
        return 1
        
    
    for i in range(len(sumstack)-1):
        for j in range(i+1,len(sumstack)):
            if setstack[i].isdisjoint(setstack[j]):
                ans=max(ans,sumstack[i]*sumstack[j])
     
    return sumstack[0] if ans==float('-inf') else ans  