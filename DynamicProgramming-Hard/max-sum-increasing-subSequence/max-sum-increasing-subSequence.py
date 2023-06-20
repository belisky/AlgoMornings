def maxSumIncreasingSubsequence(array):
    sequences=[None for x in array]
    increasingSumsAtIndex =[num for num in array]
    maxSumIdx=0
    for i in range(len(array)):
        curNum=array[i]
        for j in range(0,i):
            otherNum=array[j]
            if otherNum<curNum and  increasingSumsAtIndex[j]+curNum>=increasingSumsAtIndex[i]:
                increasingSumsAtIndex[i]=increasingSumsAtIndex[j]+curNum
                sequences[i]=j
        if increasingSumsAtIndex[i]>=increasingSumsAtIndex[maxSumIdx]:
            maxSumIdx=i
    return [increasingSumsAtIndex[maxSumIdx],buildSeq(array,sequences,maxSumIdx)]

def buildSeq(array,sequences,curIdx):
    seq=[]
    while curIdx is not None:
        seq.append(array[curIdx])
        curIdx=sequences[curIdx]
    return list(reversed(seq))
    # Write your code here.
    pass
