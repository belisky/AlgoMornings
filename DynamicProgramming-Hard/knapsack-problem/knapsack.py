def knapsackProblem(items, capacity):
    knapSackValues=[[0 for x in range(0,capacity+1)] for y in range(0,len(items)+1)]
    for itemIdx in range(1,len(items)+1):
        curWeight=items[itemIdx-1][1]
        curValue=items[itemIdx-1][0]
        for capa in range(0,capacity+1):
            if curWeight>capa:
                knapSackValues[itemIdx][capa]=knapSackValues[itemIdx-1][capa]
            else:
                knapSackValues[itemIdx][capa]=max(knapSackValues[itemIdx-1][capa],knapSackValues[itemIdx-1][capa-curWeight]+curValue)
    return [knapSackValues[-1][-1],getKnapSackItems(knapSackValues,items)]

def getKnapSackItems(knapSackValues,items):
    seq=[]
    itemSize=len(knapSackValues)-1
    col=len(knapSackValues[0])-1
    while itemSize>0:
        if knapSackValues[itemSize][col]==knapSackValues[itemSize-1][col]:
            itemSize-=1
        else:
            # print(i,i-1)
            seq.append(itemSize-1)
            col-=items[itemSize-1][1]
            itemSize-=1
        if col==0:
            break
    return list(reversed(seq))
 
   
