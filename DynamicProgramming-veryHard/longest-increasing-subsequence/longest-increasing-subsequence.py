def longestIncreasingSubsequence(array):
    seq=[None for _ in array]
    lengths=[1 for _ in array]
    maxLen=0
    for i in range(len(array)):
        cur=array[i]
        for j in range(0,i):
            other=array[j]
            if other<cur and lengths[j]+1>=lengths[i]:
                lengths[i]=lengths[j]+1
                seq[i]=j
        if lengths[i]>=lengths[maxLen]:
            maxLen=i
    return buildSeq(array,seq,maxLen)
def buildSeq(array,seq,curIdx):
    sequence=[]
    while curIdx is not None:
        sequence.append(array[curIdx])
        curIdx=seq[curIdx]
    return list(reversed(sequence))

                # Write your code here.
    pass
