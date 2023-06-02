from fractions import Fraction
def lineThroughPoints(points):
    maxPointsOnLine=1
    for i in range(len(points)-1):
        x1,y1=points[i]
        slopes={}
        for j in range(i+1,len(points)):
            x2,y2=points[j]
            slope=Fraction(y2-y1,x2-x1) if x1!=x2 else float("inf")
            numerator,denominator=(1,0) if slope==float("inf") else (slope.numerator,slope.denominator)
            if (numerator,denominator) not in slopes:
                slopes[(numerator,denominator)]=1
            slopes[(numerator,denominator)]+=1

        currentMaxPointsOnLine=max(slopes.values())
        maxPointsOnLine=max(currentMaxPointsOnLine,maxPointsOnLine)
    return maxPointsOnLine
 
