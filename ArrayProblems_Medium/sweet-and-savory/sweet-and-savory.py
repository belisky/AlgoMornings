def sweetAndSavory(dishes, target):
    sweetDishes=sorted([dish for dish in dishes if dish<0],key=abs)
    savoryDishes=sorted([dish for dish in dishes if dish>0])
    # print(sweetDishes)
    bestPair=[0,0]
    bestCombination=float('inf')
    sweetIndex,savoryIndex=0,0
    while sweetIndex<len(sweetDishes) and savoryIndex<len(savoryDishes):
        currentPair=sweetDishes[sweetIndex]+savoryDishes[savoryIndex]
        if currentPair<=target:
            currentCombination=target-currentPair
            if currentCombination<bestCombination:
                bestCombination=currentCombination
                bestPair=[sweetDishes[sweetIndex],savoryDishes[savoryIndex]]
            savoryIndex+=1
        else:
            sweetIndex+=1
    return bestPair
    # Write your code here.
    