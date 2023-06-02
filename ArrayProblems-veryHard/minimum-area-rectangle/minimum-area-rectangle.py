def minimumAreaRectangle(points):
    coordinatesSet=createPointsSet(points)
    minArea=float("inf")
    for currentIdx,currentPoint in enumerate(points):
        currentX,currentY=currentPoint
        for prevIdx in range(currentIdx):
            prevX,prevY=points[prevIdx]
            pointsShareValue=prevX==currentX or prevY==currentY
            if pointsShareValue:
                continue
            p1OnDiagonal=convertPoint2Str(prevX,currentY) in coordinatesSet
            p2OnDiagonal=convertPoint2Str(currentX,prevY) in coordinatesSet
            oppDiagonals=p1OnDiagonal and p2OnDiagonal
            if oppDiagonals:
                curArea=abs(currentX-prevX)*abs(prevY-currentY)
                minArea=min(minArea,curArea)
    return minArea if minArea!=float("inf") else 0
def createPointsSet(points):
    pointSet=set()
    for point in points:
        x,y=point
        pointsStr=convertPoint2Str(x,y)
        pointSet.add(pointsStr)
    return pointSet
def convertPoint2Str(x,y):
    return str(x)+":"+str(y)
    
 
