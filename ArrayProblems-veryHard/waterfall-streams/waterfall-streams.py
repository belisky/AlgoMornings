def waterfallStreams(array, source):
    rowAbove=array[0][:]
    rowAbove[source]=-1
    for row in range(1,len(array)):
        currentRow=array[row][:]
        for cell in range(len(rowAbove)):
            hasWaterAbove=rowAbove[cell]<0
            hasBlock=currentRow[cell]==1
            if not hasWaterAbove:
                continue
            if not hasBlock:
                currentRow[cell]+=rowAbove[cell]
                continue
            splitWater=rowAbove[cell]/2
            rightIdx=cell
            while rightIdx+1<len(rowAbove):
                rightIdx+=1
                if rowAbove[rightIdx]==1:
                    break
                if currentRow[rightIdx]!=1:
                    currentRow[rightIdx]+=splitWater
                    break
            leftIdx=cell
            while leftIdx-1>=0:
                leftIdx-=1
                if rowAbove[leftIdx]==1:
                    break
                if currentRow[leftIdx]!=1:
                    currentRow[leftIdx]+=splitWater
                    break
        rowAbove=currentRow
    return (list(map(lambda x: x*-100,rowAbove)))
  
   
