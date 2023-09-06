def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n-1-leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTrees += numberOfLeftTrees*numberOfRightTrees
    return numberOfTrees
