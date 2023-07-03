def juiceBottling(prices):
    numSizes=len(prices)
    maxProfit=[0]*numSizes
    solutions=[[]] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size+1):
            possibleProfit=maxProfit[size-dividingPoint]+prices[dividingPoint]

            if possibleProfit>maxProfit[size]:
                maxProfit[size]=possibleProfit
                solutions[size]=[dividingPoint]+solutions[size-dividingPoint]
    return solutions[numSizes-1]
    # Write your code here.
     
