def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]

    numberOfWays = 0
    for step in range(1, min(maxSteps, height)+1):
        numberOfWays += numberOfWaysToTop(height-step, maxSteps, memoize)
    memoize[height] = numberOfWays

    return numberOfWays


# solution 2

# def staircaseTraversal(height, maxSteps):
#     waysToTop=[0 for _ in range(height+1)]
#     waysToTop[0]=1
#     waysToTop[1]=1

#     for currentHeight in range(2,height+1):
#         step=1
#         while step<=maxSteps and step<=currentHeight:
#             waysToTop[currentHeight]=waysToTop[currentHeight]+waysToTop[currentHeight-step]
#             step+=1
#     return waysToTop[height]
