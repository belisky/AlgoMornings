def minimumAreaRectangle(points):
    pSet=createPSet(points)
    minArea=float("inf")
    for curIdx,p2 in enumerate(points):
        p2x,p2y=p2
        for prevIdx in range(curIdx):
            p1x,p1y=points[prevIdx]
            pointsShareVal=p1x==p2x or p1y==p2y
            if pointsShareVal:
                continue
            p1OnDiag=convertP2Str(p1x,p2y) in pSet
            p2OnDiag=convertP2Str(p2x,p1y) in pSet
            oppDiag=p1OnDiag and p2OnDiag
            if oppDiag:
                curArea=abs(p2x-p1x)*abs(p1y-p2y)
                minArea=min(minArea,curArea)
    return minArea if minArea!=float("inf") else 0
def createPSet(points):
    pSet=set()
    for p in points:
        x,y=p
        pStr=convertP2Str(x,y)
        pSet.add(pStr)
    return pSet
def convertP2Str(x,y):
    return str(x)+":"+str(y)
    
 
