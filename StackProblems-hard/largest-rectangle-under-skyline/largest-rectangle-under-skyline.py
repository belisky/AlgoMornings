def largestRectangleUnderSkyline(buildings):
    pillarIdx = []
    maxArea = 0

    for idx, height in enumerate(buildings+[0]):
        while len(pillarIdx) != 0 and buildings[pillarIdx[-1]] > height:
            pillarHeight = buildings[pillarIdx.pop()]
            width = idx if len(pillarIdx) == 0 else idx-(pillarIdx[-1]+1)
            maxArea = max(width*pillarHeight, maxArea)

        pillarIdx.append(idx)
    return maxArea


# solution 2
# O(n^2) time and O(n) space
# def largestRectangleUnderSkyline(buildings):
#     maxArea=0
#     for pillarIdx in range(len(buildings)):
#         currentHeight=buildings[pillarIdx]

#         furtherLeft=pillarIdx
#         while furtherLeft>0 and buildings[furtherLeft-1]>=currentHeight:
#             furtherLeft-=1

#         furtherRight=pillarIdx
#         while furtherRight<len(buildings)-1 and buildings[furtherRight+1]>=currentHeight:
#             furtherRight+=1
#         areaWithCurrentBuilding=(furtherRight-furtherLeft+1)*currentHeight
#         maxArea=max(areaWithCurrentBuilding,maxArea)

#     return maxArea
#     # Write your code here.
#     return 0
