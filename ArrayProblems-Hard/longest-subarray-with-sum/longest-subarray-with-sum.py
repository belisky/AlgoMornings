def longestSubarrayWithSum(array, targetSum):
    indices=[]
    currentSum=0
    startingIndex,endingIndex=0,0
    while endingIndex<len(array):
        currentSum+=array[endingIndex]
        while startingIndex<endingIndex and currentSum>targetSum:
            currentSum-=array[startingIndex]
            startingIndex+=1
        if currentSum==targetSum:
            if len(indices)==0 or indices[1]-indices[0]<endingIndex-startingIndex:
                indices=[startingIndex,endingIndex]
        endingIndex+=1
    return indices
    # Write your code here.
   
