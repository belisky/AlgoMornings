def maximumSumSubmatrix(matrix, size):
    sums=createSumMatrix(matrix)
    maxSubMatSum=float('-inf')

    for row in range(size-1,len(matrix)):
        for col in range(size-1,len(matrix[row])):
            tot=sums[row][col]

            touchesTop=row-size<0
            if not touchesTop:
                tot-=sums[row-size][col]
            touchesLeft=col-size<0
            if not touchesLeft:
                tot-=sums[row][col-size]

            touchesTopOrLeft=touchesTop or touchesLeft
            if not touchesTopOrLeft:
                tot+=sums[row-size][col-size]
                
            maxSubMatSum=max(maxSubMatSum,tot)
    return maxSubMatSum
    # Write your code here.
def createSumMatrix(mat):
    sums=[[0 for _ in range(len(mat[row]))] for row in range(len(mat))]
    sums[0][0]=mat[0][0]
    for idx in range(1,len(mat[0])):
        sums[0][idx]=sums[0][idx-1]+mat[0][idx]
    for idx in range(1,len(mat)):
        sums[idx][0]=sums[idx-1][0]+mat[idx][0]
    for row in range(1,len(mat)):
        for col in range(1,len(mat[0])):
            sums[row][col]=sums[row-1][col]+sums[row][col-1]-sums[row-1][col-1]+mat[row][col]
    return sums
