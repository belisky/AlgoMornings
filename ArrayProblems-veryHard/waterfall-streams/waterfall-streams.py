def waterfallStreams(array, source):
    rowAbove=array[0][:]
    rowAbove[source]=-1
    for row in range(1,len(array)):
        curRow=array[row][:]
        for space in range(len(rowAbove)):
            hasWaterAbove=rowAbove[space]<0
            hasBlock=curRow[space]==1
            if not hasWaterAbove:
                continue
            if not hasBlock:
                curRow[space]+=rowAbove[space]
                continue
            splitWater=rowAbove[space]/2
            rightIdx=space
            while rightIdx+1<len(rowAbove):
                rightIdx+=1
                if rowAbove[rightIdx]==1:
                    break
                if curRow[rightIdx]!=1:
                    curRow[rightIdx]+=splitWater
                    break
            leftIdx=space
            while leftIdx-1>=0:
                leftIdx-=1
                if rowAbove[leftIdx]==1:
                    break
                if curRow[leftIdx]!=1:
                    curRow[leftIdx]+=splitWater
                    break
        rowAbove=curRow
    return (list(map(lambda x: x*-100,rowAbove)))
    # Write your code here.
   
