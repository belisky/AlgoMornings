def diskStacking(disks):
    disks.sort(key=lambda disk:disk[2])
    heights=[disk[2] for disk in disks]
    seq=[None for disk in disks]
    maxHeightIdx=0
    for i in range(1,len(disks)):
        curDisk=disks[i]
        for j in range(i):
            otherDisk=disks[j]
            if stackable(otherDisk,curDisk):
                if heights[i]<curDisk[2]+heights[j]:
                    heights[i]=curDisk[2]+heights[j]
                    seq[i]=j
        if heights[i]>=heights[maxHeightIdx]:
            maxHeightIdx=i
        
    return buildSeq(disks,seq,maxHeightIdx)

def stackable(o,c):
    return o[0]<c[0] and o[1]<c[1] and o[2]<c[2]

def buildSeq(array,seq,curIdx):
    sequence=[]
    while curIdx is not None:
        sequence.append(array[curIdx])
        curIdx=seq[curIdx]
    return list(reversed(sequence))
    # Write your code here.
    
