def numberOfWaysToTraverseGraph(width, height):
    numOfWays=[[0 for _ in range(width+1)] for _ in range(height+1)]
    for widthIdx in range(1,width+1):
        for heightIdx in range(1,height+1):
            if widthIdx==1 or heightIdx==1:
                numOfWays[heightIdx][widthIdx]=1
            else:
                waysLeft=numOfWays[heightIdx][widthIdx-1]
                waysUp=numOfWays[heightIdx-1][widthIdx]
                numOfWays[heightIdx][widthIdx]=waysLeft+waysUp
    # Write your code here.
    return numOfWays[height][width]
