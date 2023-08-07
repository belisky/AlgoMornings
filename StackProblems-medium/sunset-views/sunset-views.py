def sunsetViews(buildings, direction):
    buildingsWithSunsetView = []

    start = 0 if direction == 'WEST' else len(buildings)-1
    step = 1 if direction == 'WEST' else -1

    idx = start
    runningMax = 0
    while idx >= 0 and idx < len(buildings):
        curHeight = buildings[idx]
        if curHeight > runningMax:
            buildingsWithSunsetView.append(idx)

        runningMax = max(runningMax, curHeight)
        idx += step

    if direction == 'EAST':
        return buildingsWithSunsetView[::-1]
    return buildingsWithSunsetView
    # Write your code here.

# solution 2
# def sunsetViews(buildings, direction):
#     candidateBuildings=[]
#     startIdx=0 if direction=='EAST' else len(buildings)-1
#     step=1 if direction == 'EAST' else -1
#     idx=startIdx
#     while idx>=0 and idx<len(buildings):
#         # print(idx)
#         buildingHeight=buildings[idx]
#         while len(candidateBuildings)>0 and buildings[candidateBuildings[-1]]<=buildingHeight:
#             candidateBuildings.pop()
#             # print(candidateBuildings)
#         candidateBuildings.append(idx)
#         # print(candidateBuildings)
#         idx+=step
#     print(candidateBuildings)
#     if direction=='WEST':
#         return candidateBuildings[::-1]
#     return candidateBuildings


#     # Write your code here.
#     return []
