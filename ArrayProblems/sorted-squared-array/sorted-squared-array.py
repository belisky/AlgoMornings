def sortedSquaredArray(array):
    sortedSquares=[0]*len(array)
    largerValueIndex=len(array)-1
    currentPointer=largerValueIndex
    smallerValueIndex=0
    while currentPointer>=0:
        if abs(array[largerValueIndex])>abs(array[smallerValueIndex]):
            # print(array[max],array[min],array[max]**2)
            sortedSquares[currentPointer]=array[largerValueIndex]**2
            currentPointer-=1
            largerValueIndex-=1
        else:
            sortedSquares[currentPointer]=array[smallerValueIndex]**2
            smallerValueIndex+=1
            currentPointer-=1
    
    # Write your code here.
    return sortedSquares
